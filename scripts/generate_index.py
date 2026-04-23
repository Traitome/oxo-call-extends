#!/usr/bin/env python3
"""
Generate index.json from all skill files in the skill/ directory.
This script parses YAML front-matter from markdown files and creates
a JSON index for the landing page.
"""

import json
import os
import re
import glob
from pathlib import Path

def parse_frontmatter(content: str) -> dict:
    """Parse YAML front-matter from markdown content."""
    if not content.startswith('---'):
        return {}
    
    # Find the closing ---
    end_idx = content.find('\n---', 4)
    if end_idx == -1:
        return {}
    
    frontmatter_str = content[4:end_idx]
    result = {}
    
    for line in frontmatter_str.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Handle YAML lists like tags: [a, b, c]
            if value.startswith('[') and value.endswith(']'):
                value = [v.strip() for v in value[1:-1].split(',')]
            # Handle quoted strings
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            
            result[key] = value
    
    return result

def generate_index(skill_dir: str, output_path: str):
    """Generate index.json from all skill files."""
    skills = []
    
    for md_file in glob.glob(os.path.join(skill_dir, '*.md')):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter = parse_frontmatter(content)
            if not frontmatter:
                continue
            
            skill_entry = {
                'name': frontmatter.get('name', os.path.basename(md_file).replace('.md', '')),
                'category': frontmatter.get('category', 'utility'),
                'description': frontmatter.get('description', ''),
                'tags': frontmatter.get('tags', []),
                'source_url': frontmatter.get('source_url', ''),
                'file': os.path.basename(md_file)
            }
            skills.append(skill_entry)
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    # Sort by name
    skills.sort(key=lambda x: x['name'].lower())
    
    # Create index
    index = {
        'total': len(skills),
        'generated': __import__('datetime').datetime.now().isoformat(),
        'skills': skills
    }
    
    # Write output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
    
    print(f"Generated index with {len(skills)} skills")
    return index

if __name__ == '__main__':
    script_dir = Path(__file__).parent.parent
    skill_dir = script_dir / 'skill'
    output_path = skill_dir / 'index.json'
    generate_index(str(skill_dir), str(output_path))
