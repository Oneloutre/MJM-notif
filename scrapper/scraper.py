import requests
import bs4
from datetime import datetime, timedelta


def recuperer_infos_etudiant(session):
    url = 'https://mjmcloud.com/etudiant/cahier-texte'
    response = session.post(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    infos = soup.find('div', {'class': 'portlet light calendar'}).findAll('input')
    type_utilisateur = infos[0]['value']
    utilisateur_id = infos[1]['value']
    inscription_id = infos[2]['value']
    classe_id = infos[3]['value']

    return(type_utilisateur, utilisateur_id, classe_id, inscription_id)

def recuperer_cahier_texte(session):
    url = 'https://mjmcloud.com/json_list/cahier-texte-json.php'
    date_start = datetime.now().strftime('%Y-%m-%d')
    date_end = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

    type_utilisateur, utilisateur_id, classe_id, inscription_id = recuperer_infos_etudiant(session)

    payload = {
        'utilisateur_type': type_utilisateur,
        'utilisateur_id': utilisateur_id,
        'classe_id': classe_id,
        'inscription_id': inscription_id,
        'start': date_start,
        'end': date_end
    }

    response = session.post(url, data=payload)

    return(response.json())


