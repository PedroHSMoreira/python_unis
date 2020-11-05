class five():
  @staticmethod
  def primeNumber(string):
    stringReverted = ''
    string = str(string)
    string = string.split(' ')
    for word in string:
      stringReverted += word[::-1]+' '
    print(stringReverted)

if __name__ == '__main__':
  string = input('Digite uma frase: ')
  five.primeNumber(string)