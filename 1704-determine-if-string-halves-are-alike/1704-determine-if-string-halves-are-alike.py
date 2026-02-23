class Solution(object):
    def halvesAreAlike(self, s):
        vowels = 'aeiouAEIOU'
        mid = len(s)//2
        c1=0
        for i in s[:mid]:
            if i in vowels:
                c1+=1
        for i in s[mid:]:
            if i in vowels:
                c1-=1
                
        
        if c1==0:
            return True
        return False
        
        