## REF https://docs.python.org/3.4/howto/urllib2.html
## REF https://docs.python.org/3.1/howto/urllib2.html

import time 
import socket
import urllib.request
#import winsound	as ws 		# BEEP 

#TEST SOUND
#winsound.PlaySound('SystemExit', winsound.SND_ALIAS) 

# timeout in seconds
timeout = 1
socket.setdefaulttimeout(timeout)

a_myurl = [] 
#a_myurl.append('http://python.org/')

a_myurl.append('http://192.168.1.2:8080/page1.jsp')
a_myurl.append('http://192.168.1.3:8080/a123.jsp')
#a_myurl.append('http://www.google.co.th/')
#a_myurl.append('http://dolcheck.dol.go.th')

 
minute     = 1 #/60
delay_time = 60 * minute 


def check_url(url):
	try: 
		with urllib.request.urlopen(myurl) as response:
			retcode = response.getcode()			# NOT USE  , But show as example only !!
			tx = str(response.status) + "/" +  str(response.reason)
		return {'ST':tx,'url':url}			
	except urllib.error.URLError as e:
		tx = "{no1}/{tx} ".format(no1=e.errno,tx=e.reason) 
		#ws.PlaySound('SystemExclamation', winsound.SND_ALIAS) 
		return {'ST':tx,'url':url}
	except Exception as e:
		tx = "{no1}/{tx} ".format(no1=e.errno,tx=e.reason) 
		#ws.PlaySound('SystemExclamation', winsound.SND_ALIAS) 
		return {'ST':tx,'url':url}

while (True):
	for myurl in a_myurl: 
		retobj = check_url(myurl)
		print(retobj)
	print("===================================")
	s1 = time.strftime("%Y-%m-%d %H:%M:%S")
	print("since {s1} , wait {d1} sec".format(s1=s1,d1=delay_time))
	time.sleep(delay_time) # delays for 5 seconds



	