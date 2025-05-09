class InsertInterval:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        if len(intervals) == 0:
            return [newInterval]

        merged = list()
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i = i + 1

        mergeInterval = newInterval
        while i < len(intervals) and mergeInterval[1] >= intervals[i][0]:
            mergeInterval = [min(intervals[i][0] , mergeInterval[0]) , max(intervals[i][1] , mergeInterval[1])]
            i = i + 1

        merged.append(mergeInterval)

        while i < len(intervals):
            merged.append(intervals[i])
            i = i + 1

        return merged    



insertInterval = InsertInterval()
intervals = insertInterval.insert([[1,3],[6,9]] , [2,5])

for interval in intervals:
    print(interval[0] , " ", interval[1])


