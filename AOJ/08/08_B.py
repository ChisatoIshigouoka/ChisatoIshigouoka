while True:
  a = input()
  if a == '0':
    break 
  a = list(a)
  print(sum(map(int, a)))