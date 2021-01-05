from tkinter import *
from requests import *
import requests

root = Tk()

def get_weather():
    city = city_field.get()

    key = '527ff4e42cb608c0d7b5003a0f30ae7c'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'

root['bg'] = '#fafafa'
root.title('Weather App')
root.geometry('400x300')

root.resizable(False, False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

city_field = Entry(frame_top, bg='white', font=30)
city_field.pack()

btn = Button(frame_top, text='Check the Weather', command=get_weather)
btn.pack()

info = Label(frame_bottom, text='Info', bg='#ffb700', font=40)
info.pack()

root.mainloop()
