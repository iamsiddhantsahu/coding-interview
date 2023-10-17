# 787. Cheapest Flights Within K Stops

# There are n cities connected by some number of flights. 
# You are given an array flights where flights[i] = [fromi, toi, pricei] 
# indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, 
# return the cheapest price from src to dst with at most k stops. 
# If there is no such route, return -1.

# https://www.youtube.com/watch?v=5eIK3zUdYmE

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")] * n

        for i in range(k + 1):
            tempPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
            prices = tempPrices
        
        if prices[dst] == float("inf"):
            return -1
        else:
            prices[dst]