import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY 에 해당하는 한글 KEY 값들은 다음과 같습니다.
    # feels_like : '체감온도',
    # humidity : '습도',
    # pressure : '기압',
    # temp : '온도',
    # temp_max : '최고온도',
    # temp_min : '최저온도',
    # description : '요약',
    # icon : '아이콘',
    # main : '핵심’
    # id : ‘식별자’

def get_weather(api_key):
    city = "Seoul,KR"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    response = requests.get(url).json()
    weather_data = {
    '기본': {
        '체감온도': response['main']['feels_like'],
        '습도': response['main']['humidity'],
        '기압': response['main']['pressure'],
        '온도': response['main']['temp'],
        '최고온도': response['main']['temp_max'],
        '최저온도': response['main']['temp_min'],
        },
    '날씨': {
            '아이콘': response['weather'][0]['icon'],
            '식별자': response['weather'][0]['id']
        },
        '요약': response['weather'][0]['description'], 
        '핵심': response['weather'][0]['main'],
    }
    
    return weather_data


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = 'e4daf0501f9047129b3343cacf2f350b'

    result = get_weather(api_key)
    pprint(result)

{'base': 'stations',
'clouds': {'all': 75},
'cod': 200,
'coord': {
    'lat': 37.5683, 
    'lon': 126.9778
    },
'dt': 1721364151,
'id': 1835848,
'main': {
    'feels_like': 306.77,
    'grnd_level': 999,
    'humidity': 62,
    'pressure': 1005,
    'sea_level': 1005,
    'temp': 303.34,
    'temp_max': 304.81,
    'temp_min': 301.84
    },
'name': 'Seoul',
'sys': {
    'country': 'KR',
    'id': 8105,
    'sunrise': 1721334325,
    'sunset': 1721386258,
    'type': 1
    },
'timezone': 32400,
'visibility': 10000,
'weather': [{'description': 'broken clouds',
'icon': '04d',
'id': 803,
'main': 'Clouds'}],
'wind': {'deg': 220, 'speed': 3.6}}




