class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key=lambda x:x[1], reverse=True)

        for nob, nou in boxTypes:
            ans += nou * min(truckSize, nob)
            truckSize -= min(truckSize, nob)

            if not truckSize:
                return ans
        return ans