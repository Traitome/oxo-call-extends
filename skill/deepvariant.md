---
name: deepvariant
category: variant-calling
description: DeepVariant - Google's deep learning based variant caller for germline SNPs/indels from Illumina, PacBio HiFi and ONT sequencing data.
tags: [deepvariant, variant-calling, deep-learning, snp, indel, cnn, germline, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/google/deepvariant"
---

## Concepts

- **Tool Overview**: DeepVariant (v1.6.x / v1.9.x) is Google's deep learning-based germline variant caller. It reformulates variant calling as an image classification problem: alignments at each locus are encoded into multi-channel "pileup image" tensors and classified by a CNN (Inception-v3 / EfficientNet-B3 depending on version) as reference, SNP, or indel. The model checkpoint is platform-specific.
- **Model Types** (`--model_type`):
  - `WGS` — Illumina whole-genome sequencing (default model).
  - `WES` — Illumina whole-exome / targeted panels.
  - `PACBIO` — PacBio HiFi long reads.
  - `ONT_R104` — Oxford Nanopore R10.4 chemistry.
  - `HYBRID_PACBIO_ILLUMINA` — hybrid assemblies (DeepTrio extension).
- **Three-Stage Pipeline** (run sequentially by `run_deepvariant`):
  1. `make_examples` — scans BAM/CRAM, identifies candidate loci, encodes them as TFRecord tensors. Single-threaded per task; supports `--task` sharding for parallelism (`examples.tfrecord@N.gz` produces N shards).
  2. `call_variants` — runs CNN inference on the TFRecord shards using a model checkpoint, emitting `call_variants_output.tfrecord.gz`.
  3. `postprocess_variants` — sorts calls, collapses multi-allelic records, and writes the final VCF (and gVCF if requested).
- **Entry Point**: `run_deepvariant` is a wrapper script that runs all three stages. In the official Docker image it lives at `/opt/deepvariant/bin/run_deepvariant`. Running the bare `deepvariant` binary is **not** the documented usage.
- **Input Requirements**:
  - Reference FASTA: must be indexed with `samtools faidx` (bgzipped or plain FASTA both accepted).
  - BAM/CRAM: coordinate-sorted and indexed (`.bai`/`.csi`); reads must be aligned to a reference compatible with `--ref` (shared contig names). Duplicate marking recommended (via `picard MarkDuplicates`); BQSR **not** recommended (small accuracy loss).
  - Optional `--regions` (BED or `chr:start-end` space-separated list) restricts calling to intervals.
- **Output**: VCF (bgzipped by default) and optional gVCF (`--output_gvcf`). The gVCF enables downstream joint genotyping with GLnexus.
- **GPU Acceleration**: The `-gpu` Docker image (`google/deepvariant:1.6.1-gpu`) + `--use_gpu` flag uses TensorFlow-GPU. NVIDIA Parabricks (`pbrun deepvariant`) provides further CUDA optimisation (30× WGS in ~8 min on DGX).
- **Joint Genotyping**: For cohort-level calling, run DeepVariant per-sample with `--output_gvcf`, then merge gVCFs with `glnexus_cli --config DeepVariantWGS` (or `DeepVariantWES`, `DeepVariant_unfiltered`).
- **Installation**: Docker (`docker pull google/deepvariant:1.6.1`) is the official path. Also available via `conda install -c bioconda deepvariant` (CPU-only build).
- **Use Case**: High-accuracy germline SNP/indel calling in WGS/WES/HiFi/ONT; trio phasing via DeepTrio; somatic-low-AF via DeepSomatic.

## Pitfalls

- **The bare `deepvariant` binary is not the documented entry point**. Use `run_deepvariant` (or `run_deepvariant.py` in older versions). The command `deepvariant --model_type WGS ...` shown in some tutorials is incorrect — the correct invocation is `run_deepvariant --model_type=WGS ...`.
- **Model type must match sequencing platform**. Using `WGS` on PacBio HiFi or `PACBIO` on Illumina data produces poor accuracy. The model checkpoints encode platform-specific error profiles (e.g. ONT R10.4 vs R9.4 are not interchangeable).
- **BAM must be sorted and indexed**. Without a `.bai`/`.csi`, `make_examples` silently fails or produces empty output. Run `samtools sort -o sorted.bam raw.bam && samtools index sorted.bam` first.
- **Reference must be faidx-indexed**. Missing `.fai` causes `make_examples` to crash on contig lookup. The FASTA and BAM must share contig names (e.g. `chr1` vs `1` mismatch silently excludes chromosomes).
- **BQSR is discouraged**. Base Quality Score Recalibration slightly reduces DeepVariant accuracy because the CNN was trained on raw base qualities. Run BWA-MEM2 + MarkDuplicates only.
- **Duplicate marking matters at low coverage**. Below ~20×, unmarked duplicates noticeably inflate false positives. Always run `picard MarkDuplicates` or `samtools markdup` before DeepVariant.
- **`--num_shards` should match available cores**. Each shard spawns a `make_examples` process; setting `--num_shards 64` on an 8-core node just thrashes the scheduler. Typical value: `$(nproc)` or 16–32.
- **GPU mode needs the `-gpu` image**. The CPU image lacks CUDA libs; `--use_gpu` will silently fall back or error. Pull `google/deepvariant:1.6.1-gpu` and run `docker run --gpus all ...`.
- **CRAM requires `--ref`**. DeepVariant decodes CRAM via pysam, which needs the reference FASTA path. Passing a CRAM without `--ref` raises a "missing reference" error.
- **gVCF only when `--output_gvcf` is set**. Without the flag, DeepVariant writes a VCF containing only variant sites — non-variant blocks (`<NON_REF>`) are dropped, breaking GLnexus joint genotyping.
- **Region restriction with `--regions` needs matching contig names**. `--regions chr20` on a GRCh37 BAM (where contigs are `20`) silently skips the region. Use `--regions 20` or rename contigs.
- **`make_examples_extra_args "ws_use_window_selector_model=true"` is the production default**. The legacy Allele-Count-Linear window selector is faster but less accurate; production pipelines always set the model-based selector.
- **Memory grows with coverage**. At >60× WGS, `make_examples` peak RAM ~8 GB per shard; on a 16-shard run that is ~128 GB total. Reduce `--num_shards` or partition by chromosome.

## Examples

### Call variants from Illumina WGS BAM
**Args:** `docker run -v "${PWD}:/input" -v "${PWD}/out:/output" google/deepvariant:1.6.1 /opt/deepvariant/bin/run_deepvariant --model_type=WGS --ref=/input/ref.fa --reads=/input/sample.bam --output_vcf=/output/sample.vcf.gz --num_shards=16`
**Explanation:** `-v` mounts host dirs; `--model_type=WGS` selects the Illumina WGS checkpoint (bundled at `/opt/models/wgs/model.ckpt`); `--ref` is the FASTA used for alignment (must be faidx-indexed); `--reads` is the sorted+indexed BAM; `--output_vcf` writes a bgzipped VCF; `--num_shards=16` parallelises `make_examples` across 16 cores.

### Call variants with gVCF for joint genotyping
**Args:** `docker run -v "${PWD}:/data" google/deepvariant:1.6.1 /opt/deepvariant/bin/run_deepvariant --model_type=WGS --ref=/data/ref.fa --reads=/data/sample.bam --output_vcf=/data/sample.vcf.gz --output_gvcf=/data/sample.g.vcf.gz --num_shards=16`
**Explanation:** `--output_gvcf` writes a gVCF containing both variant sites and non-variant blocks (`<NON_REF>`); this is the required input for `glnexus_cli --config DeepVariantWGS` cohort merging. The `.g.vcf.gz` is bgzipped and tabix-friendly.

### Call variants from PacBio HiFi reads
**Args:** `docker run -v "${PWD}:/data" google/deepvariant:1.6.1 /opt/deepvariant/bin/run_deepvariant --model_type=PACBIO --ref=/data/hg38.fa --reads=/data/hifi.bam --output_vcf=/data/hifi.vcf.gz --output_gvcf=/data/hifi.g.vcf.gz --num_shards=16`
**Explanation:** `--model_type=PACBIO` uses the HiFi-optimised model (trained on PacBio CCS ≥Q20); `--output_gvcf` enables downstream joint calling; `--num_shards=16` parallelises `make_examples`. HiFi calling typically achieves SNP F1 >99.7% on GIAB HG002.

### Call variants from ONT R10.4 simplex reads with GPU
**Args:** `docker run --gpus all -v "${PWD}:/data" google/deepvariant:1.6.1-gpu /opt/deepvariant/bin/run_deepvariant --model_type=ONT_R104 --ref=/data/hg38.fa --reads=/data/ont.bam --output_vcf=/data/ont.vcf.gz --use_gpu --num_shards=8`
**Explanation:** `--gpus all` exposes the host GPU to the container; the `-gpu` image ships TensorFlow-GPU + CUDA; `--model_type=ONT_R104` matches R10.4 chemistry; `--use_gpu` routes `call_variants` inference to the GPU (reduces WGS runtime from ~5 h to ~30 min); `--num_shards=8` balances CPU-side `make_examples` parallelism with GPU memory.

### WES / targeted panel calling with interval restriction
**Args:** `docker run -v "${PWD}:/data" google/deepvariant:1.6.1 /opt/deepvariant/bin/run_deepvariant --model_type=WES --ref=/data/hg38.fa --reads=/data/exome.bam --regions=/data/targets.bed --output_vcf=/data/exome.vcf.gz --num_shards=8`
**Explanation:** `--model_type=WES` selects the exome-optimised checkpoint (trained on Agilent SureSelect); `--regions=/data/targets.bed` restricts `make_examples` to the capture intervals, dramatically cutting runtime; `--num_shards=8` is sufficient for ~50 Mb exome targets. Note: BED must use the same contig naming as the BAM (e.g. `chr1`).

### Restrict calling to a chromosome interval
**Args:** `docker run -v "${PWD}:/data" google/deepvariant:1.6.1 /opt/deepvariant/bin/run_deepvariant --model_type=WGS --ref=/data/ref.fa --reads=/data/sample.bam --regions="chr20:10000000-20000000" --output_vcf=/data/chr20.vcf.gz --num_shards=4`
**Explanation:** `--regions` accepts UCSC-style intervals (`chr:start-end`, 1-based inclusive) or whole contig names; space-separated lists are supported (`--regions "chr20 chr21"`). Useful for testing parameters quickly or running per-chromosome jobs on a cluster.

### Run the three stages manually for fine-grained control
**Args:** `make_examples --mode calling --ref ref.fa --reads sample.bam --examples examples.tfrecord@16.gz --task 0 && call_variants --outfile calls.tfrecord.gz --examples "examples.tfrecord@16.gz" --checkpoint /opt/models/wgs/model.ckpt && postprocess_variants --ref ref.fa --infile calls.tfrecord.gz --outfile final.vcf.gz`
**Explanation:** `make_examples --task 0` processes shard 0 of 16 (run in parallel via GNU `parallel` for all shards); `--examples examples.tfrecord@16.gz` specifies sharded output; `call_variants --checkpoint` loads the CNN weights; `postprocess_variants --infile` consumes the raw calls and emits a sorted VCF. Use this when you want custom sharding, custom checkpoints, or to distribute across nodes.

### Multi-sample cohort: per-sample gVCFs then GLnexus joint calling
**Args:** `for bam in *.bam; do s=$(basename $bam .bam); docker run -v "${PWD}:/data" google/deepvariant:1.6.1 /opt/deepvariant/bin/run_deepvariant --model_type=WGS --ref=/data/ref.fa --reads=/data/$bam --output_vcf=/data/${s}.vcf.gz --output_gvcf=/data/${s}.g.vcf.gz --num_shards=16; done && docker run -v "${PWD}:/data" quay.io/mlin/glnexus:v1.4.1 /usr/local/bin/glnexus_cli --config DeepVariantWGS /data/*.g.vcf.gz | bcftools view - -Oz -o cohort.vcf.gz`
**Explanation:** Each sample is called independently with `--output_gvcf`; `glnexus_cli --config DeepVariantWGS` merges gVCFs into a cohort VCF using the DeepVariant-tuned merging rules; `bcftools view - -Oz` compresses the streamed output. Use `DeepVariantWES` config for exome cohorts.

### GPU-accelerated calling via NVIDIA Parabricks
**Args:** `docker run --rm --gpus all -v "${PWD}:/workdir" -v "${PWD}/out:/outputdir" nvcr.io/nvidia/clara/clara-parabricks:4.6.0-1 pbrun deepvariant --ref /workdir/ref.fa --in-bam /workdir/sample.bam --out-variants /outputdir/sample.vcf.gz --mode shortread --num-gpus 1`
**Explanation:** `pbrun deepvariant` is the Parabricks CUDA port of DeepVariant (output is bit-identical to Google's); `--mode shortread` selects the Illumina model (alternatives: `PacBio`, `ONT`); `--num-gpus 1` pins one GPU. A 30× WGS completes in ~8 min on an A100 vs ~5 h on 96-core CPU.

### Filter output VCF by quality for downstream analysis
**Args:** `bcftools view -i 'QUAL>20 && FMT/GQ>20' sample.vcf.gz -Oz -o filtered.vcf.gz && bcftools stats filtered.vcf.gz | grep TSTV`
**Explanation:** DeepVariant emits QUAL (site-level) and GQ (genotype-level) scores; `QUAL>20 && FMT/GQ>20` is a typical high-confidence filter; `bcftools stats | grep TSTV` reports the Ti/Tv ratio (~2.0–2.1 expected for WGS, ~3.0 for WES) as a sanity check.

### Benchmark against a GIAB truth set with hap.py
**Args:** `docker run -v "${PWD}:/data" jmcdani20/hap.py:latest /opt/hap.py/bin/hap.py /data/HG002_truth.vcf.gz /data/deepvariant.vcf.gz -r /data/hg38.fa -o /data/benchmark --threads 16 -f /data/HG002_confident.bed`
**Explanation:** `hap.py` compares the DeepVariant calls against the Genome in a Bottle (GIAB) HG002 truth set; `-f /data/HG002_confident.bed` restricts comparison to high-confidence regions; output includes SNP/indel recall, precision, and F1 metrics. Typical DeepVariant WGS F1: SNP >99.9%, indel >99.7%.
