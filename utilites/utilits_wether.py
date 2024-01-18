import requests

def get_weather(city_name):
    API = 'dd262aca3b857ede11b51f288a809dfa'
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=metric'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    req = requests.get(URL, headers=headers)
    if req.status_code == 200:
        data = req.json()
        return data.get('main').get('temp')
    else:
        return 'Такого города нет'

if __name__ == "__main__":
    print(get_weather('Златоуст'))