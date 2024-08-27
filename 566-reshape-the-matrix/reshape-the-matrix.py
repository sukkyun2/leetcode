class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        
        if m * n != r * c:
            return mat

        arr = [mat[i][j] for i in range(m) for j in range(n)]
        
        return [arr[i:i+c] for i in range(0,m*n,c)]
            
        


        