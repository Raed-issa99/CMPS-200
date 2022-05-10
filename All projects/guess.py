print ("Think of an integer between 1 and 1000")
print ("Now Truthfully evaluate the following statements with a true or false")

u = 1000
d = 0
Found = False


while not(Found):
    y = input(( 'your number is <= ' + str((u+d)//2) + '\n'))
    if u - d <= 1:
        print("Your number is" + str(u))
        print('mwahahahahaha')
        Found = True
    elif y.lower() == 'true':
        u = (u+d)//2
    elif y.lower() == 'false':
        d = (u+d)//2
    elif y != 'true' or 'false' or 'True' or 'False':
        print('Dahell are u doing.... i said true or false... begone')
        break
