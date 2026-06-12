# LLM Tokenization

A personal study repository documenting my hands-on journey into understanding how large language models actually work under the hood — starting from the very basics of how text gets broken into tokens, all the way to building LLM-powered tools.

I am a business process automation developer with years of experience in IT, and I got tired of using AI tools without truly understanding what is happening inside them. This repo is me fixing that, out of curiousity.

---

## Why I Built This

I have been working with RPA and automation for years. LLMs started showing up everywhere in that space and I kept integrating them without really knowing what a token was, why context windows have limits, or why some prompts work and others do not.

This repository is my attempt to go from "I use AI" to "I understand AI" — one day at a time, in plain Python, on a regular laptop with no GPU.

---

## My Setup

- Windows 11, Ryzen 5, 16GB RAM
- Python 3.14
- No GPU, no cloud compute, no paid APIs for the core lessons
- VS Code + Git Bash

Everything in this repo is designed to run on a normal machine. If it needs heavy compute I will note it clearly.

---

---

---

## Key Things I Learned So Far

**Tokens are not words.**
The word `unhappiness` becomes three separate tokens: `un`, `h`, `appiness`. The LLM never sees whole words — it sees chunks determined by frequency patterns in training data. I built this from scratch and watching it discover word roots and suffixes on its own was genuinely surprising.

**Token IDs carry no meaning on their own.**
`cat` might be ID 4964 and `dog` might be ID 5679. Those numbers are just locker assignments. The gap between them means nothing. This is why embeddings exist — to give words a real mathematical address that reflects their actual meaning.

**BPE is elegant.**
Byte Pair Encoding starts with individual characters and keeps merging the most common neighbouring pairs until it has a vocabulary of 100,000 tokens. No human labels anything. The structure emerges from counting. Same algorithm powers GPT-4 and Claude.

---

## Background

Currently I am working as a Business Process Automation Developer in the Philippines, transitioning into AI Automation Engineering and this repository is part of that transition.
My background is in Blue Prism RPA, NestJS, FastAPI, and React Native — mostly enterprise and LGU-facing systems.

---

## Notes

- Code is intentionally simple and over-commented. This is a learning repo, not a production library.

---
