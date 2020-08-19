import requests as rq 
import sys
import re


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

def options(options):
    for opt, arg in options.items():
        print(opt, arg)

        if opt == '-t':
            #check the connection n times
            global url
            check_connection(url, int(arg))

            

def check_connection(url, n=1):
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
            
    else:
        print("you have to supply a URL.")  

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
url = get_url(args)

optagrs = {}
for i in range(len(opts)):
    optagrs[opts[i]] = args[i]
    

   

print ("URL:\t", url)

options(optagrs)
check_connection(url)