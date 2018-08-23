from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient as awsClt
import ssl
import time
import json

def customCallback(client, userdata, message):
    print("Informação recebida: {} do topico {}".format(message.payload, message.topic))

awsHOST = "a2y3icdb9r700k.iot.us-west-2.amazonaws.com"
awsPORT = 8883
awsThing = "Python_com"
clientID = "Python_com"
caRootPATH = r"certificados\root-CA.crt"
certPATH = r"certificados\Python_com.cert.pem"
keyPATH = r"certificados\Python_com.private.key"
loopCount = 0

# Criar o cliente AWS

MQTTClient = awsClt(clientID)
MQTTClient.configureEndpoint(awsHOST, awsPORT)
#MQTTClient.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
MQTTClient.configureCredentials(caRootPATH, keyPATH, certPATH)

#connect to AWS
MQTTClient.connect()
print("Connect")

MQTTClient.subscribe("tempython", 0, customCallback)
time.sleep(2)



list = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]

for i in range(5):
    message = {}
    message['message'] = list[i]
    message['sequence'] = loopCount
    messageJson = json.dumps(message)
    s = MQTTClient.publish("tempython", messageJson, 0)
    print("Status {}".format(s))
    time.sleep(2)
    loopCount += 1



MQTTClient.disconnect()
