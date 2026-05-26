import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {'role': 'user', 'content': 'Tell me a fun fact about space.'}
    ]
)

answer = response['message']['content']

print("AI Response:")
print(answer)