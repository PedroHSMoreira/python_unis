class first(): 
  def show_age(self, age):
    years = age / 365
    month = age / 30
    days = age
    print(years, month, days)


if __name__ == '__main__':
  print('Informe a sua idade em dias')
  age =  int(input())
  ex = first()
  ex.show_age(age)