import sys
import json
import re
import random # For demo purposes

def analyze_github(url):
    """
    Analyzes a GitHub repository.
    In a real implementation, this would use the GitHub API.
    For this script, it generates plausible random data.
    """
    if not re.search(r"github\.com/([^/]+)/([^/]+)", url):
        print(json.dumps({"error": "Invalid GitHub URL"}), file=sys.stderr)
        sys.exit(1)
        
    analysis_results = {
        "commit_frequency": round(random.uniform(0.1, 5.0), 1),  # Commits per week
        "contributor_count": random.randint(1, 10),
        "has_readme": random.choice([True, False]),
        "readme_length": random.randint(20, 5000),
        "has_license": random.choice([True, False]),
        "days_since_creation": random.randint(1, 365),
        "star_count": random.randint(0, 100),
    }
    print(json.dumps(analysis_results))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "GitHub URL argument is missing."}), file=sys.stderr)
        sys.exit(1)
    analyze_github(sys.argv[1])
