#!/bin/bash/python3

PASSWORDS = {'email':'jonnyfox@gmail.com',
            'blog':'ikashyap@gmail.com',
            'bell':'veryverydynamicmanagement'}


import sys,pyperclip

if len(sys.argv) < 2:
    print('Usages : python3 passwordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   #first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+' copied to clipboard.')
else:
    print('There is no account named ' +account)
