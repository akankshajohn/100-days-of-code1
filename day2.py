m=int(input("ENTER MARTIX ROW SIZE m : "))
n=int(input("ENTER MARTIX COLUMN SIZE n : "))

X = [[0]*n for j in range(m)]
Y = [[0]*n for j in range(m)]
result = [[0]*n for j in range(m)]
print('Values for martix x')
#getting input to matrix X
for i in range (m):
  for j in range (n):
    print ('entry in row: ',i+1,' column: ',j+1)
    X[i][j] = int(input())
print('Values for martix y')
#getting input to matrix Y
for i in range (m):
  for j in range (n):
    print ('entry in row: ',i+1,' column: ',j+1)
    Y[i][j] = int(input())


for i in range(len(X)):
 for j in range(len(Y[0])):
    for k in range(len(Y)):
        result[i][j] += X[i][k] * Y[k][j]

for r in result:
 print(r)
