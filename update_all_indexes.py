import os
import yaml
from datetime import date

SECTIONS = {
    "Ongoing Projects": "ongoing",
    "Completed Projects": "completed",
    "On Hold":"on_hold",
    "Archived Projects": "archive"
}

MAIN_INDEX = "index.md"
REQUIRED_FIELDS = ["title", "started", "description", "language", "goal"]

def is_valid_metadata(meta):
    return all(field in meta for field in REQUIRED_FIELDS)

def extract_frontmatter(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines[0].strip() != "---":
        return None

    fm_lines = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        fm_lines.append(line)

    try:
        return yaml.safe_load("".join(fm_lines))
    except yaml.YAMLError:
        return None

def build_sub_index_table(entries):
    header = "| Project | Started | Description | Language | Goal |\n"
    divider = "|---------|---------|-------------|----------|------|\n"
    rows = []
    for meta in entries:
        row = f"| [{meta['title']}]({meta['rel_path']}) | {meta['started']} | {meta['description']} | {meta['language']} | {meta['goal']} |"
        rows.append(row)
    return header + divider + "\n".join(rows)

def build_main_index_table(entries,section_name,folder):
    header = f"""[{section_name} index](./{folder}/index.md)\n
| Project | Started | Description |\n"""
    divider = "|---------|---------|-------------|\n"
    rows = []
    for meta in entries:
        row = f"| [{meta['title']}]({meta['rel_path']}) | {meta['started']} | {meta['description']} |"
        rows.append(row)
    return header + divider + "\n".join(rows)

def update_sub_index(section_name, folder):
    entries = []
    for fname in os.listdir(folder):
        if fname.endswith(".md") and fname != "index.md":
            full_path = os.path.join(folder, fname)
            frontmatter = extract_frontmatter(full_path)
            if frontmatter and is_valid_metadata(frontmatter):
                frontmatter["rel_path"] = f"./{fname}"
                entries.append(frontmatter)
                print(f"Processed: {fname} -> {frontmatter['title']}")

    entries.sort(key=lambda x: x.get("started", ""), reverse=True)
    
    table = build_sub_index_table(entries)

    header, tail = get_header_and_tail(folder)

    maintable = build_main_index_table(entries,section_name,folder)
    index_path = os.path.join(folder, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(header + table+ tail)

    return f"## {section_name}\n\n" + maintable + "\n"

def get_header_and_tail(folder):
    tail = f"\n\n > _This Index is automatically maintained. Last updated: **{date.today()}**_"
    if (folder == "ongoing"):
        head = """# ongoing projects
This section lists all currently active projects with more detail than the [main index](../index.md).

To be considered "ongoing," a project should show activity at least once a month.
If a project becomes inactive, it will be either:
- moved to the **archive** (if dropped permanently), or 
- moved to **on-hold** (if I plan to return to it later)

"""
        return head, tail
    if (folder == "completed"):
        head = """# Completed projects
This section lists all currently active projects with more detail than the [main index](../index.md).

To be considered "ongoing," a project should show activity at least once a month.
If a project becomes inactive, it will be either:
- moved to the **archive** (if dropped permanently), or 
- moved to **on-hold** (if I plan to return to it later)

"""
        return head, tail
    if (folder == "archive"):
        head = """# Archived projects
This section lists all currently active projects with more detail than the [main index](../index.md).

To be considered "ongoing," a project should show activity at least once a month.
If a project becomes inactive, it will be either:
- moved to the **archive** (if dropped permanently), or 
- moved to **on-hold** (if I plan to return to it later)

"""
        return head, tail
    if (folder == "on_hold"):
        head = """# On Hold projects
This section lists all currently active projects with more detail than the [main index](../index.md).

To be considered "ongoing," a project should show activity at least once a month.
If a project becomes inactive, it will be either:
- moved to the **archive** (if dropped permanently), or 
- moved to **on-hold** (if I plan to return to it later)

"""
        return head, tail
    else:
        return "",""

def update_main_index():
    main_head = f"""# Project Portfolio Index
Welcome to my markdown-based dev journal that functions as a portfolio.  
Below you'll find all of my projects, organized by status: ongoing, completed,on hold, and archived.

"""
    main_tail =f"""

## Navigation
- [README.md](./README.md) # Learn more about this repo
- [Contact.md].(./CONTACT.md) # My contact info and a bit about my self


> _This Index is automatically maintained. Last updated: **{date.today()}**_
"""
    content = ""
    content += main_head
    for section, folder in SECTIONS.items():
        section_block = update_sub_index(section, folder)
        content += section_block + "\n"
    content += main_tail
    with open(MAIN_INDEX, "w", encoding="utf-8") as f:
        f.write(content)

    print("All indexes updated!")
if __name__ == "__main__":
    update_main_index()