from utils.constmap import *
from utils.pipeline import pipeline_one_cate
import time







if __name__ == "__main__":
    for category in categories:
        print(f"===================== {category}======================")
        pipeline_one_cate(category)
        time.sleep(5)