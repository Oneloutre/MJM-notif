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


def log_webhook_check():
    try:
        if os.path.exists('files/log_webhook.txt'):
            with open('files/log_webhook.txt', 'r') as f:
                webhook = f.readline().strip()
            return webhook
    except Exception as e:
        print('Erreur: ' + str(e))
        exit(1)


def webhook_send(webhook, url_cours, title, color, start, end, description, prof):
    url = webhook
    data = {
        "embeds": [
        {
            "type": "rich",
            "title": "\nCours de " + prof + " du " + start + " au " + end,
            "description": description,
            "color": int(color.replace("#", ""), 16),
            "thumbnail": {
                "url": "https://storage.letudiant.fr/osp/cards/276/mjm-graphic-design-231102102947.jpg",
                "height": 0,
                "width": 0,
                },
            "author": {
                "name": title,
                "url": url_cours,
                "icon_url": "https://cdn-icons-png.flaticon.com/512/3378/3378118.png"
                },
            "footer": {
                "text": "Pour le " + start,
                "icon_url": "https://cdn.onelots.fr/u/VakI1n.png"
                     },
            }]
    }

    result = requests.post(url, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))


def simple_send(log_webhook, message):
    url = log_webhook
    data = {
        "embeds": [
        {
            "type": "rich",
            "description": message,
            "color": 0x000000,
            "thumbnail": {
                "url": "https://storage.letudiant.fr/osp/cards/276/mjm-graphic-design-231102102947.jpg",
                "height": 0,
                "width": 0,
                },
            "author": {
                "name": "MJM",
                "url": "https://mjmcloud.com",
                "icon_url": "https://cdn-icons-png.flaticon.com/512/462/462642.png"
                },
            "footer": {
                "text": "webhook de log",
                "icon_url": "https://cdn.onelots.fr/u/VakI1n.png"
                     },
            }]
    }

    requests.post(url, json=data)