import os
import time
from tqdm import tqdm
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime

def print_banner():
    banner = """
 ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░ ░░░ ░ ░    ░   ░ ░   ░         ░     ░░   ░ 
 ░  ░  ░   ░              ░             ░  ░   ░     

                    BY ESKA ( searcher.crx )
"""
    print(colored(banner, "red"))

def get_inputs():
    site = input(colored("[?] Site ciblé: ", "red")).strip()
    print(colored("[?] Drag and Drop (url:mail:pass):", "red"))
    combo_file = input(">>> ").strip('"')
    if not os.path.exists(combo_file):
        raise FileNotFoundError(f"Fichier introuvable: {combo_file}")
    return site, combo_file

def process_combo(site_filter, file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    total = len(lines)
    matches = []
    start_time = time.time()

    print(colored(f"[*] Début de l’analyse ({total} lignes)...", "cyan"))
    for i, line in enumerate(tqdm(lines, desc="Analyse", unit="ligne")):
        if site_filter in line:
            try:
                parts = line.strip().split(":")
                if len(parts) >= 2:
                    mail = parts[-2]
                    passwd = parts[-1]
                    match = f"{mail}:{passwd}"
                    matches.append(match)
                    print(colored(f"[+] {match}", "green"))
            except Exception as e:
                print(colored(f"[!] Erreur ligne {i}: {e}", "red"))

    duration = time.time() - start_time
    return matches, total, duration

def save_results(matches, site_filter):
    if not os.path.exists("results"):
        os.mkdir("results")
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{site_filter.replace('.', '_')}_{now}.txt"
    filepath = "results/" + filename
    with open(filepath, "w") as f:
        f.write("\n".join(matches))
    return filepath

def show_summary(matches, total, duration):
    print(colored("\nRésumé du scan", "magenta"))
    print(colored(f"Total lines    : {total}", "cyan"))
    print(colored(f"Hits           : {len(matches)}", "green"))
    print(colored(f"Bad            : {total - len(matches)}", "yellow"))
    print(colored(f"Durée          : {duration:.2f} secondes", "blue"))

def main():
    try:
        print_banner()
        site, combo_path = get_inputs()
        matches, total, duration = process_combo(site, combo_path)
        output_file = save_results(matches, site)
        print(colored(f"\n[*] Résultats sauvegardés dans: {output_file}", "cyan"))
        show_summary(matches, total, duration)
    except Exception as e:
        print(colored(f"[!] Erreur: {e}", "red"))

if __name__ == "__main__":
    main()


