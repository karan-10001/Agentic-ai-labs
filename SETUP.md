# Agentic AI Labs - Initial Setup (Google Gemini SDK)

## Goal

Set up a Python learning environment using:

- uv (Package Manager)
- Jupyter Notebook
- Google Gemini SDK
- VS Code
- Environment Variables (.env)

---

# Step 1: Verify uv Installation

```powershell
uv --version
```

✅ Verifies that uv is installed and available in your terminal.

---

# Step 2: Navigate to Project Folder

```powershell
cd path\to\agentic-ai-labs
```

✅ Moves into your project directory.

---

# Step 3: Initialize the Project

```powershell
uv init
```

✅ Creates:

- pyproject.toml
- README.md

These files are used by uv to manage the project.

---

# Step 4: Create Virtual Environment

```powershell
uv venv
```

✅ Creates:

```text
.venv/
```

This is an isolated Python environment for your project.

---

# Step 5: Install Required Packages

```powershell
uv add google-genai python-dotenv jupyter ipykernel
```

✅ Installs:

### google-genai

Google Gemini SDK.

Used for:

```python
from google import genai
```

### python-dotenv

Loads environment variables from a .env file.

Used for:

```python
from dotenv import load_dotenv
```

### jupyter

Provides notebook support.

Used for:

```text
.ipynb files
```

### ipykernel

Allows VS Code and Jupyter to use the project's virtual environment as a notebook kernel.

---

# Step 6: Verify Installed Packages

```powershell
uv pip list
```

✅ Shows all installed packages.

Expected packages:

```text
google-genai
python-dotenv
jupyter
ipykernel
```

---

# Step 7: Create Project Folders

```powershell
mkdir notebooks
mkdir examples
mkdir data
```

✅ Creates folders for learning and experimentation.

Expected structure:

```text
agentic-ai-labs/
│
├── notebooks/
├── examples/
├── data/
│
├── .venv/
├── pyproject.toml
└── uv.lock
```

---

# Step 8: Create Environment File

Create:

```text
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

✅ Keeps API keys outside source code.

Never commit this file to GitHub.

---

# Step 9: Select Python Interpreter in VS Code

Open Command Palette:

```text
Ctrl + Shift + P
```

Search:

```text
Python: Select Interpreter
```

Select:

```text
.venv
```

✅ Ensures VS Code uses the project virtual environment.

---

# Step 10: Create First Notebook

Create:

```text
notebooks/01_gemini_basics.ipynb
```

---

# Notebook Cell 1

Load Environment Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key Loaded Successfully")
```

---

# Notebook Cell 2

Create Gemini Client

```python
from google import genai

client = genai.Client(
    api_key=api_key
)

print("Gemini Client Created")
```

---

# Notebook Cell 3

Call Gemini

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is Selenium?"
)

print(response.text)
```

✅ If successful, Gemini returns a response.

---

# Useful uv Commands

## Add New Package

```powershell
uv add pandas
```

Installs a new dependency.

---

## Remove Package

```powershell
uv remove pandas
```

Removes a dependency.

---

## Show Installed Packages

```powershell
uv pip list
```

Lists installed packages.

---

## Run a Python File

```powershell
uv run python examples\example.py
```

Runs a Python script using the project's virtual environment.

---

## Launch Jupyter

```powershell
uv run jupyter notebook
```

Starts Jupyter Notebook.

---

## Sync Environment

```powershell
uv sync
```

Recreates or updates the environment from:

```text
pyproject.toml
uv.lock
```

Useful when cloning a project from GitHub.

---

# Current Learning Scope

✅ uv

✅ Virtual Environment

✅ Jupyter Notebook

✅ Python-dotenv

✅ Google Gemini SDK

✅ Prompt → Response

---

# Future Learning Path

- OpenAI SDK
- Anthropic SDK
- Ollama
- Prompt Engineering
- Structured Output
- Function Calling
- LangChain
- LangGraph
- MCP
- Agentic AI