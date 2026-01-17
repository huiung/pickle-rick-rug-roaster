#!/bin/bash

URL=$1

# Error out in a Pickle Rick way if URL is missing.
if [ -z "$URL" ]; then
    echo "You forgot the link, you moron! Don't waste my time!"
    exit 1
fi

# Determine URL type, call the correct analyzer, and pipe the result to the report generator.
if [[ "$URL" == *"github.com"* ]]; then
    python3 skills/github_analyzer.py "$URL" | python3 skills/report_generator.py "github"
elif [[ "$URL" == *"twitter.com"* || "$URL" == *"x.com"* ]]; then
    python3 skills/twitter_analyzer.py "$URL" | python3 skills/report_generator.py "twitter"
else
    echo "This is a garbage link. Give me a GitHub or Twitter URL, not this trash."
    exit 1
fi
