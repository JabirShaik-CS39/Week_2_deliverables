import requests

url = "http://localhost:11434/api/generate"

name = input("Enter Name: ")
skills = input("Enter Skills: ")
experience = input("Enter Experience: ")
education = input("Enter Education: ")

resume = f"""
Name: {name}

Skills:
{skills}

Experience:
{experience}

Education:
{education}
"""

prompt = f"""
Analyze this resume for a Python Backend Developer role.

Give:
- Matching skills
- Missing skills
- Experience evaluation
- Final recommendation

Resume:
{resume}
"""

payload = {
    "model": "gemma3:1b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload)

data = response.json()

print("\nResume Feedback:\n")
print(data["response"])