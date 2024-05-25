class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])

        def searchRange():
            for i in range(m):
                if mat[i][0] <= target <= mat[i][-1]:
                    return i
            return -1
        
        def binarySearch(row: List[int], target: int) -> bool:
            front, rear = 0, len(row) - 1
            
            while front <= rear:
                mid = (front + rear) // 2
                
                if row[mid] > target:
                    rear = mid - 1
                elif row[mid] < target:
                    front = mid + 1
                else:
                    return True
            
            return False

        row = searchRange()
        if row == -1:
            return False

        return binarySearch(mat[row], target)
        

        
        