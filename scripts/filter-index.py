import json

# Load upstream index.json
with open("index.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Load blacklist (names, not package names)
with open("blacklist.txt", "r", encoding="utf-8") as f:
    blacklist = {line.strip() for line in f if line.strip()}

# Filter extensions
extensions = data["extensionList"]["extensions"]
filtered = [
    ext for ext in extensions
    if ext["name"] not in blacklist
]

# Replace list
data["extensionList"]["extensions"] = filtered

# Write cleaned index.json
with open("index.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Write minified index.min.json
with open("index.min.json", "w", encoding="utf-8") as f:
    json.dump(data, f, separators=(",", ":"))
