class four():
  @staticmethod
  def primeNumber(n):
    aux = 0
    for i in range(1, n+1, 1):
            if n % i == 0:
                aux += 1
                if aux > 2:
                    return False
                    break

    if aux == 2:
      return True

if __name__ == '__main__':
  print('Informe um número entre 1 a 100')
  n = int(input())
  res = four.primeNumber(n)
  if res:
    print('Sim')
  else:
    print('Não')