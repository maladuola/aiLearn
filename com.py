from openai import OpenAI
import os

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'],
                base_url="https://api.siliconflow.cn/v1")

COMPLETION_MODEL = 'deepseek-ai/DeepSeek-V2.5'  # 使用最新模型
prompt = '请你用朋友的语气回复给到客户，并称他为“亲”，他的订单已经发货在路上了，预计在3天之内会送达，订单号2021AEDG，我们很抱歉因为天气的原因物流时间比原来长，感谢他选购我们的商品。'

def get_response(prompt, temperature = 1.0, stop=None):
    completiˆˆøøøøøøons = client.completions.create (
        model=COMPLETION_MODEL,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=stop,
        temperature=temperature,        
    )
    message = completions.choices[0].text
    return message

print(get_response(prompt))
