#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SRC_DIR="$SCRIPT_DIR/../src"

URL=$1

if [ -z "$URL" ]; then
    echo "You forgot the link, you moron! Don't waste my time!"
    exit 1
fi

if [[ "$URL" == *"github.com"* ]]; then
    python3 "$SRC_DIR/github_analyzer.py" "$URL" | python3 "$SRC_DIR/report_generator.py" "github"

elif [[ "$URL" == *"twitter.com"* || "$URL" == *"x.com"* ]]; then    
    python3 "$SRC_DIR/twitter_analyzer.py" "$URL" | python3 "$SRC_DIR/report_generator.py" "twitter"

else    
    echo "This is a garbage link. Give me a GitHub or Twitter URL, not this trash."
    exit 1
fi
