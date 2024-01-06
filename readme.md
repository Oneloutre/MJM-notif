# :bell:   MJM-notif   :bell:

------------------

![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) [![GitHub Repo](https://img.shields.io/badge/GitHub-Repo_link-green.svg)](https://github.com/Oneloutre/MJM-notif) ![Made with love](https://img.shields.io/badge/%E2%9D%A4%EF%B8%8F_Made_with-love-red) ![Logo Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

## Description :page_facing_up: :

J'ai beaucoup entendu ma copine se plaindre du fait que des devoirs apparaissaient sur MJM cloud sans qu'elle ne soit prévenue. J'ai donc décidé de lui faire un petit programme qui lui envoie une notification sur Discord quand un devoir est ajouté.

Plus précisément, il s'agit d'un programme __server-side__ : il tourne sur un serveur et vous envoie des notifications sur Discord quand un devoir est ajouté sur MJM cloud.
Il ne s'agit donc **pas** d'une application graphique à ouvrir sur son ordinateur.

## Fonctionnement :gear: :

- le programme accède à la page des devoirs de MJM cloud grâce à vos identifiants
- toutes les heures, il vérifie que la page n'a pas changé
- si elle a changé, il envoie un message sur Discord pour vous prévenir via une webhook

voilà ce que peut faire le programme pour l'instant :

- [x] se connecter à MJM cloud
- [x] récupérer les devoirs
- [x] envoyer un message sur Discord quand des devoirs sont trouvés
- [ ] afficher le contenu des devoirs
- [ ] envoyer un message sur Discord quand un devoir est ajouté

Si vous avez une suggestion, n'hésitez pas à ouvrir une issue !

## Installation :wrench: :

L'installation est très simple, il suffit de suivre les étapes suivantes :

```
git clone https://github.com/Oneloutre/MJM-notif.git
cd MJM-notif
pip install -r requirements.txt
```
Une fois cela fait, vous pouvez lancer le programme avec la commande `python main.py`.

## Docker :whale: :

Vous pouvez également utiliser Docker pour lancer le programme. Pour cela, il suffit de suivre les étapes suivantes :

```
docker build -t mjm-notif . && docker run mjm-notif
```
Quand le build est terminé, veillez à utiliser la commande `docker run -it mjm-notif bash` afin de vous connecter au container et de renseigner les informations nécessaires au fonctionnement du programme !

## Contribuer :handshake: :

Si vous souhaitez contribuer au projet, vous pouvez ouvrir une issue ou une pull request. Je serai ravi de vous lire !



## Licence :scroll: :

[License MIT](https://choosealicense.com/licenses/mit/)