from misc import connection
from misc import webhook_handler
from scrapper import json_parser
import pickle
import os
from misc import update_checker
import schedule
import time
import functools


cookies_file = 'files/session_cookies.pkl'
webhook = webhook_handler.webhook_check()
log_webhook = webhook_handler.log_webhook_check()


def main():

    username, password = connection.creds_check()
    response, session = connection.connection(username, password)



    if 'Ma carte d\'étudiant' in response.text:
            print('Connexion réussie!')
            if os.path.exists('files/log_webhook.txt'):
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
            if os.path.exists('files/log_webhook.txt'):
                webhook_handler.simple_send(log_webhook, 'Erreur: Connexion échouée!')
            os.remove("files/creds.txt")
            os.remove("files/webhook.txt")
            main()



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Erreur: ' + str(e))
        if os.path.exists('files/log_webhook.txt'):
            webhook_handler.simple_send(log_webhook, 'Erreur: ' + str(e))
        main()
