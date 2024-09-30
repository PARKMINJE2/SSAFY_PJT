import requests
from pprint import pprint

# 문제4. C번의 데이터를 활용하여, 섭씨 온도 데이터를 추가합니다.

# def celsius(kelvin):
#     temper = kelvin - 273.15
#     return temper



def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url).json()
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    weather_data = {
    '기본': {
        '습도': response['main']['humidity'],
        '기압': response['main']['pressure'],
        '온도': response['main']['temp'],
        '온도 (섭씨)': round(response['main']['temp'] -273.15,2),
        '체감온도': response['main']['feels_like'],
        '체감온도 (섭씨)': round(response['main']['feels_like'] -273.15,2),
        '최고온도': response['main']['temp_max'],
        '최고온도 (섭씨)': round(response['main']['temp_max'] -273.15,2),
        '최저온도': response['main']['temp_min'],
        '최저온도 (섭씨)': round(response['main']['temp_min'] -273.15,2),
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


# '온도 (섭씨)': response['main']['celsius(temp)'],
# '체감온도 (섭씨)': response['main']['celsius(feels_like)'],
# '최고온도 (섭씨)': response['main']['celsius(temp_max)'],
# '최저온도 (섭씨)': response['main']['celsius(temp_min)']


    # new_main = list(response['main'].items())  # list comprehension
    # new_weather = list(response['weather'][0].items())
    # new_list = new_main + new_weather

    # weather_data = {
    # '기본': {
    #     '체감온도': response['main']['feels_like'],
    #     '습도': response['main']['humidity'],
    #     '기압': response['main']['pressure'],
    #     '온도': response['main']['temp'],
    #     '최고온도': response['main']['temp_max'],
    #     '최저온도': response['main']['temp_min'],
    #     },
    # '날씨': {
    #         '아이콘': response['weather'][0]['icon'],
    #         '식별자': response['weather'][0]['id']
    #     },
    #     '요약': response['weather'][0]['description'], 
    #     '핵심': response['weather'][0]['main'],
    # }
    
    # return weather_data