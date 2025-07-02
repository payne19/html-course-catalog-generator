import os
from pathlib import Path
from html import escape
import sys
import re


if len(sys.argv)>1:
    path_dir = sys.argv[1]
    path_dir = path_dir.replace('\\', '/').replace('"', '').replace("'", "")
    COURSE_ROOT = Path(path_dir)
else:
    print('Please enter the path')

def sanitize(name):
    return re.sub(r"[^\w\s\-.]", "", name)

for root, dirs, files in os.walk(COURSE_ROOT, topdown=False):
    for filename in files:
        old_path = os.path.join(root, filename)
        sanitized_name = sanitize(filename)
        new_path = os.path.join(root, sanitized_name)
        if old_path != new_path:
            os.rename(old_path, new_path)

    for dirname in dirs:
        old_dir = os.path.join(root, dirname)
        sanitized_dir = sanitize(dirname)
        new_dir = os.path.join(root, sanitized_dir)
        if old_dir != new_dir:
            os.rename(old_dir, new_dir)

def get_icon(file: Path):
    ext = file.suffix.lower()
    if ext == ".mp4":
        return "🎬"
    elif ext == ".pdf":
        return "📄"
    elif ext in {".html", ".htm"}:
        return "🔗"
    elif ext in {".txt", ".url"}:
        return "📃"
    else:
        return "📁"

def create_html_index(course_root: Path):
    html_lines = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <title>{}</title>".format(escape(course_root.name) + " Index"),
        "  <link rel='stylesheet' href='styles.css'>",
        "  <script defer src='script.js'></script>",
        "</head>",
        "<body>",
        "  <button id='darkModeToggle'>🌓 Toggle Dark Mode</button>",
        "  <input type='text' id='searchBar' placeholder='Search files...' />",
        "  <h1>{} – Course Index</h1>".format(escape(course_root.name))
    ]

    def process_folder(folder: Path, level=2):
        title = escape(folder.name)
        html_lines.append(f"{'  ' * level}<section>")
        html_lines.append(f"{'  ' * (level + 1)}<h{level + 1}>{title}</h{level + 1}>")
        html_lines.append(f"{'  ' * (level + 1)}<ul>")

        for item in sorted(folder.iterdir()):
            if item.name == "index.html":
                continue 
            if item.is_file():
                ext = item.suffix.lower()
                if ext in {".mp4", ".pdf", ".url", ".html", ".txt"}:
                    icon = get_icon(item)
                    rel_path = item.relative_to(course_root).as_posix()
                    html_lines.append(
                        f"{'  ' * (level + 2)}<li>{icon} <a href='{rel_path}'>{escape(item.name)}</a></li>"
                    )
            elif item.is_dir():
                process_folder(item, level + 1)

        html_lines.append(f"{'  ' * (level + 1)}</ul>")
        html_lines.append(f"{'  ' * level}</section>")

    for subfolder in sorted(course_root.iterdir()):
        if subfolder.is_dir() and subfolder.name[0].isdigit():
            process_folder(subfolder)

    html_lines.append('<div id="player-area"></div>')
    html_lines.append("</body>")
    html_lines.append("</html>")

    output_path = course_root / "index.html"
    output_path.write_text("\n".join(html_lines), encoding="utf-8")
    print(f"✅ index.html created at: {output_path.resolve()}")

if __name__ == "__main__":
    create_html_index(COURSE_ROOT)
