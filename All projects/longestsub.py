
def longest_alpha(string,index): #determines the string that is in alphabetical order starting from index
    i = index
    word = ''
    while (i < len(string) - 1) and (string[i] <= string[i+1]):#While loop terminate when either out of indecies or next letter is higher (alphabetically, example c>a)
        word += string[i]
        i += 1
    word += string[i]
    return(word)


def longest_substring(string):#Checks all substrings that are in alphabatical order and compares them to each other returning the longest
    answer = ''
    for i in range(len(string)-1):
        trial = longest_alpha(string,i)
        if len(trial) > len (answer):
            answer = trial
    print("longest substring in alphabetical order is:", end = ' ')
    return(answer)

print(longest_substring'azcbobobegghakl'))
