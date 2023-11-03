
weather_data = {
    'january': {'temperature':27, 'daylight_hours': 1130},
    'february': {'temperature':30, 'daylight_hours': 1030},
    'march': {'temperature':39, 'daylight_hours': 12},
    'april': {'temperature':49, 'daylight_hours': 1330},
    'may': {'temperature':59, 'daylight_hours': 1430},
    'june': {'temperature':70, 'daylight_hours': 15},
    'july': {'temperature':76, 'daylight_hours': 1445},
    'august': {'temperature':75, 'daylight_hours': 14},
    'september': {'temperature':67, 'daylight_hours': 1230},
    'october': {'temperature':55, 'daylight_hours': 11},
    'november': {'temperature':43, 'daylight_hours': 945},
    'december': {'temperature':32, 'daylight_hours': 915},
}

def get_weather_data(month):
    return weather_data.get(month, None)


while True:
    user_input = input("Your Query? (e.g., 'whats the weather in May?')")
    user_input = user_input.strip().capitalize() 
    if user_input == 'Quit':
        break
    elif user_input.startswith("Whats the weather in "):
        month = user_input[20:-1]  
        weather_data = get_weather_data(month)
        if weather_data:
            temperature = weather_data['temperature']
            daylight_hours = weather_data['daylight_hours']
            print(f"Average temperature in {month}: {temperature}°C")
            print(f"Average daylight hours in {month}: {daylight_hours} hours")
        else:
            print(f"Sorry, I don't have data for {month}.")
    else:
        print("I'm not sure how to answer that. Please ask about the weather in a specific month or type 'quit' to exit.")