🔍FastFinder
**FastFinder** is a fast, lightweight and user-friendly CLI tool to search for text across **multiple source code files**, **folders**, and **directory trees**.  
It supports **regex**, **highlighted results**, **progress bars**, **file stats**, and **JSON export**.


## 🇬🇧 English

### ✨ Features

- 🔍 Search through entire folder hierarchies
- 💡 Regex search support with smart highlights
- 📂 Filters by extension (`.py`, `.js`, `.php`, `.html`, etc.)
- 📊 Progress bar + performance statistics
- 📦 Export results as a clean JSON file
- 🤖 Interactive mode and CLI arguments



### 🚀 Usage
```
python fastfinder.py
```

Then follow the interactive prompts to:

- Enter your query or a regex (`idk"<your_regex>"`)
- Choose case sensitivity
- Export results if desired

---

### 🛠 CLI Arguments

```
--query        Text or regex to search
--export       Export results to JSON automatically
--no-banner    Disable the banner
```

Example:

```
python fastfinder.py --query 'idk"\$[a-zA-Z_][a-zA-Z0-9_]*"' --export --no-banner
```

---

## 🇫🇷 Français

### ✨ Fonctionnalités

- 🔍 Recherche dans plusieurs fichiers, dossiers et sous-dossiers
- 🧠 Prise en charge des expressions régulières avec surlignage
- 📂 Filtres par extensions de fichiers courants (`.py`, `.js`, `.php`, etc.)
- 📊 Statistiques de performance + barre de progression
- 📦 Exportation des résultats au format JSON
- 🧑‍💻 Mode interactif et support ligne de commande

---

### 🚀 Utilisation

```
python fastfinder.py
```

Suivez ensuite les instructions pour :

- Entrer votre mot ou expression (ou une regex : `idk"<votre_regex>"`)
- Choisir la sensibilité à la casse
- Exporter les résultats si souhaité

---

### 🛠 Options CLI

```bash
--query        Mot ou regex à chercher
--export       Exporte les résultats en JSON automatiquement
--no-banner    Désactive l'affichage du logo
```

Exemple :

```
python fastfinder.py --query "idk\"eval\(" --export --no-banner
```

---

### 📁 Default folders

- **static/** : folder to scan
- **export/** : folder for results

---

### 🤝 Credits

Developed by: **Heresalord**, **durockkoumassi**, and **Alice QDT**  
Project: **KMS STUDIO**

--
