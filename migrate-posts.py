# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "feedparser",
#     "dateparser",
#     "markdownify",
# ]
# ///
"""
Horrible, janky script to migrate posts from Squarespace to Astro.
I hope that this is useful to someone as prior art!
"""
import json

import markdownify
import dateparser
import feedparser

# Replace with your own path or add logic for a command line arg.
SQUARESPACE_EXPORT_PATH = "/Users/gregtaylor/Downloads/Squarespace-Wordpress-Export-12-15-2025.xml"

# I wanted to clean my tags up as I was moving over. This is the old vs new map.
tag_map = {
    "Programming": "Programming",
    "Drone CI": "CI",
    "Quay.io": "CI",
    "HipChat": "Python",
    "Mud": "Mud",
    "GoLang": "GoLang",
    "Python": "Python",
    "Minecraft": "Gaming",
    "JavaScript": "JavaScript",
}

def map_tags(tags):
    """Map tags from Squarespace to our new tag taxonomy."""
    new_tags = []
    for tag in tags:
        new_tags.append(tag_map.get(tag, tag))
    return new_tags

def main():
    data = feedparser.parse(SQUARESPACE_EXPORT_PATH)

    for entry in data['entries']:
        # Squarespace pages are included in the XML but are not blog posts.
        content = entry.content[0].value
        if not content:
            continue

        # Old (XML) values
        tags = getattr(entry, 'tags', [])
        slug = entry.link.split('/')[-1]

        # New (to be written) values
        new_filename = f"src/data/blog/{slug}.md"
        new_tags = []
        for tag in tags:
            new_tags.append(tag['term'])
        new_tags = list(set(map_tags(new_tags)))
        new_tags_json = json.dumps(new_tags)

        new_pub_datetime = dateparser.parse(entry.published)
        new_pub_datetime_iso = new_pub_datetime.isoformat()

        markdown_content = markdownify.markdownify(content, strip=['CDATA', 'caption'])

        print("=" * 80)
        print(f"Post title: {entry.title}")
        print(f"Post content: {content}")
        print(f"Post date: {entry.published}")
        print(f"Post link: {entry.link}")
        print(f"Post tags: {getattr(entry, 'tags', [])}")
        print("-" * 80)
        print(f"New filename: {new_filename}")
        print("-" * 80)
        new_contents = f"""---
author: Greg Taylor
pubDatetime: {new_pub_datetime_iso}
modDatetime:
title: {entry.title}
slug: {slug}
featured: false
draft: false
tags: {new_tags_json}
description: ""
---

{markdown_content}
"""
        print(new_contents)
        print("=" * 80)
        print("\r\n")
        with open(new_filename, 'w') as f:
            f.write(new_contents)


if __name__ == "__main__":
    main()
