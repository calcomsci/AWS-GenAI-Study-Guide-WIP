with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

style_start = html.find('<style>')
style_end = html.find('</style>')
styles = html[style_start:style_end]

for cls in ['proof-', 'badge-', 'eliminate', 'correct']:
    matches = [line for line in styles.splitlines() if cls in line]
    print(f"Matches for {cls}: {len(matches)}")
    for m in matches[:3]:
        print("  ", m.strip())
