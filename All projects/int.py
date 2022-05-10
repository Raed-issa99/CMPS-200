import sys
cmdList = sys.argv[1:]
def cmd_list_to_int(li): #li is name of argument, which is a list from command line
    numbers= [] #converts a sys.argv[] list of strings into intigers
    for s in li:
        numbers += [int(s)]
    return numbers

print(cmd_list_to_int(cmdList))



x = [2, 3] + [4, 5]
#print(x)
x[0] = -2 #Changes the first item in the list from 2 to -2
#print (x)


ls = ["1" , "2" , "3"]
def strongs2ints(ls):
    numbers = []
    for s in ls:
        numbers += [int(s)]
