"""
create-structure.py
Called by /vault-install Phase 4.
Creates personalized vault folder structure based on user's projects and areas.

Usage:
    python3 create-structure.py --vault-path ./vault --projects "proj1,proj2" --areas "area1,area2"
"""

import os
import sys
import argparse
from datetime import date

def create_dir(path):
    os.makedirs(path, exist_ok=True)
    print(f"  ✓ {path}")

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  ✓ {path}")

def slug(name):
    return name.lower().strip().replace(' ', '-').replace('/', '-')

def create_project_hub(vault_path, project_name):
    s = slug(project_name)
    project_dir = os.path.join(vault_path, '01_Projects', s)
    create_dir(project_dir)
    hub_content = f"""---
type: project
name: {project_name}
status: active
created: {date.today()}
tags: [project]
---

# {project_name}

## Overview


## Goals


## Notes

"""
    create_file(os.path.join(project_dir, f'{s}.md'), hub_content)

def create_area_hub(vault_path, area_name):
    s = slug(area_name)
    area_dir = os.path.join(vault_path, '02_Areas', s)
    create_dir(area_dir)
    hub_content = f"""---
type: area
name: {area_name}
created: {date.today()}
tags: [area]
---

# {area_name}

## Purpose


## Notes

"""
    create_file(os.path.join(area_dir, f'{s}.md'), hub_content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vault-path', default='./vault')
    parser.add_argument('--projects', default='')
    parser.add_argument('--areas', default='')
    args = parser.parse_args()

    vault = args.vault_path
    projects = [p.strip() for p in args.projects.split(',') if p.strip()]
    areas = [a.strip() for a in args.areas.split(',') if a.strip()]

    print("\n🗂  Creating vault structure...\n")

    # Base folders
    for folder in ['01_Projects', '02_Areas', '03_Knowledge/Insights',
                   '03_Knowledge/Soluciones', '03_Knowledge/Decisiones',
                   '03_Knowledge/Conceptos', '04_Daily', '05_Monthly', '_templates']:
        create_dir(os.path.join(vault, folder))

    # Claude_Improves project (always created)
    create_dir(os.path.join(vault, '01_Projects', 'Claude_Improves'))

    # User's projects
    for project in projects:
        create_project_hub(vault, project)

    # User's areas
    for area in areas:
        create_area_hub(vault, area)

    print(f"\n✅ Structure created at {vault}")
    print(f"   Projects: {len(projects)} + Claude_Improves")
    print(f"   Areas: {len(areas)}")

if __name__ == '__main__':
    main()
