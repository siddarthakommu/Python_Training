m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#ma=[[rw[i] for rw in matrix] for i in range(len(matrix[0]))]
#print(ma)

for i in range(len(m)):
    for j in range(len(m[0])):
        if i<j:
            m[i][j],m[j][i]=m[j][i],m[i][j]

print(m)
