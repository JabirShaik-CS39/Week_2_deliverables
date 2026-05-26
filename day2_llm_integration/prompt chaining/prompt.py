import ollama

# First prompt
response1 = ollama.chat(
    model='llama3',
    messages=[
        {'role': 'user', 'content': 'Give 5 project ideas using Python.'}
    ]
)

ideas = response1['message']['content']

print("Project Ideas:")
print(ideas)

# Second prompt
response2 = ollama.chat(
    model='llama3',
    messages=[
        {
            'role': 'user',
            'content': f'Create implementation steps for:\n{ideas}'
        }
    ]
)

print("\nImplementation Plan:")
print(response2['message']['content'])