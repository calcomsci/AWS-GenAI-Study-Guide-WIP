import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<section data-section="proof" class="searchable-section">'
end_marker = '<section data-section="pairing" class="searchable-section">'
proof_section = html[html.find(start_marker):html.find(end_marker)]

cards = proof_section.split('<div class="topic-card">')[1:]

for idx, c in enumerate(cards, 1):
    title_m = re.search(r'<div class="topic-title">(.*?)</div>', c)
    img_m = re.search(r'screenshots/(sb-[a-f0-9]+\.png)', c)
    caption_m = re.search(r'class="proof-screenshot-caption">(.*?)</div>', c)
    rec_m = re.search(r'class="proof-screenshot-recommend">(.*?)</div>', c)
    
    title = title_m.group(1) if title_m else ""
    img = img_m.group(1) if img_m else ""
    caption = caption_m.group(1) if caption_m else ""
    rec = rec_m.group(1) if rec_m else ""
    
    print(f"Card {idx}: {img} | {title}")
