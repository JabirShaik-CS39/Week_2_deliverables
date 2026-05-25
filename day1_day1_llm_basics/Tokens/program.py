from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = "Artificial Intelligence"

encoded = tokenizer.encode(text)

decoded = tokenizer.decode(encoded)

print("Encoded:", encoded)
print("Decoded:", decoded)