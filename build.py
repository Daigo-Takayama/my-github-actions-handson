import os

from calc import add

os.makedirs("dist", exist_ok=True)
with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(f"<h1>Hi, CI/CD</h1><p>1 + 2 = {add(1, 2)}</p>")
