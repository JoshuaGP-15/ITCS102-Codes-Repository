size = int(input('innput size'))

for x in range(size):
  for i in range(size):
    if x + i == size - 1 or x == i:
      print('*',end=' ')
    else:
      print(' ',end=' ')
print()
