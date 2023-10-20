import requests
import time

headers = {
    'Authorization': 'Bearer 6d63bba91b51d2c51c73f2cf3c64b835',
}

liste_initiale = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()

while liste_initiale == nouvelle_liste:
    time.sleep(1)
    print('.', end='', flush=True)
    nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
    

print("nouveau planning publié !")

planning_id = nouvelle_liste[0]['id']
print(planning_id)
response_shift = requests.get(f'https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts', headers=headers)

# response_reservation = requests.post(f'https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts/{shift_id}/reservations', headers=headers)
# print(response_reservation.json())