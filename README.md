# GitHub_Trending_CLI

A command-line tool to fetch trending GitHub repositories.

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

```bash
git clone https://github.com/KoushikReddy3103/GitHub_Trending_CLI.git
cd trending-repos
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install --upgrade pip setuptools wheel
pip install -e .
```

## Usage

### Basic Command

```bash
trending-repos --duration week --limit 10
```

### Options

- `--duration` - Time range for trending repositories
  - Choices: `day`, `week`, `month`, `year` (default: `week`)
- `--limit` - Number of repositories to display (default: `10`)

### Examples

```bash
# Fetch top 10 trending repos from the past week
trending-repos --duration week --limit 10

# Fetch top 20 trending repos from the past year
trending-repos --duration year --limit 20

# Fetch top 5 trending repos from the past day
trending-repos --duration day --limit 5
```

## Features

- Fetch trending GitHub repositories based on time duration
- Display repository name, stars, language, and description
- Sorted by star count in descending order
- User-friendly CLI interface

## Requirements

- `requests` - for GitHub API calls

## Notes

- The CLI queries the GitHub Search API (unauthenticated)
- Subject to GitHub API rate limits (60 requests/hour for unauthenticated requests)
- For higher rate limits, consider adding a GitHub personal access token