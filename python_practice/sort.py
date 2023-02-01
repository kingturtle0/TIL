# 선택정렬 selection sort
# N = int(input())
# arr = list(map(int, input().split()))
#
# for i in range(N-1):
#     for j in range(i+1, N):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#
# for k in range(N):
#     print(arr[k], end=' ')

# 삽입정렬 insert sort
# N = int(input())
# arr = list(map(int, input().split()))
# lst = [0] * N
#
# for i in range(N):
#     lst[i] = arr[i]
#     for j in range(i, 0, -1):
#         if lst[j-1] > lst[j]:
#             lst[j], lst[j-1] = lst[j-1], lst[j]
#         else:
#             break
#
# for k in range(N):
#     print(lst[k], end=' ')

# 버블정렬 bubble sort
# N = int(input())
# arr = list(map(int, input().split()))
#
# for i in range(N-1, -1, -1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#
# for k in range(N):
#     print(arr[k], end=' ')

# 계수정렬 counting sort
N = int(input())
arr = list(map(int, input().split()))

num_counts = [0] * (N+1)
for i in range(N):
    num_counts[arr[i]] += 1

for i in range(1, N+1):
    num_counts[i] += num_counts[i-1]

result = [0] * N
for i in range(N):
    result[num_counts[arr[i]] - 1] = arr[i]
    num_counts[arr[i]] -= 1
print(result)