class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        temp_sum_gas=0
        temp_sum_cost= 0
        ans = 0
        if(sum(gas)<sum(cost)):
            return -1
        for i in range(len(gas)):
            temp_sum_gas+=gas[i]
            temp_sum_cost+=cost[i]
            if temp_sum_gas<temp_sum_cost:
                temp_sum_gas=0
                temp_sum_cost=0
                ans=i+1
        return ans