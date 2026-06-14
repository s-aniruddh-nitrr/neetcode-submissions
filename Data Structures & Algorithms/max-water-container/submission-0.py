class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        list1 = []
        end = len(heights)-1
        while(start<end):
            count1 = min(heights[start],heights[end])*(end-start)
            list1.append(count1)
            if(heights[start] > heights[end]):
                end-=1
            else:
                start+=1
        return max(list1)


        
        