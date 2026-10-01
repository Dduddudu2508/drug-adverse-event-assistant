# Drug Adverse Event Research Assistant

A RAG pipeline for querying drug safety and adverse effect information using LLMs and biomedical literature.

## Milestone 1 (Complete)
- Claude API integration with structured JSON output
- Clinical pharmacovigilance prompt design
- Graceful JSON parsing with error handling

## Milestone 2 (In Progress)
- Document ingestion pipeline using FDA FAERS and PubMed data
- Vector embeddings with ChromaDB
- Retrieval-augmented generation

## Setup
```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"
python3 adverse_effects.py
```
