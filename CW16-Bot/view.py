import requests
from flask import request
from flask import jsonify
from app import app
from os import environ as env
from commands import is_command, run_command


SEND_MESSAGE = 'https://api.telegram.org/bot{}/getMe'

def get_api_key():
    api_key = '####'
    api_key = env.get('API_KEY')
    return api_key


def send_message(message):
    url = SEND_MESSAGE.format(get_api_key())
    resp = requests.post(url, json=message)
    return resp.json()


@app.route('/', method=['POST'])
def index():
    if request.method == 'POST':
        resp = request.get_json()
        chat_id = resp['message']['chat']['id']
        command = resp['message']['text'][1:].strip()

        if not is_command(command):
            return '<h1>Wrong Command</h1>'
        msg = run_command(command, chat_id)
        send_message(msg)

        return jsonify(resp)
    return '<h1> im bot </h1>'

# url = 'https://api.telegram.org/bot{}/getMe'.format(get_api_key())
# url2 = 'https://api.telegram.org/bot{}/getUpdates'.format(get_api_key())
# # ngrok
# res = requests.get(url2)

if __name__ == '__main__':
    print(res.json())