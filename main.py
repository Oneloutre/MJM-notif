from misc import connection
from misc import webhook_handler
from scrapper import json_parser
import pickle
import os
from misc import update_checker
import schedule
import time
import functools
from dotenv import load_dotenv
load_dotenv()

cookies_file = 'files/session_cookies.pkl'
webhook = os.environ['WEBHOOK']
log_webhook = os.environ['WEBHOOK_LOG']
username = os.environ['EMAIL']
password = os.environ['PASS']


def main():

    response, session = connection.connection(username, password)

    if 'Ma carte d\'étudiant' in response.text:
            print('Connexion réussie!')
            webhook_handler.simple_send(log_webhook, 'Connexion réussie!')
            json_parser.parser(session, webhook)
            with open(cookies_file, 'wb') as f:
                pickle.dump(session.cookies, f)
            scheduler = schedule.Scheduler()
            scheduler.every(15).minutes.do(functools.partial(update_checker.comparer_devoirs_json, session, log_webhook))

            while True:
                scheduler.run_pending()
                time.sleep(10)
    else:
        if os.path.exists(cookies_file):
            os.remove("files/session_cookies.pkl")
            main()
        else:
            print('Erreur: Connexion échouée!')
            webhook_handler.simple_send(log_webhook, 'Erreur: Connexion échouée!')
            main()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Erreur: ' + str(e))
        webhook_handler.simple_send(log_webhook, 'Erreur: ' + str(e))
        main()
