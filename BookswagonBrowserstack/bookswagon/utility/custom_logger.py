import logging

class CustomLogger():
    @staticmethod
    def log_utility():
        logging.basicConfig(filename="C:\\Users\\User\\Desktop\\python\\Bookswagon\\bookswagon\\logs\\log_file.log",format='%(asctime)s: %(levelname)s: %(message)s\n\r',
        datefmt='%m/%d/%Y %I:%M:%S %p',filemode='a')
        #Creating an object
        logger=logging.getLogger()
        #Setting the threshold of logger to DEBUG
        logger.setLevel(logging.INFO)
        return logger

       