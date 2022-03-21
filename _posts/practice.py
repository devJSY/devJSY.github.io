# #문제1
# n, k = map(int, input().split())
# count = 0

# while n != 1:
#     if n // k > 1:
#         n = n // k
#         count += 1
#     else:
#         n -= 1
#         count += 1
        
        
# print(n)

# #문제2
# n = list(input())
# total = 0
# for i in range(len(n)):
#     if int(n[i]) != 0 and total != 0:
#         total *= int(n[i])
#     else:
#         total += int(n[i])

# print(total)
    
# #문제3
# n = int(input())
# m = sum(list(map(int, input().split())))
# print(m // n)

# 구현 방향 백터
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]

# # 현재 위치
# x, y = 2, 2

# for i in range(4):
#     # 다음 위치
#     nx = x + dx[i]
#     ny = y +dy[i]
#     print(nx, ny)