import logging

# 创建日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建控制台处理器和文件处理器
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

# 创建格式化器并将其添加到处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将处理器添加到记录器
logger.addHandler(console_handler)
logger.addHandler(file_handler) 