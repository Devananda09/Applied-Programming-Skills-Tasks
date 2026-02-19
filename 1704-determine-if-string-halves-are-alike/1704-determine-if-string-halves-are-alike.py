class Solution(object):
    def halvesAreAlike(self, s):
        vowels = 'aeiouAEIOU'
        mid = len(s)//2
        c1,c2=0,0
        for i in s[:mid]:
            if i in vowels:
                c1+=1
        for i in s[mid:]:
            if i in vowels:
                c2+=1
                
        
        if c1==c2:
            return True
        return False
        
        