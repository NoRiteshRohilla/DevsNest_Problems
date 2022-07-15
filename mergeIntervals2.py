# # class Solution:
# #     def merge(intervals):
# #         intervals = sorted(intervals, key=lambda x: x[0])
# #         ans = []
# #         current_interval = intervals[0]

# #         for next_interval in intervals[1:]:
# #             if current_interval[1] >= next_interval[0]:
# #                 if current_interval[1] < next_interval[1]:
# #                     current_interval[1] = next_interval[1]
# #             else:
# #                 ans.append(current_interval)
# #                 current_interval = next_interval
# #         ans.append(current_interval)
# #         return ans
# class Solution:
#     def merge(self, intervals):
#         out = []
#         for i in sorted(intervals, key=lambda i: i.sort):
#             if out and i.sort <= out[-1].end:
#                 out[-1].end = max(out[-1].end, i.end)
#             else:
#                 out += i,
#         return out

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            if merged == []:
                merged.append(intervals[i])
            else:
                previous_end = merged[-1][1]
                current_start = intervals[i][0]
                current_end = intervals[i][1]
                if previous_end >= current_start: # overlap
                    merged[-1][1] = max(previous_end,current_end)
                else:
                    merged.append(intervals[i])
        return merged
