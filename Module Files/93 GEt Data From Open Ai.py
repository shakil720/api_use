import openai

openai.api_key = "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"
prompt = input("Enter prompt: ")
response = completions.create(
    model="gpt-3.5-turbo",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

text = response.get("choices")[0].get("text")
print(text)








# From gemini

# from openai import OpenAI
# import os
#
# # Better to use an environment variable: os.environ.get("OPENAI_API_KEY")
# # For now, replace 'YOUR_NEW_KEY' with a freshly generated key
# client = OpenAI(api_key="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")
#
# prompt = input("Enter prompt: ")
#
# # Use 'chat.completions' instead of 'Completion'
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo", # Use modern models
#     messages=[
#         {"role": "user", "content": prompt}
#     ],
#     temperature=0.7,
#     max_tokens=256
# )
#
# # Printing the content specifically
# print(response.choices[0].message.content)