import logging

logging.basicConfig(filename = 'Week4/W4Day1/result_sample_logFile.py',
               level = logging.DEBUG,
               format = '%(asctime)s - %(levelname)s - %(message)s')


logging.debug("This is a debug message")
logging.info("This is an Info message")
logging.warning("This is a Warning message")
logging.error("This is an Error message")
logging.critical("This is a Critical message")

print("Log printed Sucessfully")
print('Log written in result_sample_logFile.py')

