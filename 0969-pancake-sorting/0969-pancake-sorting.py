class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        
        for size in range(len(arr), 1, -1):

            # Find the largest element
            max_index = arr.index(size)

            # If already in correct position, skip
            if max_index == size - 1:
                continue

            # Move largest element to the front
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
                result.append(max_index + 1)

            # Move largest element to its final position
            arr[:size] = arr[:size][::-1]
            result.append(size)

        return result