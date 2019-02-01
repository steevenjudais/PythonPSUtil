import psutil
import requests
import simplejson as json

########## Définition des variables ##############
CPU= psutil.cpu_percent()

disk=psutil.disk_usage('/')[3]

host=psutil.net_if_addrs()

print(psutil.virtual_memory())

headers = {"Content-Type" : "application/json"}

############## Recherche de l'adresse IP ####################
for k, v in host.items():
    ip = v[0].address

host=ip

#################### Stockage des octets reçus depuis le début de la connexion ##############
network=psutil.net_io_counters(pernic=True)
key=list(network.keys())[:-1][0]
network=network[key].bytes_recv


####################### Envoie des données sous format JSON ###############
payload = {'CPU': CPU,'disk':disk,'Net':network}
data = json.dumps(payload)
try:
    r = requests.post("http://192.168.3.55:5000/collect", data=json.dumps(data),headers=headers)
    print(r.content)
    if r.status_code == 200:
        print("Code 200, connexion réussie !")
    else:
        print("Code différent de 200 !")
except:
    print("Erreur lors de la connexion")
