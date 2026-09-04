# 📋 Terminal TODO CLI

A minimal, native terminal-based task management application written in Python. Features dynamic cross-file tracking, zero external user-facing dependencies, automated color-coded states, and safe sequential index auto-shifter logic.

---

## ✨ Features
- 🚀 **Native System Call Execution**: Run `todo` globally from any folder or path in your active shell ecosystem.
- 🎨 **Hybrid Minimalist UI**: Uses clean ANSI color mappings—active priorities remain high-contrast bold white text, completed targets melt away into dim matrix gray, and critical data deletions flash alert red.
- 📂 **Decoupled Architecture**: Real physical separation dividing data models, operational modules, and terminal argument routers.
- 🔄 **Safe Index Auto-Shifting**: Deleting inner tasks automatically shifts and numbers remaining entries from 1 upwards cleanly.

---

## 🛠️ Installation

Clone the repository down to your computer and use `pip` to link it globally across your command environment path:

```bash
# 1. Clone this repository
git clone https://github.com/Srikumar6529/terminalTODO.git
cd terminalTODO

# 2. Install the application globally in editable mode
pip3 install .
```

*Note: The `-e` flag links the package in editable mode. Any direct syntax tweaks or code revisions you write inside your source files locally will apply across your universal global workspace updates instantly without needing to reinstall.*

---

## 💻 Usage Commands

| Command | Usage Example Structure | Operational Focus |
| :--- | :--- | :--- |
| **`ls`** | `todo ls` | Renders list arrays with status blocks and color indicators. |
| **`add`** | `todo add "Record video snippet"` | Intercepts parameters and generates a new tracking object. |
| **`toggle`**| `todo toggle 2` | Flips tasks back and forth between active/complete states. |
| **`update`**| `todo update 3 "Finished editing"` | Modifies structural text targets inside storage securely. |
| **`delete`**| `todo delete 1` | Purges explicit entries and auto-aligns active id counts. |
| **`help`**  | `todo help` | Outputs basic instructions. |

