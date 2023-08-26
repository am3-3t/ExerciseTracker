import datetime as dt
import requests
import os

today = dt.datetime.now()
today_date = today.date()
time = today.time().strftime('%H:%M')

app_id = os.environ.get('APP_ID')
app_id_2 = os.environ.get('APP_ID_2')
app_id_3 = os.environ.get('APP_ID_3')

query_input = input('input your excersie\n')

headers = {
    "x-app-id": app_id_3,
    'x-app-key': app_id,
    "Content-Type": "application/json"
}

headers2 = {
    'Authorization': os.environ.get('AUTHORIZATION')
}

end_point = ' https://trackapi.nutritionix.com/v2/natural/exercise'

parameters = {
    "query": f"{query_input}" 
}

response = requests.post(url=end_point, json=parameters, headers=headers)
data = response.json()

sheety_api = os.environ.get('SHEETY_API')
sheet_name =  'myWorkouts'
project = 'sheet1'

link = f"https://api.sheety.co/{sheety_api}/{sheet_name}/{project}"


for excercises in data['exercises']:
    add  = {
    f"{project}": {
        'date': f'{today_date}',
        'time': f'{time}',
        'exercise': f"{excercises['name']}",
        'duration': f"{excercises['duration_min']}",
        'calories': f"{excercises['nf_calories']}"
    }
}
    response2 = requests.post(url=link, json=add, headers=headers2)
    print(response2.text)