players = [
    {"name": "Kohli",   "runs": 741, "team": "RCB"},
    {"name": "Gill",    "runs": 890, "team": "GT"},
    {"name": "Rahul",   "runs": 616, "team": "LSG"},
    {"name": "Jaiswal", "runs": 625, "team": "RR"},
    {"name": "Samson",  "runs": 616, "team": "RR"},
]

# Sort by runs (highest to lowest)
print("By runs (high to low):")

runs = sorted(players, key=lambda p: p["runs"], reverse=True)
for p in runs:
    print(p["name"], p["runs"])


# Sort by team, then runs (highest to lowest)
print("\nBy team, then runs:")
team = sorted(players, key=lambda p: (p["team"], -p["runs"]))
for p in team:
    print(p["team"], p["name"], p["runs"])


# Sort by name length
print("\nBy name length:")

name = sorted(players, key=lambda p: len(p["name"]))
for p in name:
    print(p["name"])