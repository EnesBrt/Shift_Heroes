import requests
import time

headers = {
    'Authorization': 'Bearer 6d63bba91b51d2c51c73f2cf3c64b835',
}

try:
    liste_initiale = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
    nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
except requests.RequestException as e:
    print(f"Une erreur s'est produite : {e}")
    exit()

while liste_initiale == nouvelle_liste:
    try:
        time.sleep(1)
        print('.', end='', flush=True)
        nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
    except requests.RequestException as e:
        print(f"\nUne erreur s'est produite : {e}")
        exit()

print("\nnouveau planning publié !")

try:
    planning_id = nouvelle_liste[0]['id']
    response_shift = requests.get(f'https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts', headers=headers).json()
    print(response_shift)
except (IndexError, KeyError) as e:
    print(f"Une erreur s'est produite lors de l'accès aux données : {e}")
except requests.RequestException as e:
    print(f"Une erreur s'est produite : {e}")
