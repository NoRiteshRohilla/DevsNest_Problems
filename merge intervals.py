def solve(intervals):
    intervals = sorted(intervals, key = lambda x: x[0])
    ans = []
    current_interval = intervals[0]
    
    for next_interval in intervals[1:]:
        if current_interval[1]>=next_interval[0]:
            if current_interval[1]<next_interval[1]:
                current_interval[1] = next_interval[1]
        else:
            ans.append(current_interval)
            current_interval = next_interval
    ans.append(current_interval)
    return ans
