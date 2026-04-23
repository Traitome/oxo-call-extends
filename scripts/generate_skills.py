#!/usr/bin/env python3
"""
Generate oxo-call skill files for all bioconda CLI tools.

This script reads bioconda_tools_metadata.jsonl and bioconda_tools_docs.txt,
then generates a skill.md file for each tool following the oxo-call skill format.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional


def parse_docs_file(docs_path: str) -> Dict[str, Dict]:
    """Parse bioconda_tools_docs.txt into a dictionary keyed by tool name."""
    docs = {}
    current_tool = None
    current_content = []
    
    with open(docs_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            
            # Detect tool header
            if line.startswith('TOOL: '):
                # Save previous tool
                if current_tool and current_content:
                    docs[current_tool] = parse_tool_content(current_content)
                
                # Start new tool
                current_tool = line.split('TOOL: ', 1)[1].strip()
                current_content = []
            elif current_tool:
                current_content.append(line)
        
        # Save last tool
        if current_tool and current_content:
            docs[current_tool] = parse_tool_content(current_content)
    
    return docs


def parse_tool_content(lines: List[str]) -> Dict:
    """Parse the content of a single tool entry from docs file."""
    content = {
        'version': '',
        'summary': '',
        'description': '',
        'bioconda_page': '',
        'homepage': '',
        'documentation': '',
        'development': '',
        'source': '',
        'license': '',
        'platforms': '',
        'installation': ''
    }
    
    section = None
    description_lines = []
    
    for line in lines:
        if line.startswith('Version: '):
            content['version'] = line.split('Version: ', 1)[1].strip()
        elif line.startswith('Summary: '):
            content['summary'] = line.split('Summary: ', 1)[1].strip()
        elif line.startswith('Description:'):
            section = 'description'
        elif line.startswith('Bioconda page: '):
            content['bioconda_page'] = line.split('Bioconda page: ', 1)[1].strip()
            section = None
        elif line.startswith('Homepage: '):
            content['homepage'] = line.split('Homepage: ', 1)[1].strip()
        elif line.startswith('Documentation: '):
            content['documentation'] = line.split('Documentation: ', 1)[1].strip()
        elif line.startswith('Development: '):
            content['development'] = line.split('Development: ', 1)[1].strip()
        elif line.startswith('Source: '):
            content['source'] = line.split('Source: ', 1)[1].strip()
        elif line.startswith('License: '):
            content['license'] = line.split('License: ', 1)[1].strip()
        elif line.startswith('Platforms: '):
            content['platforms'] = line.split('Platforms: ', 1)[1].strip()
        elif line.startswith('Installation:'):
            section = 'installation'
        elif section == 'description' and line.startswith('    '):
            description_lines.append(line.strip())
        elif section == 'installation' and line.startswith('  '):
            content['installation'] = line.strip()
        elif line.startswith('==='):
            section = None
    
    if description_lines:
        content['description'] = ' '.join(description_lines)
    
    return content


def infer_category(tool_name: str, summary: str, description: str) -> str:
    """Infer tool category from name and description."""
    text = f"{tool_name} {summary} {description}".lower()
    
    # Category inference based on keywords
    if any(kw in text for kw in ['align', 'map', 'bwa', 'bowtie', 'minimap', 'star ']):
        return 'alignment'
    elif any(kw in text for kw in ['variant', 'snp', 'indel', 'vcf', 'genotype', 'gatk', 'bcftools']):
        return 'variant-calling'
    elif any(kw in text for kw in ['expression', 'rna-seq', 'transcript', 'quantif', 'kallisto', 'salmon']):
        return 'expression'
    elif any(kw in text for kw in ['assembly', 'assemble', 'contig', 'scaffold', 'spades', 'megahit']):
        return 'assembly'
    elif any(kw in text for kw in ['annot', 'gene predict', 'prokka', 'augustus']):
        return 'annotation'
    elif any(kw in text for kw in ['qc', 'quality', 'trim', 'filter', 'fastp', 'fastqc']):
        return 'qc'
    elif any(kw in text for kw in ['metagenom', 'binning', 'metabat', 'maxbin']):
        return 'metagenomics'
    elif any(kw in text for kw in ['epigenom', 'methylation', 'chip-seq', 'atac', 'bisulfite']):
        return 'epigenomics'
    elif any(kw in text for kw in ['population', 'admixture', 'plink', 'vcftools']):
        return 'population-genomics'
    elif any(kw in text for kw in ['crispr', 'genome edit']):
        return 'genome-editing'
    elif any(kw in text for kw in ['format', 'convert', 'samtools', 'bedtools', 'bcftools']):
        return 'formatting'
    elif any(kw in text for kw in ['python', 'r package', 'perl', 'library']):
        return 'programming'
    elif any(kw in text for kw in ['docker', 'singularity', 'container']):
        return 'containerization'
    elif any(kw in text for kw in ['slurm', 'sge', 'pbs', 'hpc', 'cluster']):
        return 'hpc'
    else:
        return 'utility'


def generate_tags(tool_name: str, summary: str, category: str) -> List[str]:
    """Generate relevant tags for the tool."""
    tags = [tool_name, category]
    
    # Add file format tags
    summary_lower = summary.lower()
    if 'bam' in summary_lower or 'sam' in summary_lower:
        tags.append('bam')
    if 'fastq' in summary_lower or 'fasta' in summary_lower:
        tags.append('fastq')
    if 'vcf' in summary_lower:
        tags.append('vcf')
    if 'gff' in summary_lower or 'gtf' in summary_lower:
        tags.append('gff')
    if 'bed' in summary_lower:
        tags.append('bed')
    
    # Add domain tags
    if 'rna' in summary_lower:
        tags.append('rna')
    if 'dna' in summary_lower:
        tags.append('dna')
    if 'protein' in summary_lower or 'peptide' in summary_lower:
        tags.append('protein')
    if 'genome' in summary_lower:
        tags.append('genome')
    if 'transcriptome' in summary_lower:
        tags.append('transcriptome')
    
    return list(set(tags))


def generate_skill_content(tool_name: str, metadata: Dict, doc_info: Dict) -> str:
    """Generate skill.md content for a tool."""
    
    # Use doc_info if available, otherwise fall back to metadata
    summary = doc_info.get('summary') or metadata.get('summary', '')
    description = doc_info.get('description') or metadata.get('description', '')
    version = doc_info.get('version') or metadata.get('version', '')
    homepage = doc_info.get('homepage') or metadata.get('home', '')
    doc_url = doc_info.get('documentation') or metadata.get('doc_url', '')
    dev_url = doc_info.get('development') or metadata.get('dev_url', '')
    license_info = doc_info.get('license') or metadata.get('license', '')
    
    # Infer category
    category = infer_category(tool_name, summary, description)
    
    # Generate tags
    tags = generate_tags(tool_name, summary, category)
    
    # Determine best source_url
    source_url = doc_url or homepage or dev_url or f"https://bioconda.github.io/recipes/{tool_name}/README.html"
    
    # Build skill content
    content = f"""---
