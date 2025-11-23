from src.logger import logger
import os
logger.info("Welcome to our custom logging")

if __name__ == "__main__":
    logger.info("App started successfully")
    path = ["data1","data2","data3"]
    for path in path:
        os.makedirs(path)

