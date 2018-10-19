from random import randint

w, h = 10, 10
matrix = [[0 for x in range(w)] for y in range(h)]

def getAdjacentCount(matrix, x, y):
	count = 0
	if isValid(x-1, y-1):
		if matrix[x-1][y-1] == 9:
			count += 1

	if isValid(x-1, y):
		if matrix[x-1][y] == 9:
			count += 1

	if isValid(x-1, y+1):
		if matrix[x-1][y+1] == 9:
			count += 1

	if isValid(x, y-1):
		if matrix[x][y-1] == 9:
			count += 1

	if isValid(x, y+1):
		if matrix[x][y+1] == 9:
			count += 1

	if isValid(x+1, y-1):
		if matrix[x+1][y-1] == 9:
			count += 1

	if isValid(x+1, y):
		if matrix[x+1][y] == 9:
			count += 1

	if isValid(x+1, y+1):
		if matrix[x+1][y+1] == 9:
			count += 1

	return count

def isValid(x, y):
	if (x < 0 or x > h - 1) or (y < 0 or y > w - 1):
		return False
	else:
		return True

def expandZero(matrix, matrix2, x, y):
	if isValid(x-1, y-1):
		if matrix2[x-1][y-1] == '-':
			matrix2[x-1][y-1] = str(matrix[x-1][y-1])
			if (matrix[x-1][y-1] == 0):
				expandZero(matrix, matrix2, x-1, y-1)

	if isValid(x-1, y):
		if matrix2[x-1][y] == '-':
			matrix2[x-1][y] = str(matrix[x-1][y])
			if (matrix[x-1][y] == 0):
				expandZero(matrix, matrix2, x-1, y)

	if isValid(x-1, y+1):
		if matrix2[x-1][y+1] == '-':
			matrix2[x-1][y+1] = str(matrix[x-1][y+1])
			if (matrix[x-1][y+1] == 0):
				expandZero(matrix, matrix2, x-1, y+1)

	if isValid(x, y-1):
		if matrix2[x][y-1] == '-':
			matrix2[x][y-1] = str(matrix[x][y-1])
			if (matrix[x][y-1] == 0):
				expandZero(matrix, matrix2, x, y-1)

	if isValid(x, y+1):
		if matrix2[x][y+1] == '-':
			matrix2[x][y+1] = str(matrix[x][y+1])
			if (matrix[x][y+1] == 0):
				expandZero(matrix, matrix2, x, y+1)

	if isValid(x+1, y-1):
		if matrix2[x+1][y-1] == '-':
			matrix2[x+1][y-1] = str(matrix[x+1][y-1])
			if (matrix[x+1][y-1] == 0):
				expandZero(matrix, matrix2, x+1, y-1)

	if isValid(x+1, y):
		if matrix2[x+1][y] == '-':
			matrix2[x+1][y] = str(matrix[x+1][y])
			if (matrix[x+1][y] == 0):
				expandZero(matrix, matrix2, x+1, y)

	if isValid(x+1, y+1):
		if matrix2[x+1][y+1] == '-':
			matrix2[x+1][y+1] = str(matrix[x+1][y+1])
			if (matrix[x+1][y+1] == 0):
				expandZero(matrix, matrix2, x+1, y+1)

numOfBombs = 5

# for i in range(len(matrix)):
# 	print(matrix[i])

occupied = 0
while (occupied < numOfBombs):
	x = randint(0, h-1);
	y = randint(0, w-1);

	if (matrix[x][y] == 0):
		matrix[x][y] = 9
		occupied += 1

# print()
# for i in range(len(matrix)):
# 	print(matrix[i])

for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if (matrix[i][j] != 9):
			matrix[i][j] = getAdjacentCount(matrix, i, j)

print("System Matrix")
for i in range(len(matrix)):
	print(matrix[i])

matrix2 = [["-" for x in range(w)] for y in range(h)]
print("\nUser Matrix")
for i in range(len(matrix2)):
	print(matrix2[i])

userSelection = input("Type? ")
print(userSelection)
rowSelection = int(input("Row? "))
columnSelection = int(input("Column? "))

while(matrix[rowSelection][columnSelection] != 9 or userSelection == "f"):
	if (userSelection == "f"):
		matrix2[rowSelection][columnSelection] = 'F'

		print("\nUser Matrix")
		for i in range(len(matrix2)):
			print(matrix2[i])

		userSelection = input("Type? ")
		rowSelection = int(input("Row? "))
		columnSelection = int(input("Column? "))
	else:
		if matrix[rowSelection][columnSelection] == 0:
			matrix2[rowSelection][columnSelection] = str(matrix[rowSelection][columnSelection])
			expandZero(matrix, matrix2, rowSelection, columnSelection)

		matrix2[rowSelection][columnSelection] = str(matrix[rowSelection][columnSelection])

		print("\nUser Matrix")
		for i in range(len(matrix2)):
			print(matrix2[i])

		userSelection = input("Type? ")
		rowSelection = int(input("Row? "))
		columnSelection = int(input("Column? "))

if (matrix[rowSelection][columnSelection] == 9):
	matrix2[rowSelection][columnSelection] = str(matrix[rowSelection][columnSelection])
	print("\nUser Matrix")
	for i in range(len(matrix2)):
		print(matrix2[i])
	
	print("You Lost!")