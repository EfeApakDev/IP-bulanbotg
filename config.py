from os import path, getenv

class config:
    API_ID = int(getenv("29365506", "29365506"))
    API_HASH = getenv("0bacb8797f8ddc47529e41682b40d797", "0bacb8797f8ddc47529e41682b40d797")
    BOT_TOKEN = getenv("7294309547:AAGsWrbjHK3MY3wUADGgsChD59qkKDwxwxw", "7294309547:AAGsWrbjHK3MY3wUADGgsChD59qkKDwxwxw")
    IP_API =getenv("ACCESS_TOKEN","IP-API API KEY IS HERE")
    
con = config()
