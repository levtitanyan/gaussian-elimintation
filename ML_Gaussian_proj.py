import numpy as np ## import packages

## function
def rref(Ab):
    for x in range(m):
        Ab[x] = Ab[x] / Ab[x][x]  ## making leading entries 1
        for y in range(m):
            if y != x:
                Ab[y] = Ab[y] - Ab[
                    y][x] * Ab[x]  # making column 0 besides leading entry
    return Ab


## matrix size
m = int(input("Enter the number of rows (M): ")); n = int(input("Enter the number of columns (N): "))

## creating random matrix
A = np.random.randint(-100, 100, size=(m, n)); b = np.random.randint(-100, 100, size=(m,1))

## concentration
Ab = np.concatenate((A, b), axis=1).astype(float)
print(Ab); print(f'size is  {m}x{n}')



rref(Ab)
print('*' * 40)
print(Ab)
print('Ab RREF')



