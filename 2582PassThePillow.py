class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        tick = 1
        pillow = []
        while tick <= n:
            pillow.append(tick)
            tick += 1

        tick = n - 1
        while tick > 1:
            pillow.append(tick)
            tick -= 1
        
        index = 0
        while time > 0:
            index += 1
            time -= 1
            if index == len(pillow):
                index = 0

        result = pillow[index]
        return result
    
# A better way to process
# class Solution:
#     def passThePillow(self, n: int, time: int) -> int:
#         tick = 1
#         pillow = []
#         while tick <= n:
#             pillow.append(tick)
#             tick += 1

#         tick = n - 1
#         while tick > 1:
#             pillow.append(tick)
#             tick -= 1
        
#         index = time % len(pillow)
#         result = pillow[index]
#         return result
        