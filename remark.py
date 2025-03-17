from openai import OpenAI
import numpy as np
import os

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'],
                base_url="https://api.siliconflow.cn/v1")

EMBEDDING_MODEL = 'netease-youdao/bce-embedding-base_v1'  # 使用最新模型

def get_embedding(text, model=EMBEDDING_MODEL):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def cosine_similarity(vector_a, vector_b):
  dot_product = np.dot(vector_a, vector_b)
  norm_a = np.linalg.norm(vector_a)
  norm_b = np.linalg.norm(vector_b)
  epsilon = 1e-10
  cosine_similarity = dot_product / (norm_a * norm_b + epsilon)
  return cosine_similarity

positive_review = get_embedding("好评")
negative_review = get_embedding("差评")

positive_example = get_embedding("买的银色版真的很好看，一天就到了，晚上就开始拿起来完系统很丝滑流畅，做工扎实，手感细腻，很精致哦苹果一如既往的好品质")
negative_example = get_embedding("随意降价，不予价保，服务态度差")

def get_score(sample_embedding):
  return cosine_similarity(sample_embedding, positive_review) - cosine_similarity(sample_embedding, negative_review)

good_restraurant = get_embedding("这家餐馆非常好吃")
bad_restraurant = get_embedding("这家餐馆太糟糕了")

good_score = get_score(good_restraurant)
bad_score = get_score(bad_restraurant)
print("好评餐馆的评分 : %f" % (good_score))
print("差评餐馆的评分 : %f" % (bad_score))


