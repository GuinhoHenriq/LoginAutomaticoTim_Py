import DAL.Dados as dDados
import Model.UsuarioDAO as user
import Class.File as cFile
import Class.Logs as cLogs
import socket
import pyautogui as automation
import webbrowser as web
import time 
from ctypes import *

#		Create File txt Log.log
log = cLogs.Logs.Logger('Log')
#		END


#		Kill Process RSA
cFile.File.KillProcessRSA()
#		END

#-------------------------------------

#		Disable Capslock
hllDll = WinDLL("User32.dll")
VK_CAPITAL = 0x14
capslock = hllDll.GetKeyState(VK_CAPITAL) # 1 = Enabled / 0 = Disabled

if capslock == 1:
	automation.press('capslock')
#		END

#-------------------------------------

################################## BLOCKED ################################
windll.user32.BlockInput(True)
#--------------------------------------

#       Path of Imagens
path = cFile.File.GetPath()
#       END

#--------------------------------------

#       Capuring IP, Registration and Login TIM
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

user.Usuario.ip = IP
user.Usuario.matricula = dDados.Dados.LocalizationUser() 
user.Usuario.login = dDados.Dados.LoginTIM() 
#       END

#--------------------------------------

#		Deleting RSA History File1234
cFile.File.path = cFile.File.PathHistoricRSA(0)
cFile.File.file = cFile.File.PathHistoricRSA(1)

cFile.File.RemoveFile(cFile.File.path,cFile.File.file)		
#		END

#--------------------------------------

#       Opening Google Chrome
url = 'https://apptimvendas.timbrasil.com.br/beta_live/#/login'
StatusChrome = True

AlertChrome = None

