import json

# Load upstream TaichiManga-compatible JSON
with open("index.min.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Load blacklist (names)
with open("blacklist.txt", "r", encoding="utf-8") as f:
    blacklist = {line.strip() for line in f if line.strip()}

# Filter by "name"
filtered = [
    ext for ext in data
    if ext["name"].replace("Tachiyomi: ", "").replace("Bearepo: ", "") not in blacklist
]

# Write filtered index.min.json
with open("index.min.json", "w", encoding="utf-8") as f:
    json.dump(filtered, f, separators=(",", ":"))
