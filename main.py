from misc import connection
from misc import webhook_handler
from scrapper import json_parser
import pickle


cookies_file = 'files/session_cookies.pkl'


def main():

    username, password = connection.creds_check()
    response, session = connection.connection(username, password)
    webhook = webhook_handler.webhook_check()

    if 'Ma carte d\'étudiant' in response.text:
            print('Connexion réussie!')
            #webhook_handler.webhook_send(webhook, 'Connexion réussie!')
            with open(cookies_file, 'wb') as f:
                pickle.dump(session.cookies, f)
    else:
        print('Échec de la connexion. Vérifiez vos informations d\'identification.')

    json_parser.parser(session, webhook)

if __name__ == '__main__':
    main()
