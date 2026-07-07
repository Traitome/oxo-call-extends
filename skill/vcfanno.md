---
name: vcfanno
category: bioinformatics
description: vcfanno - fast VCF annotation with INFO fields from multiple VCF/BED/BAM sources using a TOML config and embedded Lua scripting.
tags: [vcfanno, vcf-annotation, toml, lua, bioinformatics, genomics, annotation]
author: oxo-call-community
source_url: "https://github.com/brentp/vcfanno"
---

## Concepts

- **Tool Overview**: vcfanno (v0.3.x) is a Go-based tool that annotates a query VCF with INFO fields pulled from any number of VCF, BED, or BAM files. It uses a simple TOML configuration file (`.toml`) and supports custom Lua scripts for reduction operations. Benchmarks: >8,000 variants/sec with 34 annotations from 9 files on a laptop; >30,000 variants/sec with 12 processes on a server.
- **Configuration Format**: TOML (not YAML). Each annotation source is a `[[annotation]]` block with fields: `file`, `fields` (VCF INFO names) or `columns` (1-based BED columns), `names` (output INFO names), `ops` (reduction operations). The config path is a positional argument; there is **no `-config` flag**.
- **Invocation**: `vcfanno [-lua custom.lua] [-p N] [-ends] [-permissive-overlap] conf.toml input.vcf.gz > annotated.vcf`. Input VCF must be bgzipped and tabix-indexed. Annotation files may be local paths or HTTP/HTTPS URLs.
- **Field Extraction**:
  - From VCF: values are pulled from the INFO field by name; special-cased `ID` and `FILTER` pull from the corresponding VCF columns.
  - From BED: values are pulled from 1-based column number.
  - From BAM: supported fields are `depth` (count), `mapq` (mean), `seq` (concat), `DP2`, `coverage`.
- **Reduction Operations** (`ops`): determine how multiple overlapping annotation values are merged. Valid values: `self` (default for VCF — handles multi-allelics), `concat`, `count`, `div2`, `first`, `flag`, `max`, `mean`, `min`, `sum`, `uniq`, `by_alt` (Number=A), `lua:$function`.
- **Typecasting**: `ops` of `mean`/`max`/`sum`/`div2`/`min` produce `Float` by default; `self` inherits the type from the annotation VCF; others produce `String`. Append `_int` or `_float` to the `names` entry to force a type (the suffix is stripped from the output field name).
- **PostAnnotation**: `[[postannotation]]` blocks run after all annotations are applied, allowing derived fields. Fields from the query VCF (including newly added annotations) are available to the `op`. Useful for computing allele frequency from AC/AN, or combining multiple annotation sources.
- **Lua Scripting**: custom reduction functions can be defined inline (`op="lua:function sum(t) ... end"`) or in an external `.lua` file loaded via `-lua custom.lua`. Available variables in Lua: `vals`, `chrom`, `start`, `stop`, `ref`, `alt` (table of alternate alleles).
- **Multi-Allelic Handling**: with `op="self"`, vcfanno correctly aligns annotation values to the query's ALT alleles (including allele reordering and `.` for missing values). This is the recommended op for VCF annotation.
- **Input/Output**: Input VCF must be bgzipped (`.vcf.gz`) with `.tbi` index. Output is streamed to stdout (bgzip + tabix if needed).
- **Installation**: static binary from GitHub releases (no dependencies) or `conda install -c bioconda vcfanno`.
- **Use Case**: Adding population allele frequencies (gnomAD, ExAC); annotating with ClinVar significance; adding conservation scores (fitCons, phyloP) from BED; computing derived fields (AF from AC/AN); SV/CNV end annotation.

## Pitfalls

