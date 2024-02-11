class Solution(object):
    def __init__(self):
        self.sentence = ""
        
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """        
        if len(s) == 0:
            return True
        
        self.sentence = list(s.lower())

        start = 0
        end = len(self.sentence) - 1
        
        while start <= end:
            if not self.sentence[start].isalnum():
                start += 1
                continue
            
            if not self.sentence[end].isalnum():
                end -= 1
                continue
                
            if self.sentence[start] != self.sentence[end]:
                return False
            
            start += 1
            end -= 1
        
        return True
    
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
