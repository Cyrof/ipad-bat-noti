import dotenv, requests, os

def get_cred():
    credName = ['TOKEN', 'CHATID', 'MSG']
    env_path = os.path.join(os.path.dirname("__file__"), ".env")
    dotenv.load_dotenv(env_path)

    cred = dict()
    for key in os.environ:
        if key in credName:
            cred[key] = os.environ[key]
    
    return cred

def send_tele_msg(cred):
    url = f'https://api.telegram.org/bot{cred["TOKEN"]}/sendMessage?chat_id={cred["CHATID"]}&text={cred["MSG"]}'
    requests.get(url)


if __name__ == "__main__":
    cred = get_cred()
    print(cred)
    send_tele_msg(cred)