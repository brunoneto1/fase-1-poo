import requests
import json


api_key = '0KbJibxvNB2KQ0C0DcOuns53EL0vtFTK'


latitude = '-7.2305'
longitude = '-35.8811'


url = f'https://api.tomorrow.io/v4/timelines?location={latitude},{longitude}&timesteps=current&fields=temperature,humidity,windSpeed,rainIntensity,precipitationIntensity,pressureSurfaceLevel&apikey={api_key}'


response = requests.get(url)


if response.status_code == 200:
   
    data = response.json()

    
    selected_data = {
        'Temperature (°C)': data['data']['timelines'][0]['intervals'][0]['values']['temperature'],
        'Humidity (%)': data['data']['timelines'][0]['intervals'][0]['values']['humidity'],
        'Wind Speed (m/s)': data['data']['timelines'][0]['intervals'][0]['values']['windSpeed'],
        'Rain Intensity': data['data']['timelines'][0]['intervals'][0]['values']['rainIntensity'],
        'Precipitation Intensity': data['data']['timelines'][0]['intervals'][0]['values']['precipitationIntensity'],
        'Pressure Surface Level': data['data']['timelines'][0]['intervals'][0]['values']['pressureSurfaceLevel']
    }

    
    with open('dados_clima.json', 'w') as json_file:
        json.dump(selected_data, json_file, indent=4)

    print('Dados salvos em dados_clima.json')

else:
    print('Falha na solicitação à API')
