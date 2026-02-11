'''
    Given an array of timestamps and a window size, find the maximum
    number of requests made within any time window defined as the
    closed interval [x, x + window - 1] for some integer x
    给定一个时间戳数组和一个窗口大小，找出在任意一个时间窗口内
    (定义为某个整数 x 的闭区间 [x, x + window - 1]）所发生的最大请求数量。
'''

# 排序 timestamps
# 左指针 L, 右指针 R
# 不断移动右指针扩张窗口，如果超出范围，就移动左指针缩小窗口

def max_requests(timestamps, window_size):
    timestamps.sort()
    l, r = 0, 0
    max_count = 0
    while r < len(timestamps):
        while timestamps[r] - timestamps[l] > window_size - 1:
            l += 1
        max_count = max(max_count, r - l + 1)
        r += 1
    return max_count

print(max_requests([1, 1, 1, 2, 2, 3], 3))
print(max_requests([1, 2, 3, 10, 11], 3))