
# Text Analysis Tool

import re
import matplotlib.pyplot as plt
from collections import Counter
from typing import List, Dict
import pyinputplus as pyip

# ----------------------------
# Text Processing Functions
# ----------------------------

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def tokenize_words(cleaned_text: str) -> List[str]:
    return cleaned_text.split()

def tokenize_sentences(original_text: str) -> List[str]:
    sentences = re.split(r'[.!?]+', original_text)
    return [s.strip() for s in sentences if s.strip()]

# ----------------------------
# Analysis Functions
# ----------------------------

def get_word_frequency(words: List[str]) -> Dict[str, int]:
    return dict(Counter(words))

def calculate_avg_word_length(words: List[str]) -> float:
    if not words:
        return 0.0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# ----------------------------
# Output Functions
# ----------------------------

def display_stats(words: List[str], sentences: List[str], word_freqs: Dict[str, int], avg_length: float) -> None:
    print("\n--- Text Statistics ---")
    print(f"Total words: {len(words)}")
    print(f"Total sentences: {len(sentences)}")
    print(f"Average word length: {avg_length:.2f}")
    print("\nTop 5 most frequent words:")
    top_words = Counter(word_freqs).most_common(5)
    for word, freq in top_words:
        print(f"{word}: {freq}")

def generate_bar_chart(word_freqs: Dict[str, int], top_n: int = 5) -> None:
    top_words = Counter(word_freqs).most_common(top_n)
    if not top_words:
        print("No data to display in chart.")
        return
    words, freqs = zip(*top_words)
    plt.figure(figsize=(8, 5))
    plt.bar(words, freqs)
    plt.title(f"Top {top_n} Most Frequent Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# ----------------------------
# Menu and Control Logic
# ----------------------------

def run_text_analysis_tool():
    raw_text = ""
    cleaned = []
    words = []
    sentences = []
    word_freqs = {}
    avg_word_len = 0.0

    while True:
        choice = pyip.inputMenu([
            "Enter Text",
            "View Statistics",
            "Generate Chart",
            "Exit"
        ], prompt="\nChoose an option:\n", numbered=True)

        if choice == "Enter Text":
            raw_text = pyip.inputStr(prompt="\nPlease enter the text you want to analyze:\n")
            cleaned = clean_text(raw_text)
            words = tokenize_words(cleaned)
            sentences = tokenize_sentences(raw_text)
            word_freqs = get_word_frequency(words)
            avg_word_len = calculate_avg_word_length(words)
            print("\nText successfully analyzed!")

        elif choice == "View Statistics":
            if not words:
                print("\nNo text has been analyzed yet. Please enter text first.")
            else:
                display_stats(words, sentences, word_freqs, avg_word_len)

        elif choice == "Generate Chart":
            if not word_freqs:
                print("\nNo text has been analyzed yet. Please enter text first.")
            else:
                generate_bar_chart(word_freqs)

        elif choice == "Exit":
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    run_text_analysis_tool()
