<div align="center">

# 🌦️ Weather App

**Type a city, get the current conditions and temperature - powered by OpenWeatherMap and Streamlit.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-EB6E4B)

</div>

---

## ✨ Features

- 🔎 Enter any city name.
- 🌤️ Shows the current condition (Clear, Clouds, Rain, ...) and the temperature in °C.
- 🪟 Optional Windows launcher: type `weather` in `cmd` to start the app.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A free [OpenWeatherMap API key](https://openweathermap.org/api)

```bash
git clone https://github.com/Arashomranpour/weather.git
cd weather
pip install streamlit requests
```

Put your API key in `app.py` (`api_key = "..."`, preferably loaded from an environment variable), then:

```bash
streamlit run app.py
```

### Run as a command on Windows

1. Edit `weather.bat` so it points to the full path of `app.py`.
2. Copy `weather.bat` to a folder on your `PATH` (for example `C:\Windows\System32`).
3. Open `cmd` and type `weather`.

## 📁 Project Structure

```
.
├── app.py          # Streamlit weather UI
└── weather.bat     # Windows launcher
```

## 🛠️ Tech Stack

`Streamlit` · `requests` · `OpenWeatherMap API`
