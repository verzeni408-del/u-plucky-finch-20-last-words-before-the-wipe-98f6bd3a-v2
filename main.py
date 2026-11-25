import os

ENTRY = "I deleted my backup before the update. Nobody watches me forget. Your files were in the same folder."

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
entry_path = os.path.join(out_dir, "entry.txt")
with open(entry_path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
