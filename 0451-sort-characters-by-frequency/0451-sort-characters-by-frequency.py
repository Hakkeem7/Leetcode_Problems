class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        buckets = [[] for _ in range(len(s) + 1)]
        for char, freq in count.items():
            buckets[freq].append(char)
        result = []
        for freq in range(len(s), 0, -1):
            for char in buckets[freq]:
                result.append(char * freq)

        return "".join(result)
        