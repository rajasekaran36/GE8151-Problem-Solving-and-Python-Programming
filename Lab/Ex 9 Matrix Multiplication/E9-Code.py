mat_a = [[2,3,4],
        [4,5,6],
        [2,3,7]]
mat_b = [[4,5,6],
         [6,7,8],
         [2,3,4]]
res_m = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            res_m[i][j] = res_m[i][j] + (mat_a[i][k] * mat_b[k][j])

for row in res_m:
    print (row)
