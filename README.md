# Argon-Opus Bridge 🚀

<img width="173" height="240" alt="Screenshot 2026-10-17 165842" src="https://github.com/user-attachments/assets/38cf9c8e-54a1-48e8-8922-1ae2ad25a6ae" />

**Argon-Opus Bridge** is an advanced, dual-stage AI engineering pipeline designed to dramatically reduce API context costs while maximizing software architecture fidelity. It orchestrates two of the industry's most powerful frontier models: **Gemini 4 Argon** and **Claude Opus 5.5**.

---

## 🥊 The Frontier Clash: Claude Opus 5.5 vs. Gemini 4 Argon

<img width="1000" height="524" alt="image" src="https://github.com/user-attachments/assets/a7c98931-9f3b-4ad1-9eb0-0fa716672d64" />

The AI development ecosystem has entered a definitive era of specialization. Rather than a simple race of one model beating another, **Claude Opus 5.5** and **Gemini 4 Argon** represent two distinct, elite engineering philosophies:

*   **Gemini 4 Argon** is Built for Scale. Google engineered the Argon architecture around aggressive long-horizon workflows, spatial 3D reasoning, and immense token generation performance at a highly competitive price point.
*   **Claude Opus 5.5** is Built for Precision. Anthropic’s flagship model leads the industry in multi-step task execution, complex code refactoring, and granular edge-case detection through its advanced Adaptive Thinking mode.

This repository exists because choosing between them is a false dichotomy. By building a functional bridge, developers can harness the strengths of both models simultaneously.

---

## 💡 The Architectural Concept

Deploying ultra-high-tier frontier models like Claude Opus 5.5 for raw, iterative prototyping can drain token budgets rapidly. This framework introduces a hybrid approach:

1. **Phase 1 (The Blueprint):** **Gemini 4 Argon** is utilized first to ingest massive prompt requirements or legacy codebases. It leverages its highly competitive cost-per-token framework and advanced planning layers to assemble a rapid, fully functional raw architectural blueprint.
2. **Phase 2 (The Refinement):** **Claude Opus 5.5** takes over the generated blueprint. Using its state-of-the-art **Adaptive Thinking Mode**, it analyzes structural execution paths, resolves subtle logic bugs, injects comprehensive error handling, and refines the codebase into production-ready software.

---

## ⚖️ Core Synergy Matrix

| Capability Focus | Gemini 4 Argon 🧪 | Claude Opus 5.5 🎨 |
| :--- | :--- | :--- |
| **Primary Strength** | Raw spatial logic, infinite output scaling, and massive context windows. | Hyper-refined code syntax, logical depth, and flawless edge-case handling. |
| **Optimal Pipeline Phase** | **Upstream Execution:** Ingests massive specs or codebases rapidly to emit a functional structural blueprint. | **Downstream Execution:** Refactored architecture polish via Adaptive Thinking parameters. |
| **Token Economy** | Highly competitive cost structure optimized for long-horizon background workflows. | High-tier precision pricing tailored for meticulous production delivery. |

### Why This Combination Wins:
- **Cost Efficiency:** Running long-horizon iteration rounds solely on Opus 5.5 quickly depletes dev budgets. By routing the initial heavy lifting to Gemini 4 Argon, the pipeline creates highly accurate architectural layouts for fractions of a cent.
- **Syntactical Perfection:** While Argon is fast and expansive, Claude Opus 5.5 excels at cleaning up loose ends, removing code clutter, and preparing structural code to withstand enterprise production environments.

---

## 🛠️ Project Structure

The codebase is engineered to run locally on your machine with minimal overhead:

```text
argon-opus-bridge/
├── .env.example         # Template for required environment variables
├── config.py            # Validation and runtime configuration system
├── core_pipeline.py     # Execution engine orchestrating Google & Anthropic APIs
├── utils.py             # File I/O helpers and interactive CLI styling
├── main.py              # CLI entry point to accept user arguments
└── requirements.txt     # Global pipeline package dependencies
```

---

## ⚙️ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com
cd argon-opus-bridge
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Credentials
Copy the example environment file and open it to insert your private API keys:
```bash
cp .env.example .env
```
Inside your `.env` file:
```env
GEMINI_API_KEY=AIzaSyYourGeminiKeyHere
ANTHROPIC_API_KEY=sk-ant-YourAnthropicKeyHere
THINKING_EFFORT=HIGH
```

---

## 🚀 Usage Guide

Run the pipeline from your local terminal. You can define a new software system from scratch or supply a legacy file as architectural context.

### Example A: Generating code from scratch
```bash
python main.py \
  --prompt "An asynchronous web scraper in Python with automatic retry limits and structured CSV export" \
  --output "./output/scraper.py"
```

### Example B: Refactoring/Polishing an existing legacy file
```bash
python main.py \
  --input "./legacy_code/old_script.py" \
  --prompt "Refactor this legacy script into an object-oriented design and integrate type hinting" \
  --output "./output/modern_script.py"
```

---

## 📊 Configuration Parameters

You can toggle the `THINKING_EFFORT` variable inside your `.env` file to scale operational depth:

| Effort Level | Gemini 4 Argon Budget | Claude Opus 5.5 Mode | Best For |
| :--- | :--- | :--- | :--- |
| **`LOW`** | 1024 Reasoning Tokens | Standard Execution | Simple scripts, quick UI changes, bug patching |
| **`HIGH`** | 2048 Reasoning Tokens | Adaptive Thinking (High) | Complex system refactoring, full microservices |

---
