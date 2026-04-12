
from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)


def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful SaaS assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("❌ ERROR:", e)
        return f"Error: {str(e)}"
