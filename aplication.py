import sys
import re

# Kullanım: python app.py input.md output.md
infile, outfile = sys.argv[1], sys.argv[2]

with open(infile, "r", encoding="utf-8") as f:
    lines = f.readlines()

headers = [line.strip() for line in lines if line.startswith("#")]
toc = ["## İçindekiler\n"]
for h in headers:
    level = h.count("#")
    title = h.replace("#", "").strip()
    link = title.lower().replace(" ", "-")
    toc.append("  " * (level-1) + f"- [{title}](#{link})\n")

with open(outfile, "w", encoding="utf-8") as f:
    f.writelines(toc + ["\n"] + lines)

print(f"✔ {outfile} dosyası oluşturuldu")
