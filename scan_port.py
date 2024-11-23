import socket
from datetime import datetime

# Fonction pour scanner un port
def scan_port(host, port):
    try:
        # Créer un objet socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Fixer un délai de timeout de 2 secondes
        sock.settimeout(2)
        # Essayer de se connecter à l'hôte et au port
        result = sock.connect_ex((host, port))
        
        # Si result == 0, cela signifie que le port est ouvert
        if result == 0:
            print(f"Port {port} est ouvert")
        else:
            print(f"Port {port} est fermé")
        sock.close()
    except socket.error as err:
        # Si une erreur se produit lors de la tentative de connexion
        print(f"Erreur lors de la connexion au port {port}: {err}")
        return

# Fonction pour scanner une plage de ports
def scan_ports(host, start_port, end_port):
    print(f"Scanning de l'hôte {host} pour les ports ouverts entre {start_port} et {end_port}...")
    # Enregistrer l'heure de début pour mesurer la durée de l'analyse
    start_time = datetime.now()

    # Balayer tous les ports de la plage spécifiée
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

    # Mesurer le temps total de l'analyse
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\nScan terminé en: {duration}")

# Fonction principale pour exécuter le scanner
if __name__ == "__main__":
    # Demander à l'utilisateur l'adresse de l'hôte et la plage de ports
    target_host = input("Entrez l'adresse IP ou le domaine de l'hôte: ")
    start_port = int(input("Entrez le numéro du port de départ: "))
    end_port = int(input("Entrez le numéro du port de fin: "))

    # Vérifier que l'hôte est valide
    try:
        socket.gethostbyname(target_host)  # Valide l'adresse IP ou le domaine
    except socket.error:
        print(f"Erreur: L'adresse IP ou le domaine '{target_host}' est invalide.")
        exit(1)

    # Scanner les ports
    scan_ports(target_host, start_port, end_port)
