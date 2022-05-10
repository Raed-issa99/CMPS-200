li = [2, -3, 'hello']

print(li)

li[0]= 1.5 #change a value in the list(element)
print(li)

e = li[0] #stores first elemnt in variable e to re-use it
li[0] = li[1]
li[1] = e
print(li)


def mean(list):
    total = 0.0
    for v in list:
        total += v #Adds the value of the v (the elements of the list) to total
    return (total/len(list)) #python tutor.com
