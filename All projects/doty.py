    import sys

month = sys.argv[1]
day = int(sys.argv[2])

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
days31 = [0,2,4,6,7,9,11]

year = dict()
for i in range(12):
    if i in [0,2,4,6,7,9,11]:
        year[months[i]] = 31
    elif i == 1:
        year[months[i]] = 28
    else:
        year[months[i]] = 30


def day_of_year(month,day):
    daynum = day
    i = 0
    while months[i] != month:
        daynum += year[months[i]]
        i += 1
    return daynum

print("day of the year is: ", day_of_year(month,day))
