import time
import sys
import logging
import logging.config
class Logs:
    def __init__(self,message,step,log):
        self.message = message
        self.step = step
        self._log = log

    
#MESSAGE
    @property
    def message(self):
        return self._message
    

    @message.setter
    def message(self,value):
        self._message = value
#STEP
    @property
    def step(self):
        self._step

    @step.setter
    def step(self,value):
        self._step = value

#LOG
    @property
    def log(self):
        return self._log

    @log.setter
    def log(self,value):
        self._log = value

#       RecordLogsInTxt:-
# Monta String de log e faz a chamada do metodo txtLog
# metodo txtLog cria/escreve no arquivo .txt

    def RecordLogsInTxt(step,message):
        log = None
        try:
            if message != None:
                log = time.strftime("%d/%m/%Y %H:%M:%S") + ' -> ' +  step + ' - ' + message    
            else:
                log = time.strftime("%d/%m/%Y %H:%M:%S")  + ' -> ' + step + ' - Sucess'
        except:
            print('Error Log')

        if log != None:
            Logs.txtLog(log)
        else:
            print('The variable value "log" is "None"')

#       FormatterMessageLog:-
# Monta String de Log
# step -> Etapa + message -> Messagem

    def FormatterMessageLog(step,message):
        if message != None :
            txtLog = step + ' <-> ' + message
        else:
            txtLog = step + ' <-> ' + 'Sucess'

        return txtLog

#       Logger:-
# Configura Arquivo de Log
# verifica se ja existe arquivo Log.log
# se ja existe o arquivo e o programa esta executando na Segunda-feira = Monday
# substitui o arquivo de Log atual por um novo
# caso contrario mantem escrevendo no mesmo arquivo

    def Logger(file_name):
        try:
            if time.strftime('%A') == 'Monday':
                mode = 'w'
            else:
                mode = 'a'

            formatter = logging.Formatter(fmt='%(asctime)s %(module)s,line: %(lineno)d %(levelname)8s | %(message)s',
                                        datefmt='%Y/%m/%d %H:%M:%S') # %I:%M:%S %p AM|PM format
            logging.basicConfig(filename = '%s.log' %(file_name),format= '%(asctime)s %(module)s,line: %(lineno)d %(levelname)8s | %(message)s',
                                      datefmt='%Y/%m/%d %H:%M:%S', filemode = mode, level = logging.INFO)
            log_obj = logging.getLogger()
            log_obj.setLevel(logging.DEBUG)

            screen_handler = logging.StreamHandler(stream=sys.stdout) 
            screen_handler.setFormatter(formatter)
            logging.getLogger().addHandler(screen_handler)

            return log_obj           
        except:
            print('Error')
