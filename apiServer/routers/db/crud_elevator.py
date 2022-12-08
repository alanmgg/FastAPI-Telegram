from . import schemas
from datetime import datetime
from datetime import timedelta
import requests
import json

import env

def get_date():
    now = datetime.now()
    date_time = str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    return date_time

def going_up_elevator():
    date_time = get_date()
    f = open('elevator.txt', 'a')
    f.write('El elevador subio ' + date_time + '\n')
    f.close()
    return

def going_down_elevator():
    date_time = get_date()
    f = open('elevator.txt', 'a')
    f.write('El elevador bajo ' + date_time + '\n')
    f.close()
    return

def send_file():
    url_updates = 'https://api.telegram.org/bot' + env.TOKEN_ID + '/getUpdates'
    url_document = 'https://api.telegram.org/bot' + env.TOKEN_ID + '/sendDocument'
    url_sticker = 'https://api.telegram.org/bot' + env.TOKEN_ID + '/sendSticker'
    url_message = 'https://api.telegram.org/bot' + env.TOKEN_ID + '/sendMessage'

    payload = {}
    files = []
    headers = {}
    
    response_updates = requests.request("GET", url_updates, headers=headers, data=payload)
    json_updates = json.loads(response_updates.text)

    date_time_now = datetime.now()
    date_time = json_updates['result'][-1]['message']['date']
    time_format = datetime.fromtimestamp(date_time)
    
    if (date_time_now - timedelta(minutes=5) < time_format) and (json_updates['result'][-1]['message']['text'] == '/envia'):
        try:
            payload = {'chat_id': json_updates['result'][-1]['message']['chat']['id']}
            files = [('document', ('elevator.txt', open('elevator.txt', 'rb'), 'text/plain'))]
            response_document = requests.request("POST", url_document, headers=headers, data=payload, files=files)
        
            payload = {'chat_id': json_updates['result'][-1]['message']['chat']['id'], 'sticker': env.STICKER}
            files = []
            response = requests.request("POST", url_sticker, headers=headers, data=payload, files=files)
        except:
            payload = {'chat_id': json_updates['result'][-1]['message']['chat']['id'], 'text': 'No existen registros de uso del elevador'}
            response = requests.request("POST", url_message, headers=headers, data=payload, files=files)
            return False
    else:
        payload = {'chat_id': json_updates['result'][-1]['message']['chat']['id'], 'text': 'Comando inválido'}
        response = requests.request("POST", url_message, headers=headers, data=payload, files=files)
        return False
        
    return True

def invalid_command():
    url_updates = 'https://api.telegram.org/bot' + env.TOKEN_ID + '/getUpdates'
    url_message = 'https://api.telegram.org/bot' + env.TOKEN_ID + '/sendMessage'

    payload = {}
    files = []
    headers = {}
    
    response_updates = requests.request("GET", url_updates, headers=headers, data=payload)
    json_updates = json.loads(response_updates.text)

    payload = {'chat_id': json_updates['result'][-1]['message']['chat']['id'], 'text': 'Comando inválido'}
    response = requests.request("POST", url_message, headers=headers, data=payload, files=files)

    return