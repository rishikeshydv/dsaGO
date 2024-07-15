#1768. Merge Strings Alternately

'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string
'''

def merge(word1:str,word2:str)->str:
    if not word1 and not word2:
        return ''
    if not word1:
        return word2
    if not word2:
        return word1
    res = ''
    ct = 0
    if len(word1) >= len(word2):
        while ct <= len(word1):
            res += word1[ct]
            if ct <= len(word2):
                res += word2[ct] 
    else:
        while ct <= len(word2):
            res += word2[ct]
            if ct <= len(word1):
                res += word1[ct]

    return res

word1 = 'abc'
word2 = 'pqr'
res = merge(word1,word2)
print(res)
