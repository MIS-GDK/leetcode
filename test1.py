import heapq

nums = [2, 2, 3, 1]
print(list(set(nums)))
# heapq.heapify(set(nums))

print(nums)

result = heapq.nlargest(3, list(set(nums)))

print(result)