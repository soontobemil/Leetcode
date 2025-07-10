class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1, len2 = len(str1), len(str2)
# is the prefix of length k a string that can build both str1 and str2 :)
        def valid(k):
            if len1 % k or len2 % k:
                return False
# so if the either string cannot be evenly divided, not valid then false
            base = str1[:k] # take the first k character
            return str1 == base * (len1 // k) and str2 == base * (len2 // k)

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i] #since str 1 and str2 and base are equal 
        return ""
        # no string can be repeated. 