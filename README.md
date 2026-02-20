# 🎭 Alice Markov: A Memory-Augmented N-Gram Bot
> **A high-performance text generation engine built from first principles. Zero AI APIs. Pure probability.**

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Optimized-success)]()
[![License](https://img.shields.io/badge/License-MIT-orange)]()

---

## 🏗️ Architectural Overview
This repository implements a **Second-Order Markov Chain** chatbot, engineered without high-level NLP libraries (no NLTK, SpaCy, or OpenAI). It demonstrates the power of **Stochastic Mapping**—predicting the next token based on a window of preceding states.

### 🧠 The "Senior Dev" Advantage
Unlike basic Markov generators, this implementation features a **Contextual Memory Buffer**. By utilizing a `collections.deque` with a sliding window, the bot "listens" to the last 5 user inputs to anchor its responses in the current topic.

---

## ✨ Key Features
* **🥈 Dual-Order Engine**: Uses both 1st-order and 2nd-order transition maps for superior linguistic coherence.
* **🧠 Short-Term Memory**: A 5-message context window that dynamically influences seed-word selection.
* **🧹 Robust Tokenization**: Custom Regex-based pipeline `[\w']+|[.!?]` that preserves contractions while isolating punctuation.
* **⚡ Optimized Lookups**: Dictionary-based state storage providing **O(1) time complexity** for next-token prediction.

---

## 🛠️ Technical Stack
* **Runtime**: Python 3.11+
* **Probabilistic Selection**: `NumPy` (utilizing `np.random.choice` for weighted distribution)
* **Data Persistence**: Python Native Dictionaries (Hash Maps)
* **Memory Management**: `collections.deque` (Optimized for $O(1)$ append/pop operations)

---

## 📊 How It Works (The Logic)



1. **State Construction**: During the `train` phase, the bot maps word pairs (states) to an array of potential successors based on the training corpus (`alice.txt`).
2. **Contextual Seeding**: The generator scans the **Memory Buffer** for the most recent word that exists in the known state-space.
3. **Probability Walking**: The bot "walks" the chain, using weighted selection to pick the next word until it hits a termination token (`.`, `!`, or `?`).

---

## 📥 Installation & Setup

### 1. Initialize Environment
```bash
git clone [https://github.com/jaweriashakoor/python-markov-chatbot.git](https://github.com/jaweriashakoor/python-markov-chatbot.git)
cd python-markov-chatbot
pip install -r requirements.txt
