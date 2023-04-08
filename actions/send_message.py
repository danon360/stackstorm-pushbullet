import requests

from st2common.runners.base_action import Action

class Pushover(Action):
    key = ""
    def __init__(self, config):
        self.key = config['api_key']

    def run(self, message, title, user_key):
        url = 'https://api.pushover.net/1/messages.json'
        data = {
            'token': self.key,
            'user': user_key,
            'message': message,
            'title': title,
        }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            return {'success': True}
        else:
            return {'success': False, 'error': response.text}

