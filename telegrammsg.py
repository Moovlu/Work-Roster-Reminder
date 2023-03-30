import requests

def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()

if __name__ == "__main__":
    token = ""
    chat_id = ""
    message = "hello world"

    send_message(token, chat_id, message)