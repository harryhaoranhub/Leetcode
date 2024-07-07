class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        counter = numBottles
        while full >= numExchange:
            new = full // numExchange
            empty = full % numExchange
            full = new + empty
            counter = counter + new

        return counter