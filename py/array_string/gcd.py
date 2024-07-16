#1071. Greatest Common Divisor of Strings
'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''

def gcd(str1:str,str2:str)->str:
    if len(str1) ==  len(str2):
        if str1 ==  str2:
            return str1
        else:
            return ""
        
    if len(str1)>len(str2):
        if len(str1) % len(str2) == 0:
            return str2
        else:
            return ""
    else:
        if len(str2) % len(str1) == 0:
            return str1
        else:
            return ""

str1 = "ABCABC"
str2 = "ABC"
print(gcd(str1,str2))