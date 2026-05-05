import os
from openai import OpenAI
from dotenv import load_dotenv
 
# 加载环境变量
load_dotenv()
 
# 初始化OpenAI客户端
client = OpenAI(api_key=os.getenv("sk-"))
 
# 测试API调用
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Say this is a test"}
    ],
    model="gpt-3.5-turbo"
)
 
print(chat_completion.choices[0].message.content)