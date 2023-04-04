import requests

from st2common.runners.base_action import Action

class Pushover(Action):
    def __init__(self, config):
        self.client = Pushover(config['apikey'])

    def run(self, message, title, user_key, api_token):
        url = 'https://api.pushover.net/1/messages.json'
        data = {
            'token': api_token,
            'user': user_key,
            'message': message,
            'title': title,
        }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            return {'success': True}
        else:
            return {'success': False, 'error': response.text}

