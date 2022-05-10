from segment import Segment

f = open('segments.txt', 'r')
f = f.read()
f = f.split('\n')


AllSegm = list()
for line in f:
    Cords = line.split(' ')
    if len(Cords) == 2:
        AllSegm += [Segment(float(Cords[0]),float(Cords[1]))]


AllSegm.sort()
print("Sorted segments:", end = '')
for seg in AllSegm:
    print(seg, end = ' ')
print()

for i in range(len(AllSegm)-1):
    for j in range(i+1,len(AllSegm)):
        if AllSegm[i].overlaps(AllSegm[j]):
            if AllSegm[i].right > AllSegm[j].right:
                print(str(AllSegm[j]) + ' overlaps ' + str(AllSegm[i]))
            else:
                print(str(AllSegm[i]) + ' overlaps ' + str(AllSegm[j]))


BoundarySegment = Segment(min([i.left for i in AllSegm]),max([i.right for i in AllSegm]))
print("\n" "Boundary Segment is: " + str(BoundarySegment))
