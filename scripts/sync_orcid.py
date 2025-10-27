#!/usr/bin/env python3
"""
Om Vinayaka 🙏

ORCID Synchronization Script
Copyright (c) 2024-2025 Prayaga Vaibhav (Woman Inventor)
All Rights Reserved

This script fetches publications and works from ORCID profile
and generates a comprehensive PUBLICATIONS.md file with proper
copyright protection.

Protected under Proprietary License - See LICENSE file
"""

import requests
import json
import os
from datetime import datetime
from collections import defaultdict

# ORCID Configuration
ORCID_ID = "0009-0007-8995-0895"
ORCID_API_URL = f"https://pub.orcid.org/v3.0/{{ORCID_ID}}/works"
HEADERS = {
    "Accept": "application/json"
}

# Output paths
DATA_DIR = "data"
PUBLICATIONS_FILE = "PUBLICATIONS.md"
JSON_OUTPUT = os.path.join(DATA_DIR, "orcid_works.json")

def create_data_directory():
    """Create data directory if it doesn't exist"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"✓ Created directory: {{DATA_DIR}}")

def fetch_orcid_works():
    """Fetch works from ORCID API"""
    print(f"📡 Fetching works from ORCID profile: {{ORCID_ID}}")
    
    try:
        response = requests.get(ORCID_API_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        print(f"✓ Successfully fetched ORCID data")
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching ORCID data: {{e}}")
        return None

def save_raw_data(data):
    """Save raw ORCID JSON data"""
    try:
        with open(JSON_OUTPUT, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved raw data to: {{JSON_OUTPUT}}")
    except Exception as e:
        print(f"❌ Error saving raw data: {{e}}")

def parse_works(data):
    """Parse and categorize works from ORCID data"""
    if not data or 'group' not in data:
        print("⚠️ No works found in ORCID data")
        return {}
    
    works_by_type = defaultdict(list)
    
    for group in data.get('group', []):
        work_summary = group.get('work-summary', [])
        if not work_summary:
            continue
            
        # Get the first work summary (primary)
        work = work_summary[0]
        
        # Extract work information
        title_data = work.get('title', {})
        title = title_data.get('title', {}).get('value', 'Untitled Work')
        
        work_type = work.get('type', 'OTHER')
        
        pub_date = work.get('publication-date')
        date_str = ''
        if pub_date:
            year = pub_date.get('year', {}).get('value', '')
            month = pub_date.get('month', {}).get('value', '')
            day = pub_date.get('day', {}).get('value', '')
            date_parts = [p for p in [year, month, day] if p]
            date_str = '-'.join(date_parts) if date_parts else ''
        
        # Extract external IDs (DOI, URLs, etc.)
        external_ids = work.get('external-ids', {}).get('external-id', [])
        doi = ''
        url = ''
        
        for ext_id in external_ids:
            id_type = ext_id.get('external-id-type', '')
            id_value = ext_id.get('external-id-value', '')
            id_url = ext_id.get('external-id-url', {}).get('value', '')
            
            if id_type.lower() == 'doi' and not doi:
                doi = id_value
            if id_url and not url:
                url = id_url
        
        # Get journal/source
        journal = work.get('journal-title', {}).get('value', '') if work.get('journal-title') else ''
        
        work_entry = {
            'title': title,
            'type': work_type,
            'date': date_str,
            'doi': doi,
            'url': url,
            'journal': journal
        }
        
        works_by_type[work_type].append(work_entry)
    
    print(f"✓ Parsed {{sum(len(works) for works in works_by_type.values())}} works")
    return works_by_type

def generate_publications_md(works_by_type):
    """Generate PUBLICATIONS.md file with all works"""
    
    content = []
    
    # Header
    content.append("# Publications and Works")
    content.append("")
    content.append("**Om Vinayaka 🙏**")
    content.append("")
    content.append("## Prayaga Vaibhav - Woman Inventor")
    content.append("")
    content.append(f"**ORCID Profile**: [https://orcid.org/{{ORCID_ID}}](https://orcid.org/{{ORCID_ID}})")
    content.append("")
    content.append("---")
    content.append("")
    content.append("### ⚖️ COPYRIGHT NOTICE")
    content.append("")
    content.append("**© 2024-2025 Prayaga Vaibhav. All Rights Reserved.**")
    content.append("")
    content.append("All works, inventions, publications, thesis, journal articles, and other intellectual")
    content.append("property listed on this page are protected under the")
    content.append("[**Proprietary License**](LICENSE) of this repository.")
    content.append("")
    content.append("**NO PART** of any work may be reproduced, distributed, transmitted, modified,")
    content.append("or otherwise used without **EXPRESS WRITTEN PERMISSION** from Prayaga Vaibhav.")
    content.append("")
    content.append("See [LICENSE](LICENSE) file for complete terms and conditions.")
    content.append("")
    content.append("---")
    content.append("")
    content.append(f"**Last Updated**: {{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}} UTC")
    content.append("")
    content.append(f"**Total Works**: {{sum(len(works) for works in works_by_type.values())}}")
    content.append("")
    content.append("---")
    content.append("")
    
    # Type mapping for better display
    type_display = {
        'JOURNAL_ARTICLE': '📄 Journal Articles',
        'CONFERENCE_PAPER': '📑 Conference Papers',
        'BOOK': '📚 Books',
        'BOOK_CHAPTER': '📖 Book Chapters',
        'DISSERTATION': '🎓 Thesis/Dissertations',
        'PATENT': '💡 Patents/Inventions',
        'PREPRINT': '📝 Preprints',
        'REPORT': '📊 Reports',
        'OTHER': '📌 Other Works',
        'INVENTION': '🔬 Inventions',
        'RESEARCH_TOOL': '🛠️ Research Tools',
        'DATA_SET': '📊 Datasets'
    }
    
    # Sort types for consistent display
    sorted_types = sorted(works_by_type.keys())
    
    for work_type in sorted_types:
        works = works_by_type[work_type]
        if not works:
            continue
        
        display_name = type_display.get(work_type, f'📌 {{work_type.replace("_", " ").title()}}')
        
        content.append(f"## {{display_name}}")
        content.append("")
        
        # Sort works by date (newest first)
        sorted_works = sorted(works, key=lambda x: x.get('date', ''), reverse=True)
        
        for idx, work in enumerate(sorted_works, 1):
            content.append(f"### {{idx}}. {{work['title']}}")
            content.append("")
            
            if work['date']:
                content.append(f"**Publication Date**: {{work['date']}}")
                content.append("")
            
            if work['journal']:
                content.append(f"**Source**: {{work['journal']}}")
                content.append("")
            
            if work['doi']:
                content.append(f"**DOI**: [{{work['doi']}}](https://doi.org/{{work['doi']}})")
                content.append("")
            elif work['url']:
                content.append(f"**URL**: [{{work['url']}}]({{work['url']}})")
                content.append("")
            
            # Copyright notice for each work
            content.append("**COPYRIGHT NOTICE**:")
            content.append("> © 2024-2025 Prayaga Vaibhav. All Rights Reserved.")
            content.append("> Protected under [Proprietary License](LICENSE).")
            content.append("> No unauthorized reproduction, distribution, or use permitted.")
            content.append("")
            content.append("---")
            content.append("")
    
    # Footer
    content.append("## 📧 Contact for Licensing & Permissions")
    content.append("")
    content.append("For permissions to use any of these works, please contact:")
    content.append("")
    content.append("**Prayaga Vaibhav**")
    content.append("- Email: vaibhavlakshmi18@icloud.com")
    content.append("- Email: vaibhavlakshmi18@outlook.com")
    content.append("- Email: narasimhudumeetsworld@outlook.com")
    content.append("- Mobile: +91 9493177052")
    content.append("- Location: Rajamahendravaram, Andhra Pradesh, India")
    content.append("")
    content.append("**Legal Representative**:")
    content.append("- Prayaga Venkata Ramakrishna, Advocate, Rajamahendravaram")
    content.append("")
    content.append("---")
    content.append("")
    content.append("**Om Vinayaka 🙏**")
    content.append("")
    content.append("_This page is automatically synchronized with ORCID profile daily._")
    content.append("")
    content.append(f"_Repository: [Om-vinayaka-prayaga-vaibhav-inventions-Copy-Right-License](https://github.com/narasimhudumeetsworld/Om-vinayaka-prayaga-vaibhav-inventions-Copy-Right-License)_")
    content.append("")
    
    # Write to file
    try:
        with open(PUBLICATIONS_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))
        print(f"✓ Generated {{PUBLICATIONS_FILE}}")
    except Exception as e:
        print(f"❌ Error writing PUBLICATIONS.md: {{e}}")

def main():
    """Main execution function"""
    print("=" * 60)
    print("Om Vinayaka 🙏")
    print("ORCID Synchronization Script")
    print("© 2024-2025 Prayaga Vaibhav - All Rights Reserved")
    print("=" * 60)
    print("")
    
    # Create data directory
    create_data_directory()
    
    # Fetch ORCID data
    data = fetch_orcid_works()
    
    if not data:
        print("❌ Failed to fetch ORCID data. Exiting.")
        return 1
    
    # Save raw data
    save_raw_data(data)
    
    # Parse works
    works_by_type = parse_works(data)
    
    if not works_by_type:
        print("⚠️ No works found to process")
        return 0
    
    # Generate publications file
    generate_publications_md(works_by_type)
    
    print("")
    print("=" * 60)
    print("✓ ORCID synchronization completed successfully!")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    exit(main())