- **The config file is TOML, not YAML**. vcfanno uses `[[annotation]]` blocks (TOML table arrays), not YAML mappings. Using YAML syntax silently fails to parse.
- **There is no `-config` flag**. The config path is a positional argument: `vcfanno conf.toml input.vcf.gz`. Using `vcfanno -config conf.toml ...` errors out.
- **Input VCF must be bgzipped and tabix-indexed**. Plain `.vcf` (uncompressed) or gzip-only (`.vcf.gz` without `.tbi`) causes errors. Use `bgzip` + `tabix -p vcf` (or `bcftools view -Oz` + `bcftools index -t`).
- **Annotation files must also be indexed**. VCF/BED annotation files need `.tbi`/`.csi`. BAM files need `.bai`. HTTP/HTTPS URLs work but require the server to support range requests.
- **Use `op="self"` for VCF annotation**. Other ops (e.g. `first`, `concat`) do not handle multi-allelic alignment and can produce incorrect allele-to-value mapping. `self` is the only op that correctly maps annotation values to the query's ALT alleles.
- **`names` and `ops` must match `fields`/`columns` length**. A mismatch silently skips the extra entries without warning. Always double-check array lengths in the TOML.
- **BED columns are 1-based**. The first 3 columns (chrom, start, end) are not counted; column 4 is the first data column. Off-by-one errors here are common.
- **`-ends` is for large variants (SVs/CNVs)**. It annotates the leftmost and rightmost single bases separately (`left_*`, `right_*` prefixes). For SNPs/short indels, it adds no value and increases runtime.
- **`-permissive-overlap` relaxes allele matching**. By default, vcfanno requires same position + REF + at least one shared ALT. With this flag, only overlap is tested — useful for annotating with BED files but can produce wrong results for VCF-vs-VCF annotation where alleles differ.
- **Type suffixes (`_int`, `_float`) are stripped from output**. If you name a field `gnomad_af_float`, the output VCF header has `gnomad_af` of type Float. Do not rely on the suffixed name downstream.
- **Lua functions need `vals` not the raw field name**. In a custom op, the table `vals` contains the annotation values; accessing a field by name (e.g. `AC`) requires using the `postannotation` block, not the `annotation` op.
- **`[[postannotation]]` can delete fields**. Using `op="delete"` in a postannotation block removes the field from the query VCF's INFO — useful for stripping intermediate fields, but irreversible.
- **Memory scales with annotation file count, not VCF size**. Each annotation file is loaded into memory-mapped intervals; annotating with 20 large VCFs can consume >32 GB RAM. Split annotations across runs if memory-bound.

## Examples

### Basic VCF annotation with a TOML config
**Args:** `vcfanno conf.toml input.vcf.gz > annotated.vcf`
**Explanation:** `conf.toml` is the positional config argument (no `-config` flag); `input.vcf.gz` must be bgzipped + tabix-indexed; output is streamed to stdout. The TOML config defines `[[annotation]]` blocks specifying `file`, `fields`, `names`, `ops`.

### Annotate with ExAC allele frequencies (VCF source)
**Args:** `cat > exac.toml << 'EOF'
[[annotation]]
file = "ExAC.r1.sites.vep.vcf.gz"
fields = ["AC_AFR", "AC_AMR", "AC_EAS", "ID", "FILTER"]
names = ["exac_ac_afr", "exac_ac_amr", "exac_ac_eas", "exac_id", "exac_filter"]
ops = ["self", "self", "self", "self", "self"]
EOF
vcfanno -p 4 exac.toml query.vcf.gz > annotated.vcf`
**Explanation:** The TOML block pulls 5 fields from ExAC's INFO; `names` defines the output field names; `ops=["self",...]` correctly handles multi-allelic alignment; `-p 4` uses 4 processes (scales well up to ~15 cores).

### Annotate with conservation scores (BED source)
**Args:** `cat > fitcons.toml << 'EOF'
[[annotation]]
file = "fitcons.bed"
columns = [4]
names = ["fitcons_mean"]
ops = ["mean"]
EOF
vcfanno fitcons.toml query.vcf.gz > annotated.vcf`
**Explanation:** `columns = [4]` pulls the 4th column of the BED file (1-based; columns 1-3 are chrom/start/end); `ops = ["mean"]` averages values when multiple BED intervals overlap the variant; output field is `fitcons_mean` of type Float (mean op produces Float by default).

### Add ClinVar significance and compute derived AF
**Args:** `cat > clinvar.toml << 'EOF'
[[annotation]]
file = "clinvar.vcf.gz"
fields = ["CLNSIG", "CLNDN"]
names = ["clinvar_sig", "clinvar_disease"]
ops = ["self", "self"]

[[postannotation]]
name = "AF"
fields = ["AC", "AN"]
op = "lua:AC / AN"
type = "Float"
EOF
vcfanno clinvar.toml query.vcf.gz > annotated.vcf`
**Explanation:** `[[annotation]]` pulls ClinVar significance and disease name; `[[postannotation]]` computes a derived `AF` field from existing `AC` (alternate count) and `AN` (allele number) INFO fields using an inline Lua expression; `type="Float"` sets the VCF header type.

### Custom Lua reduction function in external file
**Args:** `cat > custom.lua << 'EOF'
function sum(t)
  local s = 0
  for i=1,#t do s = s + t[i] end
  return s
end

function rms(t)
  local s = 0
  for i=1,#t do s = s + t[i]^2 end
  return math.sqrt(s / #t)
end
EOF
cat > conf.toml << 'EOF'
[[annotation]]
file = "scores.bed"
columns = [4, 5]
names = ["score_sum", "score_rms"]
ops = ["lua:sum(vals)", "lua:rms(vals)"]
EOF
vcfanno -lua custom.lua conf.toml query.vcf.gz > annotated.vcf`
**Explanation:** `-lua custom.lua` loads external Lua functions; `op="lua:sum(vals)"` calls the `sum` function with the `vals` table (overlapping annotation values); the function's return value becomes the annotation. Use this when built-in ops (mean, max, etc.) are insufficient.

