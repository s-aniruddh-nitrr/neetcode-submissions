class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = 0
        water_at_i = []
        for i in range(len(height)):
            left_max,right_max = 0, 0
            for j in range(0, i+1):
                left_max = max(left_max, height[j])
            for k in range(i, len(height)):
                right_max = max(right_max, height[k])
            water_at_i.append(min(left_max,right_max)-height[i])
        print(water_at_i)
        return sum(water_at_i);
            
