import os as cmd
import Model.UsuarioDAO as user 
import getpass
import wmi
class File:
     
    def __init__(self,path,file,extension):
        self.path = path
        self.file = file
        self.extension = extension

#PATH   
    @property
    def path(self):
        # este código é executado sempre que alguém fizer 
        # ler o valor de self.path
        return self._path

    @path.setter
    def path(self,value):
        # este código é executado sempre que alguém fizer 
        # self.path = value
        self._path = value

#FILE

    @property
    def file(self):
        # este código é executado sempre que alguém fizer 
        # ler o valor de self.file 
        return self._file         
    
    @file.setter
    def file(self,value):
        # este código é executado sempre que alguém fizer 
        # self.file = value
        self._file = value

#EXTENSION

    @property
    def extension(self):
        # este código é executado sempre que alguém fizer 
        # ler o valor de self.extension
        return self._extension

    @extension.setter
    def extension(self,value):
        # este código é executado sempre que alguém fizer 
        # self.extension = value
        self._extension = value

#       KillProcessRSA
# Verifica se existe Processo do RSA 
# se Sim da Kill no Processo 
# caso contrario printa mensagem 'Not Found Process'

    def KillProcessRSA():
        Iprocess = 0
        name = 'SecurID.exe'
        managerProcess = wmi.WMI() 

        for process in managerProcess.Win32_Process(): 
            if process.name == name: 
                process.Terminate() 
                Iprocess += 1
                print('Kill Process')

        if Iprocess == 0: 
            print("Process Not Found!!!") 


#       GetPath:-
# Retorna o Caminho dos arquivos .PNG

    def GetPath():
        path = r'c:\libs\loginautomaticotim\image'
        return path 
    pass

#       OpenFile:-        
# Abre arquivo passado por Parametro(PathFile)
# PathFile = <Caminho do Arquivo> + <Nome do Arquivo> +  <Extensão do Arquivo>

    def OpenFile(PathFile):
        cmd.startfile(PathFile)

#       RemoveFile :-
# Lista os arquivos do diretorio (path) 
# se não houver nenhum arquivo finaliza o processo
# se houver arquivos vai verificar se o arquivo (file) existe
# caso o retorno seja 'True' ele irá excluir o arquivo 
# e executa comando 'print' com a mensagem "File Removed From Folder"
# caso o retorno seja 'False' executa comando 'print'
# com a mensagem "File Not Found" 

    def RemoveFile(path,file):
        clear = 0
        caminho = path
        try:
            if cmd.path.isdir(path):
                dir = cmd.listdir(caminho)
                for arquivo in dir:
                    if arquivo == file:
                        cmd.remove('{}/{}'.format(caminho, arquivo))
                        print('File "''{}''" Removed from Folder' .format(arquivo))
                        clear = 1
                if clear == 0:
                    print('File Not Found')
            else:
                print('Path Not Found')
        except:
            print('Error')
#       PathRSA -:
# Se o parâmetro (code) for igual á 0
# retorna uma String com o caminho do arquivo(RSASecurIDStorage)
# se o parâmetro (code) for igual á 1 
# retorna uma string com o nome do arquivo (RSASecurIDStorage)
# com o Caminho do "RSASecurIDStorage"

    def PathHistoricRSA(code):
        Username = getpass.getuser() 
        PathAndFile = (r'\\' + user.Usuario.ip + r'\c$\Users' +'\\' 
        + Username + r'\AppData\Local\RSA\RSA SecurID Software Token Library','RSASecurIDStorage')
        if code == 0:
            return PathAndFile[0]
        elif code == 1:
            return PathAndFile[1]
    pass

#       CreateDirectory:-
# Verifica se ja existe a pasta 'SEMENTE' no caminho (\\ + <Ip da Maquina> + \c$)
# Se não existir a pasta  ela é criada via cria Prompt de Comando 

    def CreateDirectory():
        try:
            path = r'\\' + user.Usuario.ip + '\c$\SEMENTE'  
            if cmd.path.isdir(path):
                print('Exists')
            else:
                cmd.mkdir(path)
                print('Create')
        except Exception as ex:
            print(ex)

#       CopyFileRSA:-
# Copia Arquivo(SEMENTE) da pasta de origem (source)
# para a pasta de Destino (destination)
# via Prompt de Comando
# e Retorna se deu certo a operação
# 0 para Sucesso
# 1 para Falha

    def CopyFileRSA():
        try:
            sucess = 1
            if user.Usuario.login[0] != 'Error':
                source = r'\\' + user.Usuario.ip + '\C:\\' +  user.Usuario.login[0] + '*.sdtid' #caminho origem
                destination = r'\\' + user.Usuario.ip + '\c$\SEMENTE' #caminho destino
                command = 'copy ' + source + ' ' + destination 
                sucess = cmd.system(command)
            return sucess
        except Exception as ex:
            print(ex)
    pass

#       PathAndFileRSA:-
# Se Usuário possui matricula TIM retorna 
# o caminho e nome do arquivo (SEMENTE) 
# se Usuário não possui matricula TIM
# retorno 'Error'

    def PathAndFileRSA():
        pathReturn = 'Error'
        path = r'\\' + user.Usuario.ip + '\c$\SEMENTE'

        if user.Usuario.login[0] != 'Error':
            dir = cmd.listdir(path)
            for arquivo in dir:

                if user.Usuario.login[0] in arquivo: 
                    pathReturn = path + '\\' + arquivo
        return pathReturn
    pass

#       PathRSAToken:-
# Monta String com o caminho do programa RSA

    def PathRSAToken():
        path = r'\\' + user.Usuario.ip + '\c$\ProgramData\Microsoft\Windows\Start Menu\Programs\RSA\RSA SecurID Token\RSA SecurID Token'
        return path
    pass


        
