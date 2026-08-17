class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        maxVol = min(heights[0], heights[n-1]) * (n-1)
        left, right = 0, n-1
        maxLeft, maxRight = heights[left], heights[right]

        while right - left > 1:
            if heights[left] <= heights[right]:
                left += 1
                if heights[left] > maxLeft:
                    maxLeft = heights[left]
                    maxVol = max(maxVol, min(maxLeft, maxRight)*(right-left))

            else :
                right -= 1
                if heights[right] > maxRight:
                    maxRight = heights[right]
                    maxVol = max(maxVol, min(maxLeft, maxRight)*(right-left))

        return maxVol



            


            

        