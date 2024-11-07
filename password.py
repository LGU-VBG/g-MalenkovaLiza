import re


password =  input("Enter password:" )


def check_password(password):
   
    if len (password) >8 and not re.search('a-z', password) and not re.search('A-Z', password) and not re.search('/d', password) and not re.search('/s', password):
        return print (f"Введенный пороль {password} надежен")
    
    else:
        return print(f"Введенный пороль {password} не надежен")
        

        
        
check_password(password)