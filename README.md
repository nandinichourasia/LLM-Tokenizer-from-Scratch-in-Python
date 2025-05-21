# How do we prepare input text for training LLMs?
Step1- Splitting the text into individual word and subword.<br>
Step2- Convert Tokens(Individual word) into Token IDs.<br>
Step3- Encode token IDs into Vector Representations.

# 📘 LLM Tokenizer from Scratch

# What Is a Tokenizer?
-A tokenizer converts raw text into smaller units called tokens, which are then mapped to numerical IDs. This process enables models to process and understand text data effectively.
A simple Python implementation of a Large Language Model (LLM) tokenizer built from scratch. This project is intended for learning purposes and demonstrates how tokenization works under the hood in modern NLP systems like BERT and GPT.

# 🚀 Features
Custom vocabulary building.<br>
Basic tokenization.<br>
Encoding text to tokens.<br>
Decoding tokens back to text.<br>
Minimal and educational Python code.

# 📖 How it Works
This tokenizer uses a simple approach by first building a vocabulary from the input data. It then tokenizes input text based on this vocabulary and provides both encode and decode functionalities. It's a simplified version, inspired by how tokenizers like BPE or WordPiece work.
