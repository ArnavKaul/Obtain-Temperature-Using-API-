import tkinter as tk
import requests

root=tk.Tk()

root.title("WEATHER API")
root.geometry("400x400")
city=tk.StringVar()
tk.Entry(root, textvariable=city).pack()

def get_weather():
    try:
      api_id="1ae150a47e5be607e1b7c64b47924566"

      url ="https://api.openweathermap.org/data/2.5/weather?q="+city.get()+"&appid="+api_id
      response=requests.get(url)

      #print(response.status_code)
      #print(response.text)

      weatherinfo = response.json()
      if weatherinfo['cod']==200:

         temp_kelvin=weatherinfo['main']['temp']
         temp_celsius=temp_kelvin-273
         temp_farhenheit=temp_celsius *(9/5) + 32
         tk.Label(text=str(temp_celsius)+"C").pack()
         tk.Label(text=str(temp_farhenheit)+"F").pack()
    except BaseException as e:
             tk.Label(text=f'ERROR: {e}').pack()


tk.Button(root,text="CHECK STATS",command=get_weather).pack()

root.mainloop()







