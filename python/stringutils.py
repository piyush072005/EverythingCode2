def reverse_words(s):
    return " ".join(s.split()[::-1])

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

def is_palindrome(s):
    clean = "".join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

def word_frequency(text):
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}

if __name__ == "__main__":
    text = "Hello World Hello"
    print(f"Reverse words: {reverse_words(text)}")
    print(f"Vowels: {count_vowels(text)}")
    print(f"Palindrome 'racecar': {is_palindrome('racecar')}")
    print(f"Word frequency: {word_frequency(text)}")