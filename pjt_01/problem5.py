import requests
from datetime import datetime, timedelta

# OpenWeatherMap API 키
API_KEY = 'e4daf0501f9047129b3343cacf2f350b'

def get_weather(city, api_key, date=None):
    if date:
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    else:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url).json()
    return response

def check_rain_chance(weather_data):
    rain_chance = weather_data.get('rain', {}).get('1h', 0)
    return rain_chance > 0

def recommend_nearby_area(api_key, city):
    # 부산의 예를 들면, 강수량이 적은 주변 지역을 추천합니다.
    # 이 부분은 예시로, 실제로는 특정 API나 데이터를 통해 주변 지역의 날씨를 확인해야 합니다.
    nearby_cities = ['Ulsan', 'Gyeongju', 'Changwon']
    min_rain = float('inf')
    best_city = None

    for nearby_city in nearby_cities:
        weather_data = get_weather(nearby_city, api_key)
        rain_chance = weather_data.get('rain', {}).get('1h', 0)
        if rain_chance < min_rain:
            min_rain = rain_chance
            best_city = nearby_city

    return best_city, min_rain

def find_next_dry_day(api_key, city, start_date):
    forecast_data = get_weather(city, api_key, date=True)
    forecast_list = forecast_data.get('list', [])
    
    for entry in forecast_list:
        dt = datetime.fromtimestamp(entry['dt'])
        rain = entry.get('rain', {}).get('3h', 0)
        if rain == 0 and dt > start_date:
            return dt.strftime('%Y-%m-%d')

    return "비가 그치는 날짜를 찾을 수 없습니다."

def main():
    departure_city = 'Busan'
    destination_city = 'Seoul'
    
    # 사용자로부터 입력 받기
    departure_date_str = input("부산에서 출발할 날짜를 입력하세요 (형식: YYYY-MM-DD): ")
    return_date_str = input("서울에서 돌아오는 날짜를 입력하세요 (형식: YYYY-MM-DD): ")

    try:
        departure_date = datetime.strptime(departure_date_str, '%Y-%m-%d')
        return_date = datetime.strptime(return_date_str, '%Y-%m-%d')
    except ValueError:
        print("날짜 형식이 올바르지 않습니다. 'YYYY-MM-DD' 형식으로 입력해주세요.")
        return

    # 서울의 날씨 예보를 가져옵니다.
    forecast_data = get_weather(destination_city, API_KEY, date=True)
    forecast_list = forecast_data.get('list', [])

    # 여행 기간 동안의 날씨를 확인하고 비 예보를 분석합니다.
    rain_warning = False
    for entry in forecast_list:
        dt = datetime.fromtimestamp(entry['dt'])
        if departure_date <= dt <= return_date:
            rain_chance = entry.get('rain', {}).get('3h', 0)
            if rain_chance > 0:
                rain_warning = True
                break

    if rain_warning:
        print("우산을 챙기셔야겠어요")
    else:
        print("당신의 운에 맡기세요")

    if rain_warning:
        best_area, min_rain = recommend_nearby_area(API_KEY, destination_city)
        print(f"비가 오는 예보가 확실한 경우, 강수량이 적은 주변 지역 추천: {best_area} (강수량: {min_rain}mm)")

    # 비가 그치는 날을 찾습니다.
    next_dry_day = find_next_dry_day(API_KEY, destination_city, return_date)
    print(f"비가 그치는 날: {next_dry_day}")

if __name__ == '__main__':
    main()


