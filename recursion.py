def fibonnaci(n):
    #first=0
    #second=0
    if n <= 1:
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a,b):
    if (b != 0):
        return gcd(b, a % b)
    else:
        return a
    


def compareTo(s1, s2):
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1  
    
    elif s1=='\0' and s2=='\0':
        return 0
    
    elif s1 and s2:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])
    return 0

print(fibonnaci(2))
print(fibonnaci(5))
print(gcd(20, 40))
print(compareTo('aaaa', 'bbbbb'))
