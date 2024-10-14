class Compte:
    def __init__(self, nom, telefon, email, quantitat):
        self.nom = nom
        self.telefon = telefon
        self.email = email
        self.quantitat = float(quantitat)
            
    def imprimirDades(self):
        print (f"Nom: {self.nom}, Telefon: {self.telefon}, Email: {self.email}, Quantitat: {self.quantitat}€")
            
class Fixe(Compte):
    def __init__(self, nom, telefon, email, quantitat, plaç, interes):
        Compte.__init__(self, nom, telefon, email, quantitat)
        self.plaç = plaç
        self.interes = interes
            
    def obtenirInteres(self):
        return (self.quantitat * self.interes) /100
    
    def imprimir_dades(self):
        Compte.imprimirDades(self)
        print (f"Plaç: {self.plaç} mesos, Interès: {self.interes}%, Interès generat: {self.obtenirInteres()}€")
    
class Estalvi(Compte):
    def __init__(self, nom, telefon, email, quantitat, interes):
        Compte.__init__(self, nom, telefon, email, quantitat)
        self.interes = interes
        
    def mostrarEstalvis(self):
        return self.quantitat + (self.quantitat * self.interes) /100
    
    def imprimir_dades(self):
        Compte.imprimirDades(self)
        print (f"Interès: {self.interes}%, Estalvis totals: {self.mostrarEstalvis()}€")
        
#Creem una llista de clients array
clients = []

def afegirClient():
    nom = input("Nom: ")
    telefon = input("Telèfon: ")
    email = input("Email: ")
    quantitat = input("Quantitat: ")
    tipus = input("Tipus de compte (Fixe/Estalvi): ")

    if tipus.lower() == "fixe":
        plaç = int(input("Plaç (en mesos): "))
        interes = float(input("Interès (%): "))
        client = Fixe(nom, telefon, email, quantitat, plaç, interes)
    elif tipus.lower() == "estalvi":
        interes = float(input("Interès (%): "))
        client = Estalvi(nom, telefon, email, quantitat, interes)
    else:
        print("Tipus de compte no vàlid")
        return

    clients.append(client)
    print(f"Client {nom} afegit correctament!")


def llistarClients():
    for client in clients:
        client.imprimirDades()


def mostrarClient():
    nom = input("Introdueix el nom del client: ")
    for client in clients:
        if client.nom == nom:
            client.imprimirDades()
            return
    print("Client no trobat")


def buscarClient():
    nom = input("Introdueix el nom del client: ")
    for client in clients:
        if client.nom == nom:
            print(f"Client trobat: {client.nom}")
            return
    print("Client no trobat")


def modificarClient():
    nom = input("Introdueix el nom del client a modificar: ")
    for client in clients:
        if client.nom == nom:
            client.nom = input("Nou nom: ")
            client.telefon = input("Nou telefon: ")
            client.email = input("Nou email: ")
            client.quantitat = float(input("Nova quantitat: "))
            print(f"Client {client.nom} modificat correctament!")
            return
    print("Client no trobat")


def eliminarClient():
    nom = input("Introdueix el nom del client a eliminar: ")
    for client in clients:
        if client.nom == nom:
            clients.remove(client)
            print(f"Client {nom} eliminat correctament!")
            return
    print("Client no trobat")


# Funció del menú
def menu():
    while True:
        print("\nMenu")
        print("1. Afegir un client")
        print("2. Llistar clients")
        print("3. Mostrar les dades d'un client")
        print("4. Bucar client")
        print("5. Modificar un client")
        print("6. Eliminar un client")
        print("0. Sortir")
        opcio = input("Tria una opció: ")

        if opcio == "1":
            afegirClient()
        elif opcio == "2":
            llistarClients()
        elif opcio == "3":
            mostrarClient()
        elif opcio == "4":
            buscarClient()
        elif opcio == "5":
            modificarClient()
        elif opcio == "6":
            eliminarClient()
        elif opcio == "0":
            print("Sortint...")
            break
        else:
            print("Opció no vàlida")


# Executa el menú
menu()