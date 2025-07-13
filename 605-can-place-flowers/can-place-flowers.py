class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):   
        f = [0] + flowerbed + [0] # Setting the start and end with 0

        for i in range(1, len(f) - 1): # Skip the start / last 
            if f[i - 1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1 
        return n <= 0
