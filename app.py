import requests

api_key = "b91a21c78dd9e104afa89a5d12f29311"
city = input("Enter city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
req = requests.get(url)
response = req.json()
print(response["weather"][0]["main"])

print(response["main"]["temp"])
