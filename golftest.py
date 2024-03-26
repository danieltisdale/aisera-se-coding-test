import requests
import json

# Replace with the actual API URL
api_url = "https://golf-leaderboard-data.p.rapidapi.com/world-rankings"

# Optional: Set headers if required by the API
headers = {'X-RapidAPI-Key': '147b790dc0msh8ff89029e585bf0p185e34jsn65e02967b12a',
    'X-RapidAPI-Host': 'golf-leaderboard-data.p.rapidapi.com'}  # Add headers here if needed

# Send the API request
response = requests.get(api_url, headers=headers)

# Check for successful response
if response.status_code == 200:
  # Parse the JSON response
  data = response.json()

# Extract player data
player_data = []
for ranking in data["results"]["rankings"]:
  player_data.append({
      "player_name": ranking["player_name"],
      "position": ranking["position"]
  })

# Write data to a .txt file
with open("player_data.txt", "w") as file:
  for player in player_data:
    # Convert dictionary to string with clear formatting
    player_string = json.dumps(player, indent=4)
    file.write(player_string + "\n")

print("Player data written to player_data.txt")
