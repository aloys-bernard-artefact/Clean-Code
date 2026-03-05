from loguru import logger
import random


logger.debug("This code in run every time we import the file :")
logger.info(" Importing this file.")
logger.error(f" {__name__=}")


def dice():
    return random.randint(1, 6)



if __name__ == "__main__":
    logger.info("This code is run only when we run this file directly :")
    logger.info("Rolling the dice : " + str(dice()))
    logger.info(f" {__name__=}")
