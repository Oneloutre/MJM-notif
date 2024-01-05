import os

def creds_check():
    try:
        if os.path.exists('creds.txt'):
            with open('creds.txt', 'r') as f:
                username = f.readline().strip()
                password = f.readline().strip()
            return username, password
        else:
            username = input('Nom d\'utilisateur: ')
            password = input('Mot de passe: ')
            with open('creds.txt', 'w') as f:
                f.write(username + '\n' + password)
            return username, password
    except Exception as e:
        print('Erreur: ' + str(e))
        exit(1)
