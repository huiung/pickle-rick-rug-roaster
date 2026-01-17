import sys
import json
import re
import random # For demo purposes

def analyze_twitter(url):
    """
    Analyzes a Twitter profile.
    In a real implementation, this would use the Twitter API or a scraper.
    For this script, it generates plausible random data.
    """
    if not re.search(r"(twitter|x)\.com/([^/]+)", url):
        print(json.dumps({"error": "Invalid Twitter URL"}), file=sys.stderr)
        sys.exit(1)

    followers = random.randint(50, 10000)
    # Ensure following_count is an integer
    following = int(followers * random.uniform(0.1, 10.0))

    analysis_results = {
        "follower_count": followers,
        "following_count": following,
        "account_age_days": random.randint(1, 730),
        "engagement_rate": round(random.uniform(0.01, 5.0), 2),
        "spam_keyword_ratio": round(random.uniform(0.0, 0.9), 1),
    }
    print(json.dumps(analysis_results))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Twitter URL argument is missing."}), file=sys.stderr)
        sys.exit(1)
    analyze_twitter(sys.argv[1])