name: {tool_name}
category: {category}
description: {summary}
tags: {json.dumps(tags)}
author: oxo-call-community
source_url: "{source_url}"
---

## Concepts

"""
    
    # Add basic concepts based on category and summary
    concepts = []
    
    # Basic tool description
    if description:
        concepts.append(f"- **Tool Overview**: {description}")
    else:
        concepts.append(f"- **Tool Overview**: {summary}")
    
    # Category-specific concepts
    if category == 'alignment':
        concepts.append("- **Alignment Workflow**: Input FASTQ → Alignment → Output BAM/SAM")
        concepts.append("- **Indexing**: Reference genome must be indexed before alignment")
    elif category == 'variant-calling':
        concepts.append("- **Variant Calling Workflow**: Input BAM → Variant Detection → Output VCF")
        concepts.append("- **Reference Required**: Requires indexed reference genome")
    elif category == 'qc':
        concepts.append("- **Quality Control**: Assesses and filters sequencing data quality")
        concepts.append("- **Input/Output**: Processes FASTQ/BAM files and generates quality reports")
    elif category == 'assembly':
        concepts.append("- **Assembly Workflow**: Input reads → Assembly → Output contigs/scaffolds")
        concepts.append("- **Coverage Considerations**: Assembly quality depends on sequencing depth")
    elif category == 'expression':
        concepts.append("- **Quantification Workflow**: Input reads → Quantification → Expression matrix")
        concepts.append("- **Normalization**: Results may require normalization for cross-sample comparison")
    
    # Installation concept
    concepts.append(f"- **Installation**: Install via bioconda: `conda install -c bioconda {tool_name}`")
    
    # Platform support
    if doc_info.get('platforms'):
        platforms = doc_info['platforms']
        if 'Platform-independent' in platforms:
            concepts.append("- **Platform Support**: Cross-platform (Linux, macOS)")
        elif 'Linux' in platforms and 'macOS' in platforms:
            concepts.append("- **Platform Support**: Linux and macOS")
        elif 'Linux' in platforms:
            concepts.append("- **Platform Support**: Linux only")
    
    content += '\n'.join(concepts) + '\n\n'
    
    # Add pitfalls section
    content += """## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Input Format**: Ensure input files are in the correct format and properly indexed if required.
