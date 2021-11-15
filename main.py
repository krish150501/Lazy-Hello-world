from os import system,name
import time
n='hello world'
res='                        '
for i in range(len(n)):
    for j in range(97,124):
        if(j==123):
            j=32
        res=res[:i]+chr(j)+res[i+1:]
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        print(res)
        if(n[i]==chr(j)):
            break
        
        time.sleep(1)
        
