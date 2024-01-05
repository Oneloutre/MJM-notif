from misc import connection
import pickle

cookies_file = 'session_cookies.pkl'


def main():

    username, password = connection.creds_check()
    print(username, password)
    response, session = connection.connection(username, password)

    if 'Ma carte d\'étudiant' in response.text:
            print('Connexion réussie!')
            with open(cookies_file, 'wb') as f:
                pickle.dump(session.cookies, f)
    else:
        print('Échec de la connexion. Vérifiez vos informations d\'identification.')


if __name__ == '__main__':
    main()