### Annotate SV/CNV with both ends using `-ends`
**Args:** `cat > sv.toml << 'EOF'
[[annotation]]
file = "gnomad_sv.bed"
columns = [4]
names = ["gnomad_sv_af"]
ops = ["max"]
EOF
vcfanno -ends sv.toml query_sv.vcf.gz > annotated_sv.vcf`
**Explanation:** `-ends` annotates the leftmost and rightmost single bases of each variant separately, adding `left_gnomad_sv_af` and `right_gnomad_sv_af` fields (in addition to the region-wide `gnomad_sv_af`). Essential for SV/CNV breakpoint annotation where the region-wide value may be uninformative.

### Annotate with BAM depth
**Args:** `cat > bam.toml << 'EOF'
[[annotation]]
file = "sample.bam"
fields = ["depth", "mapq", "seq"]
names = ["bam_depth", "bam_mapq", "bam_seq"]
ops = ["count", "mean", "concat"]
EOF
vcfanno bam.toml query.vcf.gz > annotated.vcf`
**Explanation:** For BAM files, the `fields` value determines the operation: `depth` counts overlapping reads, `mapq` averages mapping quality, `seq` concatenates read bases; the `ops` array is interpreted but the actual computation is fixed per field name. Requires a `.bai` index.

### Force integer type with `_int` suffix
**Args:** `cat > typed.toml << 'EOF'
[[annotation]]
file = "counts.bed"
columns = [4]
names = ["overlap_count_int"]
ops = ["count"]
EOF
vcfanno typed.toml query.vcf.gz > annotated.vcf`
**Explanation:** Appending `_int` to the name forces the output field type to Integer in the VCF header (the suffix is stripped, so the field is named `overlap_count`); without the suffix, `count` would produce a String type. Use `_float` for Float. This is the only way to override the default type inference.

### Annotate from multiple sources in one config
**Args:** `cat > multi.toml << 'EOF'
[[annotation]]
file = "gnomad.vcf.gz"
fields = ["AF", "AC"]
names = ["gnomad_af", "gnomad_ac"]
ops = ["self", "self"]

[[annotation]]
file = "clinvar.vcf.gz"
fields = ["CLNSIG"]
names = ["clinvar_sig"]
ops = ["self"]

[[annotation]]
file = "phylop.bed"
columns = [4]
names = ["phylop"]
ops = ["max"]

[[postannotation]]
name = "ID"
fields = ["clinvar_sig", "ID"]
op = "lua:clinvar_sig .. '|' .. ID"
type = "String"
EOF
vcfanno -p 8 multi.toml query.vcf.gz > annotated.vcf`
**Explanation:** Multiple `[[annotation]]` blocks are applied in order; `-p 8` parallelises across 8 cores; the `[[postannotation]]` block prepends ClinVar significance to the existing VCF ID column (using `name="ID"` to overwrite the ID field).

### Delete intermediate fields after postannotation
**Args:** `cat > cleanup.toml << 'EOF'
[[annotation]]
file = "ac_an.vcf.gz"
fields = ["AC", "AN"]
names = ["tmp_ac", "tmp_an"]
ops = ["self", "self"]

[[postannotation]]
name = "AF"
fields = ["tmp_ac", "tmp_an"]
op = "lua:tmp_ac / tmp_an"
type = "Float"

[[postannotation]]
name = "tmp_ac"
fields = ["tmp_ac"]
op = "delete"
type = "String"

[[postannotation]]
name = "tmp_an"
fields = ["tmp_an"]
op = "delete"
type = "String"
EOF
vcfanno cleanup.toml query.vcf.gz > annotated.vcf`
**Explanation:** Pulls AC/AN from an annotation VCF into temporary fields, computes AF in a postannotation block, then deletes the temporary fields with `op="delete"` to keep the output VCF clean. The `type` for delete blocks is ignored but required by the parser.

### Use `-permissive-overlap` for BED-only annotation
**Args:** `vcfanno -permissive-overlap regions.toml query.vcf.gz > annotated.vcf`
**Explanation:** `-permissive-overlap` disables the default position + REF + ALT matching for VCF sources, falling back to pure interval overlap. Useful when annotating with BED files (where REF/ALT are irrelevant) or when annotation VCFs use different representations of the same variant. **Caution**: can produce incorrect allele-specific values for VCF-vs-VCF annotation.