- **Resource Requirements**: Some operations may require significant memory or CPU. Monitor resource usage for large datasets.
- **Output Directory**: Ensure output directories exist before running the tool.
- **Threading**: Use appropriate thread counts based on available CPU cores.

"""
    
    # Add examples section
    content += """## Examples

"""
    
    # Generate basic examples based on category
    examples = []
    
    # Example 1: Basic help
    examples.append(f"""### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options, flags, and usage information. Use this to discover available subcommands and parameters.

""")
    
    # Example 2: Version check
    examples.append(f"""### Check installed version
**Args:** `--version`
**Explanation:** Displays the installed version number. Important for reproducibility and troubleshooting version-specific issues.

""")
    
    # Category-specific examples
    if category == 'alignment':
        examples.append(f"""### Basic alignment example
**Args:** `-t 8 -R {tool_name}_output input.fastq`
**Explanation:** Aligns input reads using 8 threads. Output is written to the specified prefix. Adjust thread count based on available CPU cores.

""")
    elif category == 'qc':
        examples.append(f"""### Quality control on input files
**Args:** `-i input.fastq -o qc_output.html`
**Explanation:** Performs quality assessment on input FASTQ file and generates an HTML report with quality metrics and visualizations.

""")
    elif category == 'variant-calling':
        examples.append(f"""### Variant calling from aligned reads
**Args:** `-f reference.fa -i aligned.bam -o variants.vcf`
**Explanation:** Calls variants from aligned BAM file using the provided reference genome. Output is in VCF format.

""")
    elif category == 'assembly':
        examples.append(f"""### De novo assembly
**Args:** `-t 16 -o assembly_output reads_1.fastq reads_2.fastq`
**Explanation:** Assembles paired-end reads into contigs using 16 threads. Output directory contains assembly files and statistics.

""")
    else:
        examples.append(f"""### Basic usage with input file
**Args:** `input_file output_file`
**Explanation:** Processes the input file and writes results to the output file. This is the most common usage pattern.

""")
    
    # Advanced example
    examples.append(f"""### Advanced usage with multiple options
**Args:** `-t 12 --verbose --output-dir results/ input1.fastq input2.fastq`
**Explanation:** Uses 12 threads for parallel processing, enables verbose logging for debugging, and writes output to a dedicated results directory. Multiple input files are processed sequentially or in parallel depending on tool design.

""")
    
    content += ''.join(examples)
    
    return content


def main():
    """Main entry point."""
    # Paths
    base_dir = Path(__file__).parent.parent
    metadata_path = base_dir / 'data' / 'bioconda_tools_metadata.jsonl'
    docs_path = base_dir / 'data' / 'bioconda_tools_docs.txt'
    output_dir = base_dir / 'skill'
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    print(f"Reading metadata from {metadata_path}")
    print(f"Reading docs from {docs_path}")
    print(f"Output directory: {output_dir}")
    
    # Parse docs file
    print("Parsing documentation file...")
    docs = parse_docs_file(str(docs_path))
    print(f"  Found {len(docs)} tools in docs file")
    
    # Process metadata
    print("Processing metadata and generating skills...")
    count = 0
    errors = 0
    
    with open(metadata_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                metadata = json.loads(line.strip())
                tool_name = metadata['name']
                
                # Get doc info if available
                doc_info = docs.get(tool_name, {})
                
                # Generate skill content
                skill_content = generate_skill_content(tool_name, metadata, doc_info)
                
                # Write skill file
                skill_file = output_dir / f"{tool_name}.md"
                with open(skill_file, 'w', encoding='utf-8') as sf:
                    sf.write(skill_content)
                
                count += 1
                if count % 500 == 0:
                    print(f"  Generated {count} skills...")
                    
            except Exception as e:
                errors += 1
                print(f"  Error processing line {line_num}: {e}")
    
    print(f"\nGeneration complete!")
    print(f"  Total skills generated: {count}")
    print(f"  Errors: {errors}")
    print(f"  Output directory: {output_dir}")


if __name__ == '__main__':
    main()
