import DAL.Conexao as Conexao 
import Model.UsuarioDAO as cUser

class Dados:

#       LocalizationUser:-
# Retorna a Matricula (matricula TMKT) do Operador

    def LocalizationUser():
        try:
            conn = Conexao.conn()
            cursor = conn.cursor()
            sql = "STP_LOCALIZA_MATRICULA_PELO_IP '{}' " .format(cUser.Usuario.ip)
            response = cursor.execute(sql).fetchone()
            conn.close()
            return response 
        except Exception as ex:
            print(ex)
    pass

#       LoginUser:-
# Retorna o Login da TIM do Operador
# (matricula TIM, PIN para acesso do Passcode) 

    def LoginTIM():
        try:
            conn = Conexao.conn()
            cursor = conn.cursor()
            sql = "STP_LOGIN_OPERADOR '{}' " .format(cUser.Usuario.matricula[0])
            response = cursor.execute(sql).fetchone()
            conn.close()
            return response 
        except Exception as ex:
            print(ex) 
    pass

#       CopyRSA:-
# Cria um Diretorio no C:\ chamado SEMENTE
# Copia a Semente (RSA) para a Maquina do Usuário na pasta SEMENTE 
# Retorna o Caminho da Semente(RSA)

    def CopyRSA():
        try:
            conn = Conexao.conn()
            cursor = conn.cursor()
            sql = "STP_COPIA_RSA_DESKTOP '{}','{}' ".format(cUser.Usuario.ip, cUser.Usuario.matricula[0])
            response = cursor.execute(sql).fetchone()
            cursor.commit()
            conn.close() 
            return response
        except Exception as ex:
            print(ex)
    pass 

#       PathRSA -:
# Monta uma String 
# com o Caminho do "RSASecurIDStorage"
         
    def PathRSA():
        try:
            conn = Conexao.conn()
            cursor = conn.cursor()
            sql = "STP_CAMINHO_ARQUIVO_RSA '{}','{}','{}' ".format(cUser.Usuario.ip, cUser.Usuario.matricula[0], 0)
            response = cursor.execute(sql).fetchone()       #Posição [0] -> caminho do arquivo  
            conn.close()                                    #Posição [1] -> nome do arquivo    
            return response
        except Exception as ex:
            print(ex)

#       FileRSA -:
# Monta uma String 
# com o nome do arquivo RSA

    def FileRSA():
        try:
            conn = Conexao.conn()
            cursor = conn.cursor()
            sql = "STP_CAMINHO_ARQUIVO_RSA '{}','{}','{}' ".format(cUser.Usuario.ip, cUser.Usuario.matricula[0], 1)   
            response = cursor.execute(sql).fetchone()
            conn.close()
            return response
        except Exception as ex:
            print(ex)


