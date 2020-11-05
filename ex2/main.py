class second():
  def areaCalculate(self, a, b, c):
    if((a + b) < c) or ((a + c) < b) or ((b + c) < a):
      print('Os lados informados não formam um triângulo')
    else:
      hp = (a + b + c) / 2
      area = (hp * (hp - a) * (hp -b) * (hp - c)) ** 0.5
      print('Área do triângulo %.2f' % area)

if __name__ == '__main__':
  print('Informe um valor para o lado "a"')
  a = int(input())
  print('Informe um valor para o lado "b"')
  b = int(input())
  print('Informe um valor para o lado "c"')
  c = int(input())
  second().areaCalculate(a, b, c)