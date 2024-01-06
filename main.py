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


def main():

    username, password = connection.creds_check()
    response, session = connection.connection(username, password)
    webhook = webhook_handler.webhook_check()

    if 'Ma carte d\'étudiant' in response.text:
            print('Connexion réussie!')
            #webhook_handler.webhook_send(webhook, 'Connexion réussie!')
            json_parser.parser(session, webhook)
            with open(cookies_file, 'wb') as f:
                pickle.dump(session.cookies, f)
            scheduler = schedule.Scheduler()
            scheduler.every(15).minutes.do(functools.partial(update_checker.comparer_devoirs_json, session))

            while True:
                scheduler.run_pending()
                time.sleep(10)
    else:
        os.remove("files/session_cookies.pkl")
        main()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Erreur: ' + str(e))

        main()
