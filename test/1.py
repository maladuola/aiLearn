from openai import OpenAI
import os

# client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])  # 确保环境变量正确设置
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'],
                base_url="https://api.siliconflow.cn/v1")

COMPLETION_MODEL = 'deepseek-ai/DeepSeek-V2.5'  # 使用最新模型

prompt = """ Man Utd must win trophies, says Ten Hag ahead of League Cup final 请将上面这句话的人名提取出来，并用json的方式展示出来 """

def get_response(prompt):
    completions = client.chat.completions.create(  # 适配新版 API
        model=COMPLETION_MODEL,
        messages=[{"role": "user", "content": prompt}],  # 新版 API 使用 `messages`
        max_tokens=512,
        temperature=0.0,
    )
    message = completions.choices[0].message.content
    return message

print(get_response(prompt))