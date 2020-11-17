from tkinter import * # for python3

class MyApp:
    def __init__(self, master=None):
        self.screen = master
        self.screen.resizable(False, False)
        self.screen.title('Cálculo do IMC - Índice de Massa Corporal')
        width = 440
        height = 240
        # Encontrar Resolução do Sistema
        width_screen = self.screen.winfo_screenwidth()
        height_screen = self.screen.winfo_screenheight()
        # Centralizar Janela
        posx = (width_screen / 2) - (width / 2)
        posy = (height_screen / 2) - (height / 2)
        self.screen.geometry('%dx%d+%d+%d' % (width, height, posx, posy))

        self.lb_name = Label(self.screen, text='Nome do Paciente: ')
        self.lb_name.place(x=10, y=20)
        self.e_name = Entry(self.screen)
        self.e_name.place(x=140, y=20, width=280)
        self.e_name.focus()

        self.lb_address = Label(self.screen, text='Endereço Completo: ')
        self.lb_address.place(x=10, y=50)
        self.e_address = Entry(self.screen)
        self.e_address.place(x=140, y=50, width=280)

        self.lb_height = Label(self.screen, text='Altura(cm): ')
        self.lb_height.place(x=10, y=80)
        self.e_height = Entry(self.screen)
        self.e_height.place(x=140, y=80, width=80)

        self.lb_weight = Label(self.screen, text='Peso(Kg): ')
        self.lb_weight.place(x=10, y=110)
        self.e_weight = Entry(self.screen)
        self.e_weight.place(x=140, y=110, width=80)

        self.t_result = Text(self.screen)
        self.t_result.configure(state='disabled', font=('',9))
        self.t_result.place(x=240, y=80, width=180, height=100)

        self.bt_calc = Button(self.screen, text='Calcular', command=self.calc)
        self.bt_calc.place(x=140, y=200, width=80)
        self.bt_res = Button(self.screen, text='Reiniciar', command=self.reset)
        self.bt_res.place(x=230, y=200, width=80)
        self.bt_out = Button(self.screen, text='Sair', command=self.out)
        self.bt_out.place(x=340, y=200, width=80)

    def out(self):
        self.screen.destroy()

    def reset(self):
        self.e_nome.delete(0, END)
        self.e_ender.delete(0, END)
        self.e_weight.delete(0, END)
        self.e_alt.delete(0, END)
        self.t_result.configure(state=NORMAL)
        self.t_result.delete('1.0', END)
        self.t_result.configure(state=DISABLED)

    def calc(self):
        try:
            height = float(self.e_alt.get())
            weight = float(self.e_weight.get())
            result = weight / (height / 100 * height / 100)
            situacao = self.imc_value(result)
            self.t_result.configure(state=NORMAL)
            self.t_result.delete('1.0', END)
            self.t_result.insert(END, '\nResultado: %.2f\n' %result)
            self.t_result.insert(END, '\n%s' %situacao)
            self.t_result.configure(state=DISABLED)
        except:
            pass

    def imc_value(self, valor):
      self.imc = valor
      if (self.imc < 17.00):
        return 'Situação:\n Muito abaixo do peso!'
      elif (self.imc >= 17.00) and (self.imc <= 18.49):
        return 'Situação:\n Abaixo do peso!'
      elif (self.imc >= 18.50) and (self.imc <= 24.99):
        return 'Situação:\n peso normal!'
      elif (self.imc >= 25.00) and (self.imc <= 29.99):
        return 'Situação:\n Acima do peso!'
      elif (self.imc >= 30.00) and (self.imc <= 34.99):
        return 'Situação:\n Obesidade I!'
      elif (self.imc >= 35.00) and (self.imc <= 39.99):
        return 'Situação:\n Obesidade II (severa)!'
      elif (self.imc >= 40.00):
        return 'Situação:\n Obesidade III (mórbida)!'
      else:
        return 'Valores inválidos!'

if __name__ == '__main__':
    main = Tk()
    application = MyApp(main)
    main.mainloop()