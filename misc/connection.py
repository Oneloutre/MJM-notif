import requests
import pickle


def connection(username, password):
    url_login = 'https://mjmcloud.com/login.php'
    protected_url = 'https://mjmcloud.com/etudiant/cahier-texte'
    cookies_file = 'files/session_cookies.pkl'

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
