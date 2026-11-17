#!/usr/bin/env python3
"""Create the next reviewed project from the repository's curated daily queue."""
from __future__ import annotations
import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = [
 {"title":"Blooming Flower","slug":"Blooming-Flower","emoji":"🌸","description":"A colourful flower made from repeating Turtle petals.","code":'''import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#101827")
screen.title("Blooming Flower")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#ff5c8a", "#ffb347", "#ffe66d", "#7bdff2", "#b2f7ef", "#cdb4db"]
for i in range(36):
    pen.color(colors[i % len(colors)])
    pen.circle(90, 60)
    pen.left(120)
    pen.circle(90, 60)
    pen.left(10)
pen.hideturtle()
turtle.done()
'''},
 {"title":"Neon Spiral","slug":"Neon-Spiral","emoji":"🌀","description":"A vibrant geometric spiral drawn with a changing neon palette.","code":'''import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#090b1a")
screen.title("Neon Spiral")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
colors = ["#ff4d8d", "#a78bfa", "#38bdf8", "#34d399", "#facc15"]
for i in range(100):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 3)
    pen.right(91)
pen.hideturtle()
turtle.done()
'''},
 {"title":"Golden Star","slug":"Golden-Star","emoji":"⭐","description":"A golden five-point star drawn and filled with Python Turtle.","code":'''import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#171323")
screen.title("Golden Star")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(5)
pen.color("#ffd166", "#f4a261")
pen.penup()
pen.goto(0, 150)
pen.pendown()
pen.begin_fill()
for _ in range(5):
    pen.forward(280)
    pen.right(144)
pen.end_fill()
pen.hideturtle()
turtle.done()
'''},
 {"title":"Snowflake Mandala","slug":"Snowflake-Mandala","emoji":"❄️","description":"A symmetrical icy mandala made from repeating geometric branches.","code":'''import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#071a2b")
screen.title("Snowflake Mandala")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.color("#8be9fd")
for _ in range(12):
    for length in (90, 35, 35):
        pen.forward(length)
        pen.backward(length)
        pen.left(45)
    pen.right(75)
    pen.forward(90)
    pen.backward(90)
    pen.left(30)
pen.hideturtle()
turtle.done()
'''},
 {"title":"Rainbow Polygon","slug":"Rainbow-Polygon","emoji":"🌈","description":"A colourful layered polygon pattern made from rotating shapes.","code":'''import turtle
screen = turtle.Screen()
screen.setup(650, 580)
screen.bgcolor("#111827")
screen.title("Rainbow Polygon")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
colors = ["#ff595e", "#ffca3a", "#8ac926", "#1982c4", "#6a4c93"]
for layer in range(18):
    pen.pencolor(colors[layer % len(colors)])
    for _ in range(6):
        pen.forward(110 + layer * 4)
        pen.left(60)
    pen.left(20)
pen.hideturtle()
turtle.done()
'''},
]

def main() -> None:
    days = [int(m.group(1)) for p in ROOT.glob("Day-*") if (m := re.match(r"Day-(\d+)-", p.name))]
    day = max(days, default=0) + 1
    index = day - 3
    if index < 0:
        index = 0
    if index >= len(PROJECTS):
        print("Daily project queue is complete; no placeholder commit created.")
        return
    item = PROJECTS[index]
    folder = ROOT / f"Day-{day:02d}-{item['slug']}"
    folder.mkdir(parents=True, exist_ok=False)
    ast.parse(item["code"])
    (folder / "main.py").write_text(item["code"], encoding="utf-8")
    (folder / "README.md").write_text(
        f"# Day {day:02d} — {item['title']}\n\n{item['description']}\n\n"
        "## Run locally\n\nRun python main.py with Python 3 and Turtle/Tk graphics support.\n",
        encoding="utf-8",
    )
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    marker = "## Run locally"
    row = f"| {day:02d} | [{item['title']}]({folder.name}/) | {item['description']} |\n"
    if marker not in text:
        raise RuntimeError("README is missing the project table insertion point.")
    readme.write_text(text.replace(marker, row + "\n" + marker, 1), encoding="utf-8")
    index_path = ROOT / "index.html"
    html = index_path.read_text(encoding="utf-8")
    marker = "<!-- DAILY_PROJECT_CARDS -->"
    if marker not in html:
        raise RuntimeError("index.html is missing DAILY_PROJECT_CARDS marker.")
    key = f"day-{day:02d}"
    card = f"""
<article class="card"><div class="art"><div class="generated-art">{item['emoji']}</div></div><div class="cardbody"><div class="day">Day {day:02d} · Turtle Graphics</div><h2>{item['title']}</h2><p>{item['description']}</p><div class="links"><button class="runbtn" data-run="{key}">▶ Run &amp; Preview</button><a href="{folder.name}/main.py">View Python source ↗</a><a href="https://github.com/Lokesh087/Daily-Python-creation/tree/main/{folder.name}">GitHub folder ↗</a></div></div><section class="runner" id="runner-{key}"><div class="runnerbar"><span class="runstatus" id="status-{key}">Ready to run the original Python program.</span><button class="smallbtn" data-source="{key}">View Code</button></div><div class="turtle-stage" id="canvas-{key}"></div><pre class="source" id="source-{key}"></pre></section></article>
"""
    html = html.replace(marker, card + marker, 1)
    old = "radha:{file:'Day-02-Radha-Krishna-Art/main.py',canvas:'canvas-radha',status:'status-radha'}};"
    new = old.replace("}};", f"}}, {key}:{{file:'{folder.name}/main.py',canvas:'canvas-{key}',status:'status-{key}'}}}};")
    if old not in html:
        raise RuntimeError("Could not find browser project registry insertion point.")
    html = html.replace(old, new, 1)
    if ".generated-art" not in html:
        html = html.replace(".art svg{width:min(90%,360px);height:90%;overflow:visible}", ".art svg{width:min(90%,360px);height:90%;overflow:visible}.generated-art{font-size:104px;filter:drop-shadow(0 10px 24px #a78bfa66)}", 1)
    index_path.write_text(html, encoding="utf-8")
    print(f"Created Day {day:02d}: {item['title']}")

if __name__ == "__main__":
    main()
