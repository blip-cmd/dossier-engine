#!/usr/bin/env python3
"""GitHub Repository Metadata Extractor.

Extracts repository stars, forks, languages, and topics from public GitHub repos
to assist in drafting verified metrics for DossierEngine project matrices.
"""

import json
import sys
import urllib.request
import urllib.error

def fetch_repo_data(repo_slug):
    """Fetch repository info using standard library urllib."""
    url = f"https://api.github.com/repos/{repo_slug}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "DossierEngine-Extractor/1.0", "Accept": "application/vnd.github.v3+json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"[!] HTTP Error {e.code}: {e.reason} for repository {repo_slug}")
        return None
    except Exception as e:
        print(f"[!] Error fetching repository data: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python github_extractor.py <owner/repo>")
        print("Example: python github_extractor.py torvalds/linux")
        sys.exit(1)

    repo_slug = sys.argv[1].replace("https://github.com/", "").strip("/")
    print(f"[*] Querying GitHub API for {repo_slug}...")
    
    data = fetch_repo_data(repo_slug)
    if not data:
        sys.exit(1)

    print("\n" + "=" * 60)
    print(f" Repository: {data.get('full_name')}")
    print("=" * 60)
    print(f"Description : {data.get('description')}")
    print(f"Primary Lang: {data.get('language')}")
    print(f"Stars       : {data.get('stargazers_count'):,}")
    print(f"Forks       : {data.get('forks_count'):,}")
    print(f"Open Issues : {data.get('open_issues_count'):,}")
    print(f"License     : {data.get('license', {}).get('spdx_id') if data.get('license') else 'None'}")
    print(f"Topics      : {', '.join(data.get('topics', []))}")
    print("-" * 60)
    print("Suggested Dossier Bullet Starter:")
    print(f"* Architected and open-sourced {data.get('name')}, earning {data.get('stargazers_count')} stars on GitHub...")
    print("=" * 60)

if __name__ == "__main__":
    main()
