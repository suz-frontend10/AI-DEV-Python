import os
from datetime import datetime

folder = os.path.dirname(os.path.abspath(__file__))
files = []

for filename in os.listdir(folder):
    if filename.endswith(".py"):
        path = os.path.join(folder, filename)

        size = os.path.getsize(path)
        modified = os.path.getmtime(path)
        modified_date = datetime.fromtimestamp(modified)

        if size >= 1024:
            size_text = f"{size / 1024:.1f} KB"
        else:
            size_text = f"{size} B"

        files.append((filename, size_text, modified_date))

print(f"{'File':<25}{'Size':<12}{'Last Modified'}")
print("-" * 55)

for filename, size, modified in files:
    print(f"{filename:<25}{size:<12}{modified.strftime('%d-%m-%Y %H:%M')}")

print("-" * 55)
print(f"Total: {len(files)} files")