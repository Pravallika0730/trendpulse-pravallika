import requests
import json
import os
import time
from datetime import datetime

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm", "programming"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global", "policy"],
    "sports": ["nfl", "nba", "fifa", "sport", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome", "experiment"],
    "entertainment": ["movie", "film", "music", "netflix", "book", "show", "award", "streaming"]
}

def get_category(title):
    title = title.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title:
                return category
    return None

collected_data = []
category_count = {cat: 0 for cat in categories}
category_list = list(categories.keys())

try:
    res = requests.get(TOP_STORIES_URL, headers=headers, timeout=5)
    res.raise_for_status()
    story_ids = res.json()[:2000]   # increased pool
except Exception as e:
    print("Error fetching top stories:", e)
    exit()

for story_id in story_ids:

    if all(count >= 25 for count in category_count.values()):
        break

    try:
        res = requests.get(ITEM_URL.format(story_id), headers=headers, timeout=5)
        res.raise_for_status()
        story = res.json()
    except:
        continue

    if not story or "title" not in story:
        continue

    category = get_category(story["title"])

    # SMART fallback (balanced)
    if category is None:
        # pick category with least count
        category = min(category_count, key=category_count.get)

    if category_count[category] < 25:
        data = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected_data.append(data)
        category_count[category] += 1

        print(f"Added [{category}] - {story['title']}")

        if category_count[category] == 25:
            print(f"Completed {category}, waiting 2 seconds...")
            time.sleep(2)

if not os.path.isdir("data"):
    os.makedirs("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(collected_data, f, indent=4)

print(f"\nCollected {len(collected_data)} stories. Saved to {filename}")