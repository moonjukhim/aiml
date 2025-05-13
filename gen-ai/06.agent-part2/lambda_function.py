import json
import requests

def lambda_handler(event, context):
    # OpenWeatherMap API URL
    api_key = "[YOUR_API_KEY]"
        
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters',[])
    city = parameters[0]['value']
    print(city)

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
        # 날씨 API 호출
        response = requests.get(url)
        data = response.json()
        
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        response_body = {
            'TEXT' : {
                'body': f"Temperature: {temperature}K, Humidity: {humidity}%"
            }
        }

        function_response = {
            'actionGroup' : event['actionGroup'],
            'function' : event['function'],
            'parameters' : event.get('parameters', []),
            'functionResponse' : {
                'responseBody' : response_body
            }
        }

        session_attributes = event['sessionAttributes']
        prompt_session_attributes = event['promptSessionAttributes']

        # 날씨 정보 파싱
        if response.status_code == 200:
            temperature = data['main']['temp']
            #description = data['weather'][0]['description']
            weather_info = {
                'temperature': temperature,
            #    'description': description
            }

            action_response = {
                'messageVersion': '1.0', 
                'response': function_response,
                'sessionAttributes': session_attributes,
                'promptSessionAttributes': prompt_session_attributes
            }

            return action_response
            
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps({'error': 'Failed to retrieve weather data'})
            }
    
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
