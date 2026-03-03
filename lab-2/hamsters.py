def counting_sort(arr):
    if not arr:
        return []

    n = len(arr)
    maxval = int(max(arr))
    
    counts = [0] * (maxval + 1)
    
    for v in arr:
        counts[int(v)] += 1
        
    for i in range(1, maxval + 1):
        counts[i] += counts[i - 1]
        
    result = [0] * n
    
    for i in range(n - 1, -1, -1):
        v = int(arr[i])
        result[counts[v] - 1] = v
        counts[v] -= 1
        
    return result

def max_hamsters(S, C, hamsters):
    left = 0
    right = C
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        
        if mid == 0:
            left = 1
            continue

        costs = []
        for h, g in hamsters:
            costs.append(h + g * (mid - 1))

        costs = counting_sort(costs)

        total = sum(costs[:mid])

        if total <= S:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer