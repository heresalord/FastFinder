# 🔍 FASTFINDER BY DU-ROCK KOUMASSI / File Search Tool

A powerful terminal-based tool to search for strings inside files (supports `.py`, `.js`, `.html`, `.css`, `.php`, `.ts`, `.json`, `.txt`) with progress bars, highlights, and export to JSON.

## Features

- Supports multiple file types
- Case-insensitive search option
- Highlights matches in the terminal
- Exports results as JSON
- Shows performance stats (time, files, total size)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/heresalord/FastFinder.git
cd file-search-tool
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

Usage
Place the files you want to scan in the static/ folder, then run:

```bash
python search_tool.py
Follow the prompts to enter a search term and export results.
```

Output
Results can be exported in JSON format inside the export/ folder.