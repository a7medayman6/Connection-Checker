import sys
from methods import *

    

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
url = get_url(args)

optagrs = {}
for i in range(len(opts)):
    if(opts[i] == '--help'):
        optagrs[opts[i]] = ""
    elif(i <= len(args)):
        optagrs[opts[i]] = args[i]
        
    



options(optagrs, url)