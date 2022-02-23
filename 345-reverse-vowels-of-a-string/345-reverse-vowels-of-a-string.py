class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u',"A","E",'I','O','U']
        li = list(s)
        l,r = 0,len(li)-1
        while l < r:
            if li[l] in vowel and li[r] not in vowel:
                r -= 1
            elif li[l] not in vowel and li[r] in vowel:
                l += 1
            elif li[l] in vowel and li[r] in vowel:
                li[l],li[r] = li[r], li[l]
                l += 1
                r -= 1
            else:
                l += 1
                r -= 1
        st = ""
        return st.join(li)