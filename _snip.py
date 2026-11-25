html = open("index.html", encoding="utf-8", errors="replace").read()
for needle in [".gh-stats", ".gh-grid", "ghRand", "id=\"stats\"", "gh-bg"]:
    i = html.find(needle)
    print("\n====", needle, i, "====")
    if i >= 0:
        print(html[max(0, i-80): i+900])
