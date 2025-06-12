#  Project Blog

Welcome to my **Markdown Blog** where I document and reflect on all my **ongoing** and **completed projects**.  
This repo serves as a developer journal, tracking ideas, progress, challenges, and outcomes.


##  Structure
├── [README.md](./README.md) # This file 

├── [index.md](./index.md) # List of all projects

├── [Contact.md](./contact.md) # A bit about me and how to reach me

├── [ongoing/](./ongoing/index.md) # Active projects in progress

├── [completed/](./completed/index.md) # Finished projects

├── [On hold/](./on_hold/index.md) # on hold projects

├── [archive/](./archive/index.md) # Deprecated or old work

└── assets/images/ # Screenshots, diagrams, etc.

## Purpose
- Document ongoing work and updates.
- Reflect on completed projects and lessons learned.
- Organize ideas and experiments.
- Share insights or dev logs in a simple, readable format.

## Projects Overview
- [Ongoing Projects](./ongoing/)
- [Completed Projects](./completed/)
- [Archived Work](./archive/)

## Auto-Generated Indexes
- The `index.md` files in project folders are generated automatically.
- Any direct edits to them will be overwritten by the GitHub workflow.
- To regenerate manually, run:

```bash
python update_all_indexes.py
```

## Example Project Entry Format

Each project entry follows a template:
```markdown
---
title:
status: 
started:
description:
language: 
goal: 
tags:
---

# Project Name
**Status:** Ongoing / Completed  
**Start Date:** YYYY-MM-DD

## Overview
Brief description...

## Collaborators
- [Collabotator github username](link_their_github_user)

## Goals
- [ ] Goal 1
- [x] Goal 2

## Stack
- Technologies used

## Progress
- YYYY-MM-DD: Started work
- YYYY-MM-DD: Reached MVP

## Links
- [Repo](link)
```
> _This README is manually maintained. Last updated: **2025-06-12**_