class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)

        return [(curNum + extraCandies >= maxCandies) for curNum in candies]  
        