if user.Usuario.login[0] != 'Error':
	if StatusChrome == True:
		web.register('chrome',
			None,
			web.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))

		StatusChrome = web.get('chrome').open(url)

	if StatusChrome == False:
		web.register('chrome',
			None,
			web.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
		StatusChrome = web.get('chrome').open(url)
	
	if StatusChrome == False:
		AlertChrome = 'Not Found'
else:
    AlertChrome = 'Not Found'
#		END

#--------------------------------------
##################LOG##################
log.info(cLogs.Logs.FormatterMessageLog('Opening Google Chrome "AlertChrome"',AlertChrome))
#--------------------------------------

#		Expanding Google Chorme Window

time.sleep(2)
ImageMaximizar = None
AlertMaximizar = None

try:
	if user.Usuario.login[0] != 'Error':
		ImageMaximizar = automation.locateOnScreen(path + '\Maximizar.PNG', grayscale = True, confidence = 0.6)

		if ImageMaximizar != None:
			automation.moveTo(ImageMaximizar)
			automation.click(button = 'left')
		else:
			AlertMaximizar = 'Not Found' 	
	else:
		AlertMaximizar = 'Not Found'
except Exception as ex:
	AlertMaximizar = 'Not Found' 	
	print(ex)
#		END

#--------------------------------------
##################LOG##################
log.info(cLogs.Logs.FormatterMessageLog('Expanding Google Chorme Window "AlertMaximizar"',AlertMaximizar))
#--------------------------------------

#		Creating Directory and Copying the RSA Seed to the User machine
Attempts = 0
AlertCopyFile = 1

cFile.File.CreateDirectory()

if user.Usuario.login[0] != 'Error':
	while Attempts < 4: 
		if AlertCopyFile != 0:
			AlertCopyFile =  cFile.File.CopyFileRSA() #dDados.Dados.CopyRSA()
		else:
			break
		Attempts = Attempts + 1 
#		END

#--------------------------------------
##################LOG##################
if AlertCopyFile == 0:
	log.info(cLogs.Logs.FormatterMessageLog('Copying the RSA Seed to the User machine "AlertCopyFile"',None))
else:
	log.info(cLogs.Logs.FormatterMessageLog('Copying the RSA Seed to the User machine "AlertCopyFile"','Not Found'))
#--------------------------------------

#		Open the seed (seed RSA)
AlertSeed = None

PathSeed = cFile.File.PathAndFileRSA()

if PathSeed != 'Error':
    cFile.File.OpenFile(PathSeed)	
else:
    AlertSeed = 'Not Found'	
#		END

#--------------------------------------
##################LOG##################
log.info(cLogs.Logs.FormatterMessageLog('Open the seed (seed RSA) "AlertSeed"',AlertSeed))
#--------------------------------------

#		Import the seed (seed RSA)

ImageEnterPassword = None
ImageOK = None
ImageChangeName = None
ImageConfirmar = None
ImageConfirmarChange = None

AlertConfirmeChange = None
AlertProcess = None

time.sleep(7)
try:
	if user.Usuario.login[0] != 'Error' and AlertSeed == None and AlertCopyFile == 0:
		ImageEnterPassword = automation.locateOnScreen(path + '\EnterPassword.PNG', grayscale = True, confidence = 0.6)
		ImageOK = automation.locateOnScreen(path + '\OK.PNG', grayscale = True, confidence = 0.6)

		if ImageEnterPassword != None and ImageOK != None:
    			
			#Process: typing password
			automation.moveTo(ImageEnterPassword)
			automation.click(button = 'left')
			automation.write(user.Usuario.login[0])

			#Process: Click in Ok
			automation.moveTo(ImageOK)
			automation.click(button='left')
				
			#Process: Click in Change Name
			time.sleep(2)
			ImageChangeName = automation.locateOnScreen(path + '\ChangeName.PNG', grayscale = True, confidence = 0.6)
			ImageConfirmarChange = automation.locateOnScreen(path + '\Confirmar.PNG', grayscale = True, confidence = 0.6)

			if ImageChangeName != None:
				automation.moveTo(ImageChangeName)
				automation.click(button='left')
			elif ImageConfirmarChange != None:
				automation.moveTo(ImageConfirmarChange)
				automation.click(button='left')

				AlertConfirmeChange = 'Exists'

			#Process: Click in OK
			time.sleep(5)
			ImageConfirmar = automation.locateOnScreen(path + '\Confirmar.PNG', grayscale = True, confidence = 0.6)

			if ImageConfirmar != None and AlertConfirmeChange == None:
				automation.moveTo(ImageConfirmar)
				automation.click(button='left')
			else:
				AlertProcess = 'Not Found' 	
		
		else:
			AlertProcess = 'Not Found' 	
	else:
		AlertProcess = 'Not Found' 					
except Exception  as  ex:
	AlertProcess = 'Not Found' 	
	print(ex)
#		END

#--------------------------------------
##################LOG##################
log.info(cLogs.Logs.FormatterMessageLog('Import the seed (seed RSA) "AlertProcess"',AlertProcess))
#--------------------------------------

#		Typing the Pin and Geting PassCode
ImagePin = None
ImageCopyPassCode = None

AlertCopyPassCode = None
AlertPin = None

#Process: Typing the Pin
time.sleep(2)
try:
	if user.Usuario.login[1] != 'Error' and AlertProcess == None:	
		ImagePin = automation.locateOnScreen(path + '\ReceiveToken.PNG', grayscale = True, confidence = 0.6)
	
		if ImagePin != None:
			automation.write(user.Usuario.login[1])
			automation.moveTo(ImagePin)	
			automation.click(button='left')
		else:
			AlertPin = 'Not Found' 	
	else:
		AlertPin = 'Not Found' 			
except:
	AlertPin = 'Not Found' 	
	

time.sleep(2)
try:
	if AlertPin == None:
		ImageCopyPassCode = automation.locateOnScreen(path + '\Copy.PNG', grayscale = True, confidence = 0.6)

		if ImageCopyPassCode != None:
			automation.moveTo(ImageCopyPassCode)
			automation.click(button='left')
		else:
			AlertCopyPassCode = 'Not Found' 	
	else:
		AlertCopyPassCode = 'Not Found' 	
except:
	AlertCopyPassCode = 'Not Found' 	
#		END

#--------------------------------------
##################LOG##################
log.info(cLogs.Logs.FormatterMessageLog('Process: Typing the Pin "AlertPin"',AlertPin))
log.info(cLogs.Logs.FormatterMessageLog('Process: Geting PassCode "AlertCopyPassCode"',AlertCopyPassCode))
#--------------------------------------

#		Close Program RSA Token
time.sleep(1)
ImageCloseRSA = None

AlertCloseRSA = None


try:
	if user.Usuario.login[0] != 'Error' and AlertPin == None and AlertCopyPassCode == None:
		ImageCloseRSA = automation.locateOnScreen(path + '\CloseRSA.PNG', grayscale = True, confidence = 0.6)
		if ImageCloseRSA != None:
			automation.moveTo(ImageCloseRSA)
			automation.click(button='left')
		else:
			AlertCloseRSA = 'Not Found' 	
	else:
		AlertCloseRSA = 'Not Found' 	
except:
	AlertCloseRSA = 'Not Found' 	
#		END

#--------------------------------------
##################LOG##################
log.info(cLogs.Logs.FormatterMessageLog('Close Program RSA Token "AlertCloseRSA"',AlertCloseRSA))
#--------------------------------------

#		User disconnected?
ImageOKError = None

AlertOKError = None

AttemptsDesconnect = 0

try:
	if user.Usuario.login[0] != 'Error' and AlertCloseRSA == None:
		ImageOKError = automation.locateOnScreen(path + '\OKError.PNG', grayscale = True, confidence = 0.6)

		if ImageOKError != None:
			automation.moveTo(ImageOKError)
			automation.click(button='left')
		else:
			AlertOKError = 'Not Found' 	
	else:
		AlertOKError = 'Not Found' 	
except:
	AlertOKError = 'Not Found' 	

if AlertOKError == None:
	while AttemptsDesconnect < 4:
		time.sleep(3)
		ImageLoadingDesconnect = None
		ImageLoadingDesconnect = automation.locateOnScreen(path + '\Desconnect.PNG', grayscale = True, confidence = 0.6)
		
		if ImageLoadingDesconnect == None:
			AttemptsDesconnect = 4

	AttemptsDesconnect = AttemptsDesconnect + 1
#		END

#--------------------------------------
##################LOG##################
log.info(cLogs.Logs.FormatterMessageLog('User disconnected? "AlertOKError"',AlertOKError))
#--------------------------------------

#		Entering the TIM website
ImageRegistrationTIM = None
ImagePasswordTIM = None
ImageLogin = None

AlertPasswordTIM = None
AlertRegistrationTIM = None
AlertLogin = None

time.sleep(5)
try:
	if user.Usuario.login[0] != 'Error' and AlertCloseRSA == None:
		ImageRegistrationTIM = automation.locateOnScreen(path + '\RegistrationTIM.PNG', grayscale = True, confidence = 0.6)
		ImagePasswordTIM = automation.locateOnScreen(path + '\PasswordTIM.PNG', grayscale = True, confidence = 0.6)
			

		#Password
		if ImagePasswordTIM != None:
			automation.moveTo(ImagePasswordTIM)
			automation.click(button='left')
			automation.hotkey('ctrl','v')
		else:
			AlertPasswordTIM = 'Not Found' 	

		#User
		if ImageRegistrationTIM != None:
			automation.moveTo(ImageRegistrationTIM)
			automation.click(button='left')
			automation.write(user.Usuario.login[0])
		else:
			AlertRegistrationTIM = 'Not Found' 	

	else:
		AlertRegistrationTIM = 'Not Found' 	
		AlertPasswordTIM = 'Not Found' 	
except:
	AlertRegistrationTIM = 'Not Found' 	
	AlertPasswordTIM = 'Not Found' 	

try:
	if ImageRegistrationTIM != None and ImagePasswordTIM != None:
		ImageLogin = automation.locateOnScreen(path + '\Login.PNG', grayscale = True, confidence = 0.6)

		if ImageLogin != None:
			automation.moveTo(ImageLogin)
			automation.click(button='left')
		else:
			AlertLogin = 'Not Found' 	
	else:
		AlertLogin = 'Not Found' 	
except:
	AlertLogin = 'Not Found' 	
#		END

#--------------------------------------
##################LOG##################
log.info(cLogs.Logs.FormatterMessageLog('Entering the TIM website (Password) "AlertPasswordTIM"',AlertPasswordTIM))
log.info(cLogs.Logs.FormatterMessageLog('Entering the TIM website (User) "AlertRegistrationTIM"',AlertRegistrationTIM))
log.info(cLogs.Logs.FormatterMessageLog('Entering the TIM website (Login) "AlertLogin"',AlertLogin))
#--------------------------------------

#		Error entering TIM website (New try)
ImageErrorLogin = None

AlertErrorLogin = None

time.sleep(3)

if AlertRegistrationTIM == None and AlertPasswordTIM == None:
	try:
			
		# 4 Attempts
		ErrorAttempts = 0

		while ErrorAttempts < 4:
				
			time.sleep(4)	
			ImageErrorLogin = None
			ImageLoading = None

			ImageErrorLogin = automation.locateOnScreen(path + '\Login.PNG', grayscale = True, confidence = 0.6)
			ImageLoading = automation.locateOnScreen(path + '\Loading.PNG', grayscale = True, confidence = 0.6)

			if ImageErrorLogin != None:
				ErrorAttempts = ErrorAttempts + 1
				cFile.File.OpenFile(cFile.File.PathRSAToken())

				#Process: Typing Pin (1º)
				time.sleep(3)
				if user.Usuario.login[1] != 'Error' and AlertProcess == None:	
					ImagePin = None
					ImagePin = automation.locateOnScreen(path + '\ReceiveToken.PNG', grayscale = True, confidence = 0.6)
		
					if ImagePin != None:
						automation.write(user.Usuario.login[1])
						automation.moveTo(ImagePin)	
						automation.click(button='left')

						# Process: Geting PassCode (2º)
						time.sleep(2)
						ImageCopyPassCode = None
						ImageCopyPassCode = automation.locateOnScreen(path + '\Copy.PNG', grayscale = True, confidence = 0.6)

						if ImageCopyPassCode != None:
							automation.moveTo(ImageCopyPassCode)
							automation.click(button='left')	

							#Close Program RSA Token (3º)
							ImageCloseRSA = None
							ImageCloseRSA = automation.locateOnScreen(path + '\CloseRSA.PNG', grayscale = True, confidence = 0.6)

							if ImageCloseRSA != None:
								automation.moveTo(ImageCloseRSA)
								automation.click(button='left')

								#Process: Entering the TIM website (4º)
								ImageRegistrationTIM = None
								ImagePasswordTIM = None
								ImageRegistrationTIM = automation.locateOnScreen(path + '\RegistrationTIM.PNG', grayscale = True, confidence = 0.6)
								ImagePasswordTIM = automation.locateOnScreen(path + '\PasswordTIM.PNG', grayscale = True, confidence = 0.6)
			

								#Password and User
								if ImagePasswordTIM != None and ImageRegistrationTIM != None:
									automation.moveTo(ImagePasswordTIM)
									automation.click(button='left')
									automation.hotkey('ctrl','v')

									automation.moveTo(ImageRegistrationTIM)
									automation.click(button='left')
									automation.write(user.Usuario.login[0])
								
									ImageLogin = None
									ImageLogin = automation.locateOnScreen(path + '\Login.PNG', grayscale = True, confidence = 0.6)
								
									if ImageRegistrationTIM != None and ImagePasswordTIM != None and ImageLogin != None:
										automation.moveTo(ImageLogin)
										automation.click(button='left')

			elif ImageLoading != None and ImageErrorLogin == None:
					continue
			else:
				ErrorAttempts = 4	 				
	except:
		AlertErrorLogin = 'Not Found' 
else:
	AlertErrorLogin = 'Not Found' 

#--------------------------------------
##################LOG##################
log.info(cLogs.Logs.FormatterMessageLog('Entering TIM website (New try) "AlertErrorLogin"',AlertErrorLogin))
log.handlers.clear()
#--------------------------------------

windll.user32.BlockInput(False)
################################## UNLOCKED ################################