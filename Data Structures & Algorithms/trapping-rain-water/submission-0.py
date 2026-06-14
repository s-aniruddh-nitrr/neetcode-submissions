class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = 0
        list1 = []
        for i in range(len(height)):
            maxi1 = 0
            maxi2 = 0
            for j in range(0, i+1):
                maxi1 = max(maxi1, height[j])
            for k in range(i, len(height)):
                maxi2 = max(maxi2, height[k])
            list1.append(min(maxi1,maxi2)-height[i])
            print(list1)
        return sum(list1);
            
