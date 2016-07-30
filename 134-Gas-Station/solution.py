class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n=len(gas)
        if n!=len(cost):
            return -1
        
        # potiential start gas station
        st=0
        while st<n:
            # if cann't as start pos then move on
            if gas[st]-cost[st]<0:
                st+=1
                continue
            
            idx=st
            remaining=0
            while idx<n+st:
                pos=idx%n
                remaining+=gas[pos]-cost[pos]
                # if reach exhaust, get new start
                if remaining<0:
                    st=idx+1
                    break
                # if reach the start
                if (idx+1)%n==st:
                    return st
                idx+=1
        return -1
                        