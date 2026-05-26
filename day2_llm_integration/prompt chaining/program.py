from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

# Step 1
response1 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Give 3 startup ideas in AI."}
    ]
)

ideas = response1.choices[0].message.content

print("Generated Ideas:")
print(ideas)

# Step 2
response2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f"Create a business plan for this idea:\n{ideas}"}
    ]
)

print("\nBusiness Plan:")
print(response2.choices[0].message.content)