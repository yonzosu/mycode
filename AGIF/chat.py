import openai 

openai.api_key = 'sk-'

response = openai.ChatCompletion.create(
    model = "gpt-4",
    message = [
        {"role": "system", "content": "你是一个帮助用户的助手。"},
        {"role": "user", "content": "你好，请帮我解释一下量子物理。"},
    ]
)

print(response.choices[0].message['content'])