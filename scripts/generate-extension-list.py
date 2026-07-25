import json

# Load upstream TaichiManga-compatible JSON
with open("index.min.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Load blacklist (names)
with open("blacklist.txt", "r", encoding="utf-8") as f:
    blacklist = {line.strip() for line in f if line.strip()}

names_txt = []

for ext in data:
    # Extract raw name (remove prefixes)
    raw_name = ext["name"].replace("Tachiyomi: ", "").replace("Bearepo: ", "")

    # Skip blacklisted names
    if raw_name in blacklist:
        continue

    # Keep only English or multi-language
    if ext.get("lang") not in ("en", "all"):
        continue

    # Save name to txt list
    names_txt.append(raw_name)

# Write names to a .txt file
with open("filtered_extensions.txt", "w", encoding="utf-8") as f:
    for name in names_txt:
        f.write(name + "\n")
