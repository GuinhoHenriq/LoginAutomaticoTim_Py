import pyodbc

#       conn :-
#Monta a conexão com o banco na Base Da TIM

def conn():
    server = 'TMKT-ZL-DB20' 
    database = 'TIM_LOGIN' 
    username = 'ADM' 
    password = 'ADMUSR'
    cnx = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnx   
pass