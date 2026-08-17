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

            

        
        
        
        
        
        
        
        
        while right - left > 1:
            if heights[left] < heights[right]:
                left += 1
                continue



            if (left + 1) < right and height[left + 1] > height[left]:
                maxVol = max(maxVol, min(height[left + 1], height[left]) * (right - left + 1))
                left += 1
            
            elif (right - 1) > left and height[right - 1] > height[right]:
                maxVol = max(maxVol, min(height[right - 1] , height[right]) * (right-left -1))
                right -= 1
                break

            


            

        