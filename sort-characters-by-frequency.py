class Solution:
    def frequencySort(self, s: str) -> str:
        bucket=[[] for _ in s]
        for ch,freq in collections.Counter(s).items():
            bucket[-freq].append(ch*freq)
        res=""
        for x in range(len(bucket)):
            if bucket[x]:
                for j in bucket[x]:
                    res+=j
        return res