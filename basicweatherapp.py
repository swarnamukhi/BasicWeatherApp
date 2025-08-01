
import requests 


def get_weather(cityname):
    baseurl ="https://api.openweathermap.org/data/2.5/weather"
    appkey = "8d1ce897ab239abf2204a1b3585bfa55"

    params = {
        "q": cityname,
        "appid": appkey,
        "units" : "metric"
        }
    try:
        response = requests.get(baseurl,params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.HTTPError:
            return {"error": "❌ Invalid city name. Please try again."}
    except requests.exceptions.RequestException as e:
            return {"error" : f"Network error {e}"}
            
                    
def show_weather(data):
    if "error"  in data:
        print(data["error"])    
                      
    city= data.get("name","unknow")
    description = data["weather"][0]["description"]
    temparature =data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"📍city: {city}")
    print(f"🌦️Description :  {description}")
    print(f"🌡️Temparature : {temparature}°C")
    print(f"🥵 Feels_like : {feels_like}")
    print(f"💧Humidity : {humidity}")
    print(f"💨 wind_speed :  {wind_speed}")
                  
def main():
     print("welcome to the WEATHER APP")
    
     while True:
        cityname = input("please enter the name of the city or  (type exit to quit)")
        if cityname.lower() == 'exit':
            break
        data = get_weather(cityname)
        show_weather(data)

if __name__ == "__main__":
    main()


      

