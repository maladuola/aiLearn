import requests
from logger_config import logging

class HttpPostClient:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def send_post_request(self):
        try:
            response = requests.post(self.url, json=self.data)
            response.raise_for_status()  # 检查请求是否成功
            logging.info("Response Status Code: %s", response.status_code)
            logging.info("Response Body: %s", response.json())
        except requests.exceptions.RequestException as e:
            logging.error("HTTP Request failed: %s", e)

# 示例用法
if __name__ == "__main__":
    url = "https://example.com/api"
    data = {"key1": "value1", "key2": "value2"}
    client = HttpPostClient(url, data)
    client.send_post_request() 