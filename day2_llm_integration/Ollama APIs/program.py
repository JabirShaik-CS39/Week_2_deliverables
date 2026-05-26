from openai import OpenAI

# Create client
client = OpenAI(api_key="YOUR_API_KEY")

# Send request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain Machine Learning in simple terms."}
    ]
)
# Print response
print(response.choices[0].message.content)
