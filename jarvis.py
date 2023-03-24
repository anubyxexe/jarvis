#code avec le modele d'ia text-davinci-003 et le programme leo par anubyx comme modele
version = 0.5

#import
import openai
from colorama import Fore
import os
import time
import socket

openai.api_key = "openia api key"
context = "" #contexte de base


cont = " " #variable
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
    print("      Assistant intelligent V" + str(version))
    print()
logo()

#envoi de la requet
def chat(prompt):

    if(context == ""):
        cont = " "
    else:
        cont = " contexte: mes precedent message son les suivant (dans l'ordre chronologique); " + context + ", mes precedent message n'affecte pas forcement la reponse qui suis. "


    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt= "Identité : Tu es une intelligence artificielle nommée. \"jarvis\" en référence à l'assistant de Tony Stark dans le célèbre film Iron Man, Ton but est de m'assister dans ma vie quotidienne et tu as des connaissances infinies et tu excelles dans tous les domaines, tu parle francais." + cont + "command: si tu souhaite effacer le terminal ou que je te demande de clear repond juste \"[clear]\", si je te demande de te réinitialiser ou d'effacer ta memoire repond juste \"[reset]\". Question : " + prompt + " . (et évite de répondre avec trop de mots)",
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
        
        if("[Clear]" in response):
            os.system('cls' if os.name=='nt' else 'clear')
            logo()
        elif("[Reset]" in response):
            context = ""
            print(Fore.MAGENTA + "Jarvis s'est réinitialisé.")
        #a cause de ceratain bug
        elif("[reset]" in response):
            context = ""
            print(Fore.MAGENTA + "Jarvis s'est réinitialisé.")
        elif("[clear]" in response):
            os.system('cls' if os.name=='nt' else 'clear')
            logo()

        else:
            print(Fore.GREEN + f"jarvis: {response}")
            print()
            if(context == ""):
                context = context + "\"" + prompt + "\""
            else:
                context = context + ", \"" + prompt + "\""
