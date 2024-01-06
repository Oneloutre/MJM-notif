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


def webhook_send(webhook, url_cours, title, color, start, end):
    url = webhook
    data = {
        "embeds": [
        {
            "type": "rich",
            "title": "Des devoirs ont été ajoutés !",
            "description": title,
            "color": int(color.replace("#", ""), 16),
            "thumbnail": {
                "url": "https://storage.letudiant.fr/osp/cards/276/mjm-graphic-design-231102102947.jpg",
                "height": 0,
                "width": 0,
                },
            "author": {
                "name": title,
                "url": url_cours,
                },
                "icon_url": "https://cdn.discordapp.com/guilds/749473022821400596/users/70569212453191698/avatars/1b3e0342e581ad0313ba94cf6043494a.webp",
            "footer": {
                "text": "Pour le " + start,
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
