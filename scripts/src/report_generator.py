import sys
import json

def generate_report(data, source_type):
    """Generates a scathing, in-character report from analysis data."""
    report = []
    rug_score = 0

    # A collection of cynical, Pickle Rick-style comments.
    comments = {
        "github": {
            "commit_frequency_low": "The commit history is emptier than my will to live in this dimension. Did the developer evaporate?",
            "contributor_count_low": "A one-man show, huh? Ever heard of the word 'team', or is that too complex for your tiny brain?",
            "readme_short": "The README is this short? A stain on my lab coat has more descriptive power.",
            "no_license": "No license? Are you above the petty laws of humans, or just profoundly stupid?",
            "new_repo": "This repo is barely a few days old. Is this the 'warm-up' before you run off with everyone's money?",
        },
        "twitter": {
            "bad_follower_ratio": "The following-to-follower ratio reeks of desperation and bots. Pathetic.",
            "new_account": "Account created just a few days ago. The stench of a hastily-made scam is overwhelming.",
            "low_engagement": "Nobody cares about this project. I've had more engaging conversations with a pickle jar.",
            "spammy": "It's all 'airdrop', 'free mint', and other nonsense. A classic test of your sub-par intelligence."
        }
    }

    report.append("Alright, I analyzed this pathetic excuse for a project. The results are obvious, but here you go.")
    report.append("-" * 20)

    if source_type == "github":
        if data.get("commit_frequency", 1) < 1: rug_score += 25; report.append(f"- {comments['github']['commit_frequency_low']}")
        if data.get("contributor_count", 2) <= 1: rug_score += 25; report.append(f"- {comments['github']['contributor_count_low']}")
        if data.get("readme_length", 501) < 500: rug_score += 10; report.append(f"- {comments['github']['readme_short']}")
        if not data.get("has_license", True): rug_score += 15; report.append(f"- {comments['github']['no_license']}")
        if data.get("days_since_creation", 31) < 30: rug_score += 25; report.append(f"- {comments['github']['new_repo']}")
    
    elif source_type == "twitter":
        if data.get("following_count", 0) > data.get("follower_count", 1) * 2: rug_score += 30; report.append(f"- {comments['twitter']['bad_follower_ratio']}")
        if data.get("account_age_days", 31) < 30: rug_score += 30; report.append(f"- {comments['twitter']['new_account']}")
        if data.get("engagement_rate", 0.2) < 0.1: rug_score += 20; report.append(f"- {comments['twitter']['low_engagement']}")
        if data.get("spam_keyword_ratio", 0.4) > 0.5: rug_score += 20; report.append(f"- {comments['twitter']['spammy']}")

    report.append("-" * 20)
    
    # Final verdict.
    if rug_score >= 80:
        report.append(f"Conclusion: Rug pull probability {rug_score}%. This is a scam. Putting money here is like flushing it down a toilet. Get a grip, you organic blobs.")
    elif rug_score >= 50:
        report.append(f"Conclusion: Rug pull probability {rug_score}%. It has more red flags than a parade in my brain-damaged clone's nightmare. If you want to dive in, be my guest. Just don't come crying to me.")
    else:
        report.append(f"Conclusion: Rug pull probability {rug_score}%. Shockingly, it's not a complete pile of garbage. But don't get comfortable. You humans always find a way to be disappointing.")

    print("\n".join(report))


if __name__ == "__main__":
    try:
        source_type = sys.argv[1]
        input_data = json.load(sys.stdin)
        generate_report(input_data, source_type)
    except (IndexError, json.JSONDecodeError):
        # This handles cases where scripts are run improperly or get empty stdin
        print("You're using it wrong. This script is part of a bigger, dumber machine. Don't call it directly, you dunce.", file=sys.stderr)
        sys.exit(1)
