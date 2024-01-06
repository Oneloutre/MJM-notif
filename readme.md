# :bell:   MJM-notif   :bell:

------------------

![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) [![GitHub Repo](https://img.shields.io/badge/GitHub-Repo_link-green.svg)](https://github.com/Oneloutre/MJM-notif) ![Made with love](https://img.shields.io/badge/%E2%9D%A4%EF%B8%8F_Made_with-love-red) ![Logo Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

## Description :page_facing_up: :

Ma copine a souvent des devoirs ajoutés dans un "cahier de texte" sur son espace étudiant MJM mais elle n'a pas de notification quand ca arrive. Avec ce script, elle recevra les notifications directement sur discord.

Plus précisément, il s'agit d'un programme __server-side__ : il tourne sur un serveur et vous envoie des notifications sur Discord quand un devoir est ajouté sur MJM cloud.
Il ne s'agit donc **pas** d'une application graphique à ouvrir sur son ordinateur.

## Fonctionnement :gear: :

- le programme accède à la page des devoirs de MJM cloud grâce à vos identifiants
- tous les quart d'heure, il vérifie que la page n'a pas changé.
- si elle a changé, il envoie un message sur Discord pour vous prévenir via une webhook

voilà ce que peut faire le programme:

- [x] se connecter à MJM cloud
- [x] récupérer les devoirs
- [x] envoyer un message sur Discord quand des devoirs sont trouvés
- [x] afficher le contenu des devoirs
- [x] envoyer un message sur Discord quand un devoir est ajouté
- [x] vérifier tous les quarts d'heures que les devoirs n'ont pas changé

Si vous avez une suggestion, n'hésitez pas à ouvrir une issue !

## Installation :wrench: :

L'installation est très simple, il suffit de suivre les étapes suivantes :

```
git clone https://github.com/Oneloutre/MJM-notif.git
cd MJM-notif
pip install -r requirements.txt
```

:signal_strength: Python doit être >= 3.11 !!!! :signal_strength:

Une fois cela fait, vous pouvez lancer le programme avec la commande `python main.py`.
Le programme va vous demander vos identifiants (email et mdp mjm cloud) et [une webhook discord](https://support.discord.com/hc/fr/articles/228383668-Introduction-aux-Webhooks), puis un "daemon", donc le programme va tourner en arrière plan et vérifier toutes les quarts d'heure si des devoirs ont été ajoutés.

## Docker :whale: :

Vous pouvez également utiliser Docker pour lancer le programme.

Pour cela, il suffit de lancer la commande suivante :

```
docker build -t mjm-notif . && docker run -it --name mjm-notifier --restart always mjm-notif
```
le programme va vous demander vos identifiants et l'url de la webhook.
dès que vous les aurez entrés, le programme va tourner en arrière plan et vérifier toutes les quarts d'heure si des devoirs ont été ajoutés.

:warning: Attention, vous devez faire CTRL+P puis CTRL+Q pour quitter le container sans l'arrêter ! :warning:
## Contribuer :handshake: :

Si vous souhaitez contribuer au projet, vous pouvez ouvrir une issue ou une pull request. Je serai ravi de vous lire !

## Auteur :pencil: :

- Onelots (`onelots.` sur discord)

## Licence :scroll: :

[License MIT](https://choosealicense.com/licenses/mit/)
