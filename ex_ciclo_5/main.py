import mysql.connector 
import os

def connect():
    cnx = mysql.connector.connect(
    host="localhost",
    user=os.environ['DBUSERNAME'],
    password=os.environ['DBPASSWORD'],
    database=os.environ['DBNAME'],
    auth_plugin='mysql_native_password'
    )
    # cursor.execute("CREATE TABLE patient (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), height DOUBLE, weight DOUBLE)")
    return cnx

def saveUser(self):
    cursor = self.cursor()
    name = input('Nome: ')
    address = input('Endereço: ')
    height = float(input('Altura(M): '))
    weight = float(input('Peso(Kg): '))
    sql = "INSERT INTO patient (name, address, height, weight) VALUES (%s, %s, %s, %s)"
    val = (name, address, height, weight)
    print('-------------------')
    print('\nConfirmar Valores:')
    print('Nome:', name)
    print('Endereço:', address)
    print('Altura(M):', height)
    print('Peso(Kg):', weight)
    res = input('Os valores estão corretos(s/n)? ')
    if res == 's':
        cursor.execute(sql, val)
        self.commit()
        print('\n\nPaciente inserido com sucesso!')
    elif res == 'n':
        return

def getAllPatients(self):
    cursor = self.cursor()
    cursor.execute('SELECT * FROM patient')
    result = cursor.fetchall()
    for x in result:
        print('Id: ',x[0])
        print('Nome: ', x[1])
        print('Endereço: ', x[2])
        print('Altura(M): ', x[3])
        print('Peso(Kg): ', x[4])

def searchPatientByName(self):
    cursor = self.cursor()
    name = input('Nome: ')
    sql = "SELECT * FROM patient WHERE name = %s"
    val = (name, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    print('\nResultado:\n')
    for x in result:
        print('Id:',x[0])
        print('Nome:', x[1])
        print('Endereço:', x[2])
        print('Altura(M):', x[3])
        print('Peso(Kg):', x[4])

def searchPatientById(self):
    cursor = self.cursor()
    idPatient = input('Id: ')
    sql = "SELECT * FROM patient WHERE id = %s"
    val = (idPatient, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    print('\nResultado:\n')
    for x in result:
        print('Id:',x[0])
        print('Nome:', x[1])
        print('Endereço:', x[2])
        print('Altura(M):', x[3])
        print('Peso(Kg):', x[4])
    return idPatient

def updatePatientById(self):
    cursor = self.cursor()
    idPatient = int(input('Id: '))
    print('1 - Atualizar todos os dados')
    print('2 - Atualizar somente o nome')
    print('3 - Atualizar somente o endereço')
    print('4 - Atualizar somente a altura')
    print('5 - Atualizar somente o peso')
    print('0 - Cancelar')
    choice = input('\nO que deseja atualizar? ')
    if choice == '0':
        return
    elif choice == '1':
        name = input('Nome: ')
        address = input('Endereço: ')
        height = float(input('Altura(M): '))
        weight = float(input('Peso(Kg): '))
        sql = "UPDATE patient SET name = %s, address = %s, height = %s, weight = %s WHERE id = %s"
        val = (name, address, height, weight, idPatient)
        cursor.execute(sql, val)
        self.commit()
    elif choice == '2':
        name = input('Nome: ')
        sql = "UPDATE patient SET name = %s WHERE id = %s"
        val = (name, idPatient)
        cursor.execute(sql, val)
        self.commit()
    elif choice == '3':
        address = input('Endereço: ')
        sql = "UPDATE patient SET address = %s WHERE id = %s"
        val = (address, idPatient)
        cursor.execute(sql, val)
        self.commit()
    elif choice == '4':
        height = float(input('Altura(M): '))
        sql = "UPDATE patient SET height = %s WHERE id = %s"
        val = (height, idPatient)
        cursor.execute(sql, val)
        self.commit()
    elif choice == '5':
        weight = float(input('Peso(Kg): '))
        sql = "UPDATE patient SET weight = %s WHERE id = %s"
        val = (weight, idPatient)
        cursor.execute(sql, val)
        self.commit()
    print('\n\nPaciente atualizado com sucesso!')

def deletePatientById(self):
    cursor = self.cursor()
    idPatient = searchPatientById(self)
    sql = "DELETE FROM patient WHERE id = %s"
    val = (idPatient, )
    choice = input('Tem certeza que deseja excluir esse paciente?(s/n)')
    if choice == 'n':
        return
    elif choice == 's':
        cursor.execute(sql, val)
        self.commit()
        print('\n\nPaciente excluído com sucesso!')  
    

def getChoice():
    print('1 - Cadastrar paciente')
    print('2 - Buscar todos pacientes')
    print('3 - Buscar paciente por nome')
    print('4 - Buscar paciente por id')
    print('5 - Atualizar cliente por id')
    print('6 - Excluir usuário por id')
    print('0 - Sair do sistema')
    choice = input('\nO que deseja fazer? ')
    return choice

def main(context): 
    print('\n   Cálculo IMC ')
    print('-------------------')
    print('\n   Menu')
    print('-------------------')
    choice = getChoice()

    if choice == '0':
        print('\nSair')
        quit()
    elif choice == '1':
        print('\nCadastrar paciente\n')
        saveUser(context)
    elif choice == '2':
        print('\nBuscar todos pacientes')
        getAllPatients(context)
    elif choice == '3':
        print('\nBuscar paciente por nome')
        searchPatientByName(context)
    elif choice == '4':
        print('\nBuscar paciente por id')
        searchPatientById(context)
    elif choice == '5':
        print('\nAtualizar cliente por id')
        updatePatientById(context)
    elif choice == '6':
        print('\nExcluir usuário por id')
        deletePatientById(context)
     

if __name__=='__main__':
    cnx = connect()
    while True: 
        main(cnx)
        
