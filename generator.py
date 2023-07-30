import random
import string
import requests
import time

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def send_to_discord_webhook(webhook_url, message, mention_everyone=False):
    payload = {"content": message}
    if mention_everyone:
        payload["content"] = "@everyone " + payload["content"]
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, json=payload, headers=headers)
    if response.status_code == 204:
        print("Wysłano wiadomość do Discord Webhook!")
    else:
        print(f"Błąd podczas wysyłania wiadomości: {response.status_code} - {response.text}")

discord_webhook_url = "WEBHOOK"  # Tutaj podaj swój URL Discord Webhooka

while True:
    random_string = generate_random_string(16)
    file_name = f"discord.gift/{random_string}"

    print(file_name)  # Wypisz wynik przed wysłaniem do Discorda

    if "stracił ważność" in file_name or "został cofnięty" in file_name:
        send_to_discord_webhook(discord_webhook_url, file_name, mention_everyone=True) # Jeżeli gift będzie działał zostanie wysłana wzmianka @everyone
    else:
        send_to_discord_webhook(discord_webhook_url, file_name)

    time.sleep(x)  # Odczekaj x sekund przed kolejnym wygenerowaniem i wysłaniem wiadomości
