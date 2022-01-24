N = int(input())
rgb = []
for i in range(N):
    rgb.append(list(map(int, input().split())))

for k in range(1, N):
    rgb[k][0] = min(rgb[k-1][1], rgb[k-1][2]) + rgb[k][0]
    rgb[k][1] = min(rgb[k-1][0], rgb[k-1][2]) + rgb[k][1]
    rgb[k][2] = min(rgb[k-1][1], rgb[k-1][0]) + rgb[k][2]

ans = min(rgb[N-1])
print(rgb)
print(ans)

