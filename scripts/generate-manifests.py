"""
generate-manifests.py
Called by /vault-install Phase 4.
Generates VAULT-MANIFEST.md — a living index of all vault contents.

Usage:
    python3 generate-manifests.py --vault-path ./vault
"""

import os
import argparse
from datetime import date

def list_notes(folder):
    notes = []
    if not os.path.exists(folder):
        return notes
    for f in sorted(os.listdir(folder)):
        if f.endswith('.md') and not f.startswith('_'):
            notes.append(f.replace('.md', ''))
    return notes

def list_projects(vault_path):
    projects_dir = os.path.join(vault_path, '01_Projects')
    if not os.path.exists(projects_dir):
        return []
    return [d for d in sorted(os.listdir(projects_dir))
            if os.path.isdir(os.path.join(projects_dir, d)) and not d.startswith('_')]

def list_areas(vault_path):
    areas_dir = os.path.join(vault_path, '02_Areas')
    if not os.path.exists(areas_dir):
        return []
    return [d for d in sorted(os.listdir(areas_dir))
            if os.path.isdir(os.path.join(areas_dir, d)) and not d.startswith('_')]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vault-path', default='./vault')
    args = parser.parse_args()

    vault = args.vault_path
    projects = list_projects(vault)
    areas = list_areas(vault)

    lines = [
        f"# VAULT-MANIFEST",
        f"",
        f"Generated: {date.today()}",
        f"",
        f"---",
        f"",
        f"## Projects ({len(projects)})",
        f"",
    ]
    for p in projects:
        lines.append(f"- [[01_Projects/{p}/{p}|{p}]]")

    lines += [
        f"",
        f"## Areas ({len(areas)})",
        f"",
    ]
    for a in areas:
        lines.append(f"- [[02_Areas/{a}/{a}|{a}]]")

    lines += [
        f"",
        f"## Knowledge Base",
        f"",
        f"- [[03_Knowledge/Insights/|Insights]]",
        f"- [[03_Knowledge/Soluciones/|Soluciones]]",
        f"- [[03_Knowledge/Decisiones/|Decisiones]]",
        f"- [[03_Knowledge/Conceptos/|Conceptos]]",
        f"",
        f"## Reports",
        f"",
        f"- [[05_Monthly/|Monthly Synthesis Reports]]",
        f"",
    ]

    manifest_path = os.path.join(vault, 'VAULT-MANIFEST.md')
    with open(manifest_path, 'w') as f:
        f.write('\n'.join(lines))

    print(f"✓ VAULT-MANIFEST.md generated at {manifest_path}")

if __name__ == '__main__':
    main()
