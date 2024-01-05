import requests
import pickle
import os

def connection(username, password):
    url_login = 'https://mjmcloud.com/login.php'
    protected_url = 'https://mjmcloud.com/etudiant/cahier-texte'
    cookies_file = 'session_cookies.pkl'

    session = requests.Session()

    try:
        with open(cookies_file, 'rb') as f:
            session.cookies.update(pickle.load(f))

        response = session.get(protected_url)

        if response.ok:
            print('Session chargée. Connexion persistante.')
        else:
            raise Exception('Session invalide. Connexion nécessaire.')

    except (FileNotFoundError, Exception):
        form_data = {
            'id_formulaire': '1',
            'username': username,
            'password': password
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        response = session.post(url_login, data=form_data, headers=headers)

    return response, session


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
