from collections import deque
class Solution:

    def largestRectangleArea(self, heights):
        s = deque()
        max_area = 0
        i = 0
        while i < len(heights):
            if not s or heights[i] >= heights[s[-1]]:
                s.append(i)
                i += 1
            else:
                tp = s.pop()
                area = heights[tp] * (i if not s else i - s[-1] - 1)
                if area > max_area:
                    max_area = area
        while s:
            tp = s.pop()
            area = heights[tp] * (i if not s else i - s[-1] - 1)
            if area > max_area:
                max_area = area
            
        return max_area
                

            
                
            
            

            
if __name__ == '__main__':
    s = Solution()
    # print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(s.largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))
