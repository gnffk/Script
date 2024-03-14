import random
import time

random.seed(time.time())

RandomUppercase = chr(random.randint(65,90))
print("대문자: ", RandomUppercase)