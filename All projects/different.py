def different(lst):
    unique= []
    for i in lst:
        for j in i:
            if not (j in unique):
                unique += [j]
    return(len(unique))

t = [[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]
print(different(t))
