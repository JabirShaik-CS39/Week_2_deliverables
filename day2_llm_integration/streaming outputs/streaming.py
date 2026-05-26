import ollama

stream = ollama.chat(
    model='llama3',
    messages=[
        {'role': 'user', 'content': 'Explain cloud computing.'}
    ],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)