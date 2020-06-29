import requests
import sys

if len(sys.argv) - 1 > 1:
    # Initializing variables
    counter = 0

    # Opening file
    f = open(sys.argv[2], 'r')

    # Looking for available pages inside the wordlist
    for i in f:
        t = i
        i = t[:-1]
        url = 'https://{}{}'.format(sys.argv[1],i)
        try:
            request = requests.get(url)
            if request.status_code == 200:
                print('Directory {} exists ({})'.format(url,request.status_code))
                counter = counter + 1
            elif request.status_code == 301 or request.status_code == 307:
                print('Directory {} was moved ({})'.format(url,request.status_code))
                counter = counter + 1
            elif request.status_code == 401 or request.status_code == 403:
                print('Directory {} exists, but you cannot access ({})'.format(url,request.status_code))
                counter = counter + 1
        except:
            counter = counter
    print('The wordlist has {} valid directories'.format(counter))
else: 
    print()
    print('                    DirExceed - v1.0                     ')
    print('                Created by brenu (Exceed)                ')
    print()
    print('                          Usage                          ')
    print('->    python3 direxceed.py www.example.com file.txt    <-')