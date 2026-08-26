# Llama Librarian

> A local LLM shushes your notes when they contradict each other.

Your notes become library patrons who sit in a digital reading room. When two notes argue, the librarian fines the louder one and re-shelving the conflict in a smaller font.

## Features
- Import Markdown notes and store them as library patrons
- Use embeddings to detect contradictions and overlapping claims
- Issue fines, shush levels, and shelf relocations for noisy notes
- Create a reading-room queue that surfaces unresolved debates

## Stack
- Ollama
- FastAPI
- SQLite
- HTMX

## Getting started
```
Start Ollama with a small embedding model (e.g. nomic-embed-text), run `pip install -r requirements.txt`, then start the app with `uvicorn app.main:app --reload --port 8000`.
```

---
*Farmed 🚜 by [Appshaker](https://github.com/buberlo) — shaken into existence.*
