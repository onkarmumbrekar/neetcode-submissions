class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        n = len(arr)
        for i in range(n-1):
            max_val = 0
            for j in range(i+1, n):
                if arr[j] >= max_val:
                    max_val = arr[j]
            arr[i] = max_val
        arr[n-1] = -1
        return arr