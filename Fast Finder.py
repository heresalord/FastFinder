import os
import time
import json
from tqdm import tqdm
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.text import Text
from datetime import datetime

console = Console()
ALLOWED_EXTENSIONS = ['.py', '.js', '.html', '.css', '.php', '.ts', '.json', '.txt']
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
EXPORT_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export")


def get_all_files(folder):
    files_list = []
    total_size = 0
    for root, _, files in os.walk(folder):
        for file in files:
            if any(file.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                path = os.path.join(root, file)
                files_list.append(path)
                total_size += os.path.getsize(path)
    return files_list, total_size


def search_in_file(file_path, query, case_insensitive=False):
    matches = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, start=1):
                haystack = line.lower() if case_insensitive else line
                needle = query.lower() if case_insensitive else query
                if needle in haystack:
                    matches.append((i, line.rstrip('\n')))
    except Exception as e:
        console.print(f"[!] Error reading {file_path}: {e}", style="bold red")
    return matches


def highlight_query_in_line(line, query, case_insensitive=False):
    text = Text()
    original_line = line
    search_line = line.lower() if case_insensitive else line
    search_query = query.lower() if case_insensitive else query

    start = 0
    while True:
        index = search_line.find(search_query, start)
        if index == -1:
            text.append(original_line[start:])
            break
        text.append(original_line[start:index])
        text.append(original_line[index:index+len(query)], style="bold yellow on red")
        start = index + len(query)
    return text


def export_results_as_json(query, case_insensitive, results, stats):
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(EXPORT_FOLDER, f"search_results_{timestamp}.json")

    export_data = {
        "search_term": query,
        "case_insensitive": case_insensitive,
        "scanned_files": stats['scanned_files'],
        "matched_files": len(results),
        "total_matches": sum(len(file["matches"]) for file in results),
        "duration_seconds": stats['duration'],
        "total_size_mb": round(stats['total_size'] / (1024 * 1024), 2),
        "results": results
    }

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=4)

    console.print(f"\n📦 Results exported to: [bold green]{file_path}[/bold green]")


def search_loop():
    while True:
        query = Prompt.ask("Enter word or phrase to search")
        case_insensitive = Confirm.ask("Should the search be case insensitive?", default=True)

        start_time = time.time()
        all_files, total_size = get_all_files(STATIC_FOLDER)

        console.print(f"\n[+] Scanning {len(all_files)} files in: [bold]{STATIC_FOLDER}[/bold]", style="cyan")

        found = False
        results_for_export = []
        total_matches = 0

        for file_path in tqdm(all_files, desc="Searching"):
            results = search_in_file(file_path, query, case_insensitive)
            if results:
                found = True
                total_matches += len(results)
                console.print(f"\n[✓] Matches found in {file_path}", style="bold green")
                for line_num, line_content in results:
                    highlighted = highlight_query_in_line(line_content, query, case_insensitive)
                    console.print(f"  line {line_num} :", highlighted)

                results_for_export.append({
                    "file": os.path.relpath(file_path, STATIC_FOLDER),
                    "matches": [{"line": line_num, "content": line_content} for line_num, line_content in results]
                })

        duration = round(time.time() - start_time, 2)
        stats = {
            "scanned_files": len(all_files),
            "total_size": total_size,
            "duration": duration
        }

        console.print(f"\n⏱️ Scan completed in [bold]{duration}[/bold]s | Scanned [bold]{len(all_files)}[/bold] files ({round(total_size / (1024 * 1024), 2)} MB)", style="bold cyan")

        if found:
            console.print(f"🎯 Total matches: [bold yellow]{total_matches}[/bold yellow] in [bold]{len(results_for_export)}[/bold] file(s)\n")
            if Confirm.ask("Do you want to export these results to JSON?", default=True):
                export_results_as_json(query, case_insensitive, results_for_export, stats)
        else:
            console.print("\n[!] No matches found.", style="bold yellow")

        if not Confirm.ask("\n🔁 Do you want to perform another search?", default=False):
            console.print("\n👋 Goodbye!", style="bold cyan")
            break


if __name__ == "__main__":
    search_loop()