import random

def get_response(message: str) -> str:
    p_message = message.lower()
    saluting = p_message.encode("utf-8")

    if saluting == b'\xf0\x9f\xab\xa1':
        return
    else:
        return "I didn't understand what you wrote. Try typing '!help'."
