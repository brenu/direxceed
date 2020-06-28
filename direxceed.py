import requests

# Initializing variables
counter = 0

# Opening file
f = open('test.txt', 'r')

# Looking for available pages inside the wordlist
for i in f:
    t = i
    i = t[:-1]
    url = 'https://www.google.com{}'.format(i)
    try:
        request = requests.get(url)
        if request.status_code == 200:
            print('Directory {} exists'.format(url))
            counter = counter + 1
    except:
        counter = counter

print('The wordlist has {} valid directories'.format(counter))