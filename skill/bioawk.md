---
name: bioawk
category: utility
description: "Bioawk (by Heng Li) is an extension of BWK awk that auto-parses common bioinformatics formats (FASTA/FASTQ, BED, GFF, SAM, VCF) and provides built-in functions for sequence manipulation (length, gc, reverse, revcomp, trimq)."
tags: [bioawk, awk, text-processing, fastq, fasta, bed, gff, sam, vcf, bioinformatics, sequence, streaming]
author: oxo-call-community
source_url: "https://github.com/lh3/bioawk"
---

## Concepts

- **Tool Overview**: bioawk (by Heng Li, https://github.com/lh3/bioawk) is an extension of BWK awk that adds built-in parsing for common bioinformatics file formats and biological sequence-manipulation functions. It uses the same `awk` syntax (`'pattern { action }' file`), so all standard awk constructs (BEGIN/END, NF, NR, arrays, printf, getline) work as expected.
- **Core Function**: Reads bioinformatics files (FASTA, FASTQ, BED, GFF, SAM, VCF, or any tabular format with a header) and automatically splits each record into named fields accessible via `$<fieldname>` (e.g., `$seq`, `$chrom`, `$start`). Eliminates the need for ad-hoc parsers.
- **Input/Output**: Auto-detects and reads gzip-compressed files when given a `.gz` path. Output is plain text by default; use `-v OFS='\t'` or `-t` for tab-separated output. Streams records one at a time, so memory usage is independent of file size.
- **Format Auto-parsing via `-c fmt`**: The `-c` option selects the parser. Available formats and their fields:
  - **fastx** (FASTA or FASTQ): `$name`, `$seq`, `$qual`, `$comment`. Auto-detects FASTA vs FASTQ.
  - **bed**: `$chrom`, `$start`, `$end`, `$name`, `$score`, `$strand`, `$thickstart`, `$thickend`, `$rgb`, `$blockcount`, `$blocksizes`, `$blockstarts`.
  - **sam**: `$qname`, `$flag`, `$rname`, `$pos`, `$mapq`, `$cigar`, `$rnext`, `$pnext`, `$tlen`, `$seq`, `$qual`.
  - **vcf**: `$chrom`, `$pos`, `$id`, `$ref`, `$alt`, `$qual`, `$filter`, `$info`.
  - **gff**: `$seqname`, `$source`, `$feature`, `$start`, `$end`, `$score`, `$filter`, `$strand`, `$group`, `$attribute`.
  - **header**: Uses the first line's column names as field variables (spaces/special chars converted to `_`), enabling arbitrary TSV/CSV processing.
- **Built-in Biological Functions**:
  - `length($seq)`: sequence length (works on any string).
  - `gc($seq)`: GC fraction (0–1) of a nucleotide sequence.
  - `reverse($seq)`: reverse the string.
  - `revcomp($seq)`: reverse complement (DNA).
  - `trimq($qual, $seq)`: quality-trim a read (returns trimmed length).
  - Bitwise: `and()`, `or()`, `xor()` (useful for SAM FLAG decoding).
- **Standard awk still applies**: All awk built-ins (`substr`, `split`, `gsub`, `printf`, `BEGIN`, `END`, `NR`, `NF`, arrays, `getline`) work. bioawk only extends, never restricts.
- **Installation**: `conda install -c bioconda bioawk` (preferred); or build from source: `git clone https://github.com/lh3/bioawk && cd bioawk && make`. On macOS: `brew install bioawk`.

## Pitfalls

- **Field semantics differ per format**: `$name` is the FASTA header in `fastx`, but `$name` is column 4 (feature name) in `bed`, and there is no `$name` in `sam` (it's `$qname`). Always pick the field name matching your `-c fmt`. The fields table in Concepts lists every format's variables.
- **`-c fastx` unifies FASTA/FASTQ**: For FASTA, `$qual` is empty; for FASTQ, `$comment` is often empty. Code that assumes a specific format may silently produce empty output. Use `length($qual)>0` to detect FASTQ.
- **SAM `$flag` is an integer bitmask**: To filter mapped reads, use bitwise AND: `$flag and 4 == 0` (not `$flag == 0`). Common bits: 4=unmapped, 16=reverse strand, 256=secondary, 2048=supplementary.
- **VCF `$alt` may contain commas**: Multi-allelic sites have `$alt = "A,T"`. Use `split($alt, a, ",")` to enumerate alternatives; do not assume a single character.
- **BED coordinates are 0-based, half-open**: `$start` is 0-based, `$end` is exclusive. Subtracting `$end - $start` gives the feature length, but conversion to 1-based GFF/VCF coordinates requires `$start+1`.
- **GFF `$attribute` is one field**: The 9th GFF column is the entire `key=value;key=value` string, not split. Use `gsub`/`split` on `;` and `=` inside the awk program if you need individual attributes.
- **`-c header` requires a header row**: If the file has no header, bioawk fails or treats data as field names. For headerless TSV, use plain `-F'\t'` and `$1`, `$2`, ... instead.
- **`-H` only preserves headers, not comments**: `-H` reprints the first (header) line of SAM/VCF files in the output. Comment lines (`##`) in VCF/BAM headers are not auto-skipped; filter them with `!/^#/`.
- **No native BAM/CRAM support**: bioawk reads text SAM only. Pipe through `samtools view -h file.bam | bioawk -c sam ...` for BAM input. The `sam` parser also accepts the SAM header lines as records — guard with `!/^@/`.
- **`gc()` returns a fraction, not a percentage**: `gc($seq)` returns e.g., 0.5 for 50% GC. Multiply by 100 in `printf` if you want a percentage.
- **Single-quoted awk programs on the command line**: `'pattern { action }'` must be single-quoted to protect `$` and `{}` from the shell. If you need a shell variable inside, escape with `'"$VAR"'` or use `-v var="$VAR"`.
- **Not a replacement for specialized tools**: bioawk is great for ad-hoc one-liners, but for production pipelines prefer `samtools`/`bcftools`/`bedtools`/`seqkit` — they are faster, validated, and handle edge cases bioawk does not.

## Examples

### Count sequences in a FASTA/FASTQ file
**Args:** `-c fastx 'END{print NR}' reads.fa.gz`
**Explanation:** `-c fastx` selects the unified FASTA/FASTQ parser (auto-detected from content); `NR` is the standard awk record counter, incremented once per sequence; `END` prints the final count after the last record. gzip is auto-decompressed.

### Print sequence name, length, and GC fraction as TSV
**Args:** `-t -c fastx '{print $name, length($seq), gc($seq)}' assembly.fa`
**Explanation:** `-t` sets both input and output field separators to tab (equivalent to `-F'\t' -v OFS='\t'`); `length($seq)` and `gc($seq)` are bioawk built-ins; output is tab-separated for easy piping to `cut`/`sort`/`awk`/R. Multiply by 100 in printf if a percentage is required.

### Reverse-complement every sequence (FASTA in, FASTA out)
**Args:** `-c fastx '{print ">"$name; print revcomp($seq)}' input.fa`
**Explanation:** `revcomp()` is a bioawk built-in returning the reverse complement; `print ">"$name` reconstructs the FASTA header. Note the two `print` statements produce a header line and a sequence line per record, yielding a valid FASTA file. Use `$comment`/`$qual` if round-tripping FASTQ.

### Filter FASTA sequences longer than 1 kb
**Args:** `-c fastx 'length($seq)>1000{print ">"$name"\n"$seq}' input.fa`
**Explanation:** The pattern `length($seq)>1000` is evaluated per record; only matching records trigger the action block. The action prints header and sequence lines. This is equivalent to `seqkit seq -m 1000` but bioawk needs no extra tool.

### Convert FASTQ to FASTA (drop quality)
**Args:** `-c fastx '{print ">"$name; print $seq}' reads.fq.gz > reads.fa`
**Explanation:** `-c fastx` parses FASTQ into `$name`, `$seq`, `$qual`; the action only prints the first two, discarding `$qual`. The `.fq.gz` input is auto-decompressed; stdout is redirected to `reads.fa`. Equivalent to `seqkit fq2fa` or `awk` but with cleaner field names.

### Extract sequences by ID list
**Args:** `-c fastx 'BEGIN{while((getline k <"ids.txt")>0) i[k]=1} i[$name]{print ">"$name"\n"$seq}' assembly.fa`
**Explanation:** `BEGIN` block loads IDs from `ids.txt` into associative array `i` (keyed by ID); per record, the pattern `i[$name]` is true (1) only if the ID is in the set. `getline k <"file"` is a standard awk idiom. For very large FASTA, prefer `seqkit grep -f ids.txt` (faster, indexed).

### Calculate mean MAPQ from a BAM file
**Args:** `samtools view -h aln.bam | bioawk -c sam -H '!/^@/{s+=$mapq; n++} END{print s/n}'`
**Explanation:** `samtools view -h` streams SAM (with `@SQ`/`@PG` header lines) to bioawk; `-c sam` parses fields including `$mapq`; `-H` reprints the header; `!/^@/` skips header lines from accumulation; `s+=$mapq` accumulates the sum, `n++` counts reads, `END` prints the mean. Dividing by `n` after END gives the average MAPQ.

### Count reads mapped to each reference (BAM input)
**Args:** `samtools view aln.bam | bioawk -c sam '{c[$rname]++} END{for (r in c) print r, c[r]}'`
**Explanation:** `samtools view` (without `-h`) streams alignment records only (no header); `-c sam` exposes `$rname` (reference name); associative array `c` counts per reference; `END` iterates with `for (r in c)`. Output is reference name and read count, sorted by `sort -k2,2 -nr` for ranking.

### Filter SAM for primary mapped forward reads
**Args:** `bioawk -c sam '!/^@/ && $flag and 4 == 0 && $flag and 16 == 0 {print}' aln.sam`
**Explanation:** `!/^@/` skips header lines; `$flag and 4 == 0` checks bit 4 (unmapped) is unset → mapped; `$flag and 16 == 0` checks bit 16 (reverse strand) is unset → forward; `and` is bioawk's bitwise-AND function. `{print}` outputs the full SAM record unchanged. Add `-H` to preserve header in output.

### Sum feature lengths from a BED file
**Args:** `-c bed '{s += $end - $start} END{print s}' regions.bed`
**Explanation:** `-c bed` parses BED columns into `$chrom`, `$start`, `$end`, etc.; `$end - $start` is the feature length (BED is 0-based, half-open); `s` accumulates the total; `END` prints the total covered bases. Use `awk` if you also need to merge overlapping intervals first (bioawk does not merge).

### Extract CDS features from a GFF and print gene ID
**Args:** `-c gff '$feature=="CDS"{print $seqname, $start, $end, $strand, $attribute}' genes.gff`
**Explanation:** `-c gff` parses GFF columns including `$feature` (3rd column, e.g., gene/mRNA/CDS/exon); the pattern `$feature=="CDS"` selects only CDS records; `$attribute` is the entire 9th column (`ID=...;Parent=...`). Use `match($attribute, /ID=([^;]+)/, m)` (gawk extension) or `split` on `;` and `=` to extract specific attributes.

### Compute per-chromosome read counts from VCF
**Args:** `-c vcf '!/^#/ {c[$chrom]++} END{for (k in c) print k, c[k]}' variants.vcf`
**Explanation:** `!/^#/` skips both `##` header lines and the single `#CHROM` header line; `$chrom` is parsed from column 1; associative array `c` counts variants per chromosome; `END` prints chromosome and count. Equivalent to `bcftools query -f '%CHROM\n' | sort | uniq -c` but in a single pass.

### Use `-c header` for arbitrary TSV with column names
**Args:** `-c header '$expression > 10 {print $gene_id, $expression}' counts.tsv`
**Explanation:** `-c header` reads the first line of `counts.tsv` as column names (e.g., `gene_id`, `expression`, ...) and exposes them as `$gene_id`, `$expression`. Spaces/special characters in column names are converted to `_`. This is the most flexible mode for arbitrary tables without memorizing column indices.
