import os
import requests

def webhook_check():
    try:
        if os.path.exists('files/webhook.txt'):
            with open('files/webhook.txt', 'r') as f:
                webhook = f.readline().strip()
            return webhook
        else:
            webhook = input('Webhook: ')
            with open('files/webhook.txt', 'w') as f:
                f.write(webhook)
            return webhook
    except Exception as e:
        print('Erreur: ' + str(e))
        exit(1)


def webhook_send(webhook, message):
    url = webhook
    data = {
        "embeds": [
            {
                "title": "Connexion réussie!",
                "description": message,
                "color": 65280
            }
        ]
    }
    requests.post(url, json=data)