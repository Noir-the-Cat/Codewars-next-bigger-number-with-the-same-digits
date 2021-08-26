#Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.

import itertools
def next_bigger(n):
    num = str(n)
    highest = "".join(sorted(num,reverse=True))
    if len(num) < 2:
        return -1
    elif int(highest) == n:    
       return -1
    elif len(num)== 3:
        combinations = sorted(set((list(map("".join, itertools.permutations(num))))))
        for j in range(len(combinations)-1):
            if n == int(combinations[j]):
                return int(combinations[j+1])
    elif len(num) == 2:
        return int(num[1] + num[0])
    else:
        for i in range(2,len(num)+1):
            result = get_bigger(num,i)
            if int(result) != n:
                return(int(result))
            

def get_bigger(num,i):
    last_digit =num[-i:]
    combinations = sorted(set((list(map("".join, itertools.permutations(last_digit))))))
    for j in range(len(combinations)-1):
        if int(combinations[j]) == int(last_digit):    
            return int(num[:-i] +combinations[j+1])
        
    return num
if __name__ == "__main__":
    next_bigger(2637657691371)