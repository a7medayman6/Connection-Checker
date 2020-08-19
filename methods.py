import requests as rq
import re
import time 

def is_url(arg):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return (re.match(regex, arg) is not None)

def get_url(args):
    for arg in args:
        if is_url(arg):
            args.remove(arg)
            return arg
    return None        

def help_menu():
    print("\nUSAGE: $ python3 ping.py [URL] -[Option] [argument]\n")
    print("\t\t________OPTIONS________")
    print("-t [times] number of times to check the connection, default value 1.")
    print("-d [seconds] number of seconds to delay between each time default value 0.")
    print('-help displays the help menu.')


    print("\nEXAMPLE: $ python3 ping.py https://www.google.com -t 4 -d 2")

def options(options, url):
    n = 1
    delay = 0
    help = False
    for opt, arg in options.items():
        
        if opt == '-t':
            #check the connection n times
            n = int(arg)-1
        if opt == '-d':
            delay = int(arg)
        if opt == '--help':
            help_menu()
            help = True
    if not help:
        print ("URL:\t", url)
        check_connection(url, n, delay)
def check_connection(url, n=1, delay=0):
    if url is not None:
        for i in range(n):
            try:
                req = rq.get(url)   
                code = req.status_code         
                print("Status code:", code)
                if code == 200:
                    print(url + " is up and running.")
                else:
                    print(url + " is not up.")    
            except Exception as ex:
                print("ERROR!")
            if i < range(n):
                time.sleep(delay)    
            
    else:
        print("WRONG URL.")
        print("USAGE: $ python3 ping.py [URL] -[Option] [argument]")
        