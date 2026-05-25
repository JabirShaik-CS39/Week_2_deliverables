from google import genai

API_KEY = "YOUR_API_KEY"


def create_client():
    return genai.Client(api_key=API_KEY)


def ask_gemma(question):
    client = create_client()

    response = client.models.generate_content(
        model="gemma-4-26b-a4b-it",
        contents=question
    )

    return response.text


answer = ask_gemma(
    "Explain API wrappers in simple words."
)

print(answer)