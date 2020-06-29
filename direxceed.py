import requests
import sys

# Initializing variables
counter = 0

# Opening file
f = open('test.txt', 'r')

# Looking for available pages inside the wordlist
if len(sys.argv) - 1 > 1:
    for i in f:
        t = i
        i = t[:-1]
        url = 'https://{}{}'.format(sys.argv[1],i)
        try:
            request = requests.get(url)
            if request.status_code == 200:
                print('Directory {} exists'.format(url))
                counter = counter + 1
        except:
            counter = counter
    print('The wordlist has {} valid directories'.format(counter))
else: 
    print()
    print('                        DirExceed                        ')
    print('                 Created by brenu (Exceed)               ')
    print()
    print('                         Usage                           ')
    print('--------- python3 direxceed.py www.example.com ----------')