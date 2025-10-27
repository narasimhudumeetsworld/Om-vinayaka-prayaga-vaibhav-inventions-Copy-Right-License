# ORCID Integration Documentation

**Om Vinayaka 🙏**

## Overview

This repository features automated synchronization with the ORCID profile of **Prayaga Vaibhav** (Woman Inventor), ensuring that all academic works, thesis, journal articles, patents, and other publications are automatically synchronized and displayed with proper copyright protection.

**ORCID Profile**: [https://orcid.org/0009-0007-8995-0895](https://orcid.org/0009-0007-8995-0895)

---

## ⚖️ COPYRIGHT NOTICE

**© 2024-2025 Prayaga Vaibhav. All Rights Reserved.**

All synchronized works remain protected under the [Proprietary License](LICENSE) of this repository. No part of any work may be reproduced, distributed, transmitted, modified, or otherwise used without express written permission from Prayaga Vaibhav.

---

## Features

### 🔄 Automatic Synchronization

- **Daily Updates**: Runs automatically every day at 2:00 AM UTC
- **Manual Trigger**: Can be manually triggered from GitHub Actions
- **Real-time Sync**: Fetches latest works from ORCID public API
- **Smart Updates**: Only commits when new works are added or existing works are modified

### 📋 Comprehensive Coverage

The synchronization system fetches and categorizes all types of works:

- 📄 **Journal Articles** - Peer-reviewed publications
- 📑 **Conference Papers** - Conference proceedings and presentations
- 📚 **Books** - Published books and monographs
- 📖 **Book Chapters** - Contributions to edited volumes
- 🎓 **Thesis/Dissertations** - PhD, Master's, and other academic theses
- 💡 **Patents/Inventions** - Patent applications and granted patents
- 📝 **Preprints** - Early versions and preprints
- 📊 **Reports and Datasets** - Technical reports and research datasets
- 🛠️ **Research Tools** - Software, tools, and methodologies
- 📌 **Other Works** - Any other scholarly contributions

### 🛡️ Copyright Protection

Every synchronized work includes:
- Full copyright notice
- License reference
- Contact information for permissions
- Attribution requirements

### 📁 Files Generated

1. **PUBLICATIONS.md** - Main publications listing with formatting
2. **data/orcid_works.json** - Raw ORCID data cache (gitignored)

---

## Technical Implementation

### Components

#### 1. Sync Script (`scripts/sync_orcid.py`)

Python script that:
- Fetches works from ORCID public API
- Parses and categorizes works by type
- Generates formatted PUBLICATIONS.md
- Includes copyright notices for each work
- Saves raw data for debugging

#### 2. GitHub Actions Workflow (`.github/workflows/sync-orcid.yml`)

Automated workflow that:
- Runs on schedule (daily at 2 AM UTC)
- Can be triggered manually
- Installs Python dependencies
- Executes sync script
- Commits changes if updates found
- Provides summary in GitHub Actions UI

#### 3. Dependencies (`requirements.txt`)

Minimal Python dependencies:
- `requests` - For ORCID API calls

### How It Works

```
┌─────────────────────────────────────────────────────────┐
│  GitHub Actions Workflow (Daily at 2 AM UTC)           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  1. Checkout Repository                                 │
│  2. Setup Python 3.11                                   │
│  3. Install dependencies (requests)                     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Run sync_orcid.py Script                               │
│  ├── Fetch from ORCID API                               │
│  ├── Parse works by type                                │
│  ├── Generate PUBLICATIONS.md                           │
│  └── Save raw JSON cache                                │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Check for Changes                                      │
│  └── Compare PUBLICATIONS.md with git                   │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  If Changed: Commit and Push                            │
│  ├── Configure git user                                 │
│  ├── Add PUBLICATIONS.md and data/                      │
│  ├── Commit with timestamp                              │
│  └── Push to repository                                 │
└─────────────────────────────────────────────────────────┘
```

---

## Usage

### Viewing Publications

Simply visit [PUBLICATIONS.md](../PUBLICATIONS.md) to see all synchronized works.

The file includes:
- Full title of each work
- Publication date
- Source/journal information
- DOI or URL links
- Copyright notices
- Type categorization

### Manual Synchronization

To manually trigger a sync:

1. Go to the repository on GitHub
2. Navigate to **Actions** tab
3. Select **Sync ORCID Publications** workflow
4. Click **Run workflow**
5. Select the branch (usually `main`)
6. Click **Run workflow** button

The workflow will run immediately and update PUBLICATIONS.md if there are any changes.

### Local Testing

To test the sync script locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the sync script
python scripts/sync_orcid.py
```

This will:
- Create a `data/` directory (if not exists)
- Fetch works from ORCID
- Generate PUBLICATIONS.md
- Save raw JSON to data/orcid_works.json

---

## Configuration

### Updating ORCID ID

If needed, update the ORCID ID in `scripts/sync_orcid.py`:

```python
ORCID_ID = "0009-0007-8995-0895"  # Update this line
```

### Changing Sync Schedule

Edit `.github/workflows/sync-orcid.yml` to change the schedule:

```yaml
schedule:
  - cron: '0 2 * * *'  # Currently: Daily at 2 AM UTC
  # Examples:
  # - cron: '0 */6 * * *'  # Every 6 hours
  # - cron: '0 0 * * 0'    # Weekly on Sunday
  # - cron: '0 0 1 * *'    # Monthly on 1st
```

---

## Troubleshooting

### Workflow Not Running

1. Check that GitHub Actions are enabled for the repository
2. Verify the workflow file is in `.github/workflows/`
3. Check repository permissions allow workflows to write

### No Updates Appearing

1. Verify works are added to ORCID profile
2. Check ORCID profile is public (not private)
3. Review GitHub Actions logs for errors
4. Manually trigger workflow to test

### API Errors

1. ORCID API may be temporarily unavailable
2. Rate limiting may apply (unlikely with daily sync)
3. Network issues may prevent connection
4. Check GitHub Actions logs for specific error messages

---

## Maintenance

### Regular Tasks

- ✅ **Automatic**: Daily sync via GitHub Actions
- ✅ **Automatic**: Commit and push changes
- ✅ **Automatic**: Update PUBLICATIONS.md
- ⚠️ **Manual**: Review sync logs occasionally
- ⚠️ **Manual**: Update ORCID profile with new works

### Data Directory

The `data/` directory contains:
- `orcid_works.json` - Raw ORCID API response (cached)

This directory is gitignored and not committed to the repository.

---

## Copyright & Licensing

All synchronized works are protected under the **Prayaga Vaibhav Proprietary License**.

### For Each Work

Each work in PUBLICATIONS.md includes:
```markdown
**COPYRIGHT NOTICE**:
> © 2024-2025 Prayaga Vaibhav. All Rights Reserved.
> Protected under [Proprietary License](LICENSE).
> No unauthorized reproduction, distribution, or use permitted.
```

### Permissions

For permissions to use any of these works, contact:

**Prayaga Vaibhav**
- Email: vaibhavlakshmi18@icloud.com
- Email: vaibhavlakshmi18@outlook.com
- Email: narasimhudumeetsworld@outlook.com
- Mobile: +91 9493177052
- Location: Rajamahendravaram, Andhra Pradesh, India

**Legal Representative**:
- Prayaga Venkata Ramakrishna, Advocate, Rajamahendravaram

---

## References

- **ORCID**: [https://orcid.org/](https://orcid.org/)
- **ORCID Public API**: [https://info.orcid.org/documentation/api-tutorials/](https://info.orcid.org/documentation/api-tutorials/)
- **GitHub Actions**: [https://docs.github.com/en/actions](https://docs.github.com/en/actions)

---

**Om Vinayaka 🙏**

**© 2024-2025 Prayaga Vaibhav - All Rights Reserved**

_Part of the Om Vinayaka Comprehensive Intellectual Property Repository_
