import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

examples = [
    "Hello, world!",
    "This is a test sentence.",
    "Tokenization is the process of converting text into tokens.",
    "The quick brown fox jumps over the lazy dog.",
    "Python is a popular programming language.",
    "Jambo, dunia!",
    "Jana usiku",
    "CBK",
    "KRA",
    "M-Pesa",
    "The Central Bank of Kenya",
]


for text in examples:
    tokens = enc.encode(text)
    pieces = [enc.decode([token]) for token in tokens]
    print(f"{text!r:45} -> {len(tokens):2} tokens -> {pieces}")


# sanity check the ~4 chars per token rule of thumb
long_text = "a" * 400

print(f"\n400 chars -> {len(enc.encode(long_text))} tokens")
