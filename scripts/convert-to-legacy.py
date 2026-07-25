import json
import re

# Load Mihon-style JSON
with open("index.json", "r", encoding="utf-8") as f:
    data = json.load(f)

extensions = data["extensionList"]["extensions"]

# Load blacklist (names)
with open("blacklist.txt", "r", encoding="utf-8") as f:
    blacklist = {line.strip() for line in f if line.strip()}

legacy = []

for ext in extensions:
    name = ext["name"]
    pkg = ext["packageName"]
    version = ext["versionName"]
    code = int(ext["versionCode"])
    sources = ext.get("sources", [])

    # Skip blacklisted names
    if name in blacklist:
        continue

    # Extract APK filename from URL
    apk_url = ext["resources"]["apkUrl"]
    apk_filename = apk_url.split("/")[-1]

    # Determine language
    # If multiple languages exist, TaichiManga expects "all"
    langs = {s["language"] for s in sources}
    lang = "all" if len(langs) != 1 else next(iter(langs))

    # Determine NSFW flag
    warning = ext.get("contentWarning", "")
    nsfw = 1 if "NSFW" in warning else 0

    # Build legacy entry
    legacy.append({
        "name": f"Bearepo: {name}",
        "pkg": pkg,
        "apk": apk_filename,
        "lang": lang,
        "code": code,
        "version": version,
        "nsfw": nsfw,
        "sources": sources
    })

# Write legacy index.json (pretty)
with open("index.json", "w", encoding="utf-8") as f:
    json.dump(legacy, f, indent=2)

# Write legacy index.min.json (minified)
with open("index.min.json", "w", encoding="utf-8") as f:
    json.dump(legacy, f, separators=(",", ":"))
