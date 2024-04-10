#!/bin/bash



URL="https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" 

# Retrieve data from NOAA Aviation Weather API
# Parse data and pull out the receiptTime value 
# Output only the first six values to the screen (use head -n 6)
RESULT=$(curl "$URL" | jq '.[].receiptTime' | head -n 6)

# Print out the first six values
echo "$RESULT"
