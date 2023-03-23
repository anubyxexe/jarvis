#code avec le modele d'ia text-davinci-003 et le programme leo par anubyx comme modele

#import
import openai
from colorama import Fore
import os
import time
import socket

openai.api_key = "[open ai api key]"

#intro
print(Fore.MAGENTA + "test de connexion...")
time.sleep(0.5)
try:
    socket.create_connection(("www.google.com", 80))
    print(Fore.GREEN + "connexion reussite")
except OSError:
    print(Fore.RED + "[error] Vous n'êtes pas connecté à Internet")
    quit()
time.sleep(1.5)
os.system('cls' if os.name=='nt' else 'clear')

def logo():
    print(Fore.BLUE + "     __                   .__        ")
    print("    |__|____ __________  _|__| ______")
    print("    |  \__  \\\\_  __ \  \/ /  |/  ___/")
    print("    |  |/ __ \|  | \/\   /|  |\___ \ ")
    print("/\__|  (____  /__|    \_/ |__/____  >")
    print("\______|    \/                    \/ ")
    print("Assistant intelligent")
    print()
logo()

#envoi de la requet
def chat(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt= "Identité : Tu es une intelligence artificielle nommée. \"jarvis\" en référence à l'assistant de Tony Stark dans le célèbre film Iron Man, Ton but est de m'assister dans ma vie quotidienne et tu as des connaissances infinies et tu excelles dans tous les domaines. Question : " + prompt + " . (et évite de répondre avec trop de mots)",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


#input
while True:
    prompt = input(Fore.CYAN + "user-> ")
    if(prompt == "exit"):
        print(Fore.MAGENTA + "[exit] Jarvis te dit au revoir")
        quit()
    else:
        response = chat(prompt)
        print(Fore.GREEN + f"jarvis: {response}")
        print()
