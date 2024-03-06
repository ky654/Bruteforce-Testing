import threading
import requests
import logging
import logging.config
import sys

# log file setting
logging.basicConfig(filename="6digit_pass.txt", filemode='w', format='%(message)s')

for i in range(0, 1000000):
    logging.error("{:06d}".format(i))
    print("{:06d}".format(i))