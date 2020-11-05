class tree():
  def smaller(self, a, b, c):
    if (a < b) and (a < c):
        smaller = a
    elif (b < a) and (b < c):
        smaller = b
    elif (c < a) and (c < b):
        smaller = c
    elif (a <= b) or (a <= c):
        smaller = a
    elif (b <= a) or (b <= c):
        smaller = b
    else:
        smaller = c
    print("O menor é:", smaller)

if __name__ == '__main__':
  print('Informe um valor "a"')
  a = int(input())
  print('Informe um valor "b"')
  b = int(input())
  print('Informe um valor "c"')
  c = int(input())
  tree().smaller(a, b, c)