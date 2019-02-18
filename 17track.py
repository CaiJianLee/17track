#Creador TheChapu
#fuente http://www.17track.net
#Cuentan con una Api pero es PAGADA

#Codigo para obtener informacion de envios ---> 17Track
#Agradecimientos a @unkndown

# Importamos las librerias
import requests
import urllib
import httplib
import json

ID = "CN750400915LT"#Aqui numero de seguimiento

host = "17track.net"
link = "http://www.17track.net/restapi/handlertrack.ashx"
parametros = '{"guid":"","data":[{"num":"'+ID+'"}]}'

headers    = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"Accept": "*/*",
"Referer": "http://www.17track.net/es/track?nums="+ID+"&fc=0",
'X-Requested-With': 'XMLHttpRequest',
"Cookie":"__cfduid=d068db605f07408be5e77b46a1b5a3c9b1489755836; __atuvc=5%7C11; __atuvs=58cbdebee36d7721004; v5_ShowedWelcome=1; _ga=GA1.2.102662854.1489755840; __gads=ID=59a7a3123039d55c:T=1489755840:S=ALNI_MaM_SfNKpkXhENkfjaxZbBDSQ5txQ; v5_TrackingGuid=04998d4cd8844d089ba29484654e257a; _gat=1"
}


conexion   = httplib.HTTPConnection(host)
conexion.request("POST", link, parametros, headers)
respuesta  = conexion.getresponse()
ver_source = respuesta.read()

data = json.loads(ver_source)

print "Informacion Chile\n"
for i in range (0,len(data['dat'][0]['track']['z2'])):
	print data['dat'][0]['track']['z2'][i]['a']
	print data['dat'][0]['track']['z2'][i]['c']
	print data['dat'][0]['track']['z2'][i]['z']
	print

print"******************************************"

print "Informacion Extranjero\n"
for i in range (0,len(data['dat'][0]['track']['z1'])):
	print data['dat'][0]['track']['z1'][i]['a']
	print data['dat'][0]['track']['z1'][i]['c']
	print data['dat'][0]['track']['z1'][i]['z']
	print
