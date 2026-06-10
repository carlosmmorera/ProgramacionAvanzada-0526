"""
Client class for the Open-Meteo Weather API.
https://api.open-meteo.com/v1/forecast
"""

import requests

# Carlos: Hago observaciones sobre el código, marcados
# con # INTERESTING. Sobre temas que son interesantes resaltar y 
# relacionados con lo que vimos en teoría + en los ejercicios de la clase 2.

class OpenMeteoClient:
    """Client for interacting with the Open-Meteo weather API."""

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    # INTERESTING: Para traducir de la codificación que usa la API
    # a algo más legible: le "ocultamos" la implementación interna de 
    # la API (es decir, los códigos numéricos que se usan por dentro),
    # a los clientes de la clase, que por un lado no entenderían esos 
    # códigos numéricos, y por otro lado no necesitan saberlo para nada.
    # Esto es uno de los principios de la programación orientada a objetos: 
    # ocultar detalles de implementación
    WEATHER_DESCRIPTIONS = {
        0: "Clear sky ☀️",
        1: "Mainly clear 🌤️",
        2: "Partly cloudy ⛅",
        3: "Overcast ☁️",
        45: "Fog 🌫️",
        48: "Depositing rime fog 🌫️❄️",
        51: "Light drizzle 🌦️",
        53: "Moderate drizzle 🌦️",
        55: "Dense drizzle 🌧️",
        61: "Light rain 🌧️",
        63: "Moderate rain 🌧️",
        65: "Heavy rain 🌧️🌧️",
        71: "Light snow 🌨️",
        73: "Moderate snow 🌨️",
        75: "Heavy snow ❄️❄️",
        80: "Light showers 🌦️",
        81: "Moderate showers 🌧️",
        82: "Violent showers ⛈️",
        95: "Thunderstorm ⛈️",
        96: "Thunderstorm with hail ⛈️🧊",
        99: "Severe thunderstorm with hail ⛈️🧊",
    }

    DEFAULT_CITIES = {
        "Madrid":    {"lat": 40.42, "lon": -3.70},
        "Barcelona": {"lat": 41.39, "lon": 2.17},
        "London":    {"lat": 51.51, "lon": -0.13},
        "Paris":     {"lat": 48.86, "lon": 2.35},
        "Berlin":    {"lat": 52.52, "lon": 13.41},
        "Rome":      {"lat": 41.90, "lon": 12.50},
    }

    def __init__(self, cities: dict | None = None):
        # INTERESTING: Das la opción a que el cliente pase las ciudades
        # que le interesen. Si no lo hace, se usan las ciudades por defecto. Esto es un ejemplo
        self.cities = cities or self.DEFAULT_CITIES

    def __get(self, params: dict) -> dict:
        # INTERESTING: Método auxiliar (privado) para hacer las llamadas
        # a la API, es decir, lo que es propiamente la request y el control
        # de la response. Se usa en otros métodos de la clase.
        """Make a GET request to the API and return the JSON response."""
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    def get_current_weather(self, name: str, lat: float, lon: float) -> dict:
        """Get current weather conditions for a single city."""
        data = self.__get({
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
            "timezone": "auto",
        })
        current = data["current"]
        # INTERESTING: Ocultas la estructura interna de la response, y ya
        # devuelves solamente los datos que realmente le interesan al cliente que ha llamado a 
        # este método de nuestra clase: el tiempo ACTUAL.
        return {
            "city": name,
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind_kmh": current["wind_speed_10m"],
            "weather_code": current["weather_code"],
        }

    def get_weekly_forecast(self, name: str, lat: float, lon: float) -> dict:
        """Get the 7-day daily forecast for a single city."""
        data = self.__get({
            "latitude": lat,
            "longitude": lon,
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
            "timezone": "auto",
            "forecast_days": 7,
        })
        daily = data["daily"]
        return {
            "city": name,
            "dates": daily["time"],
            "temp_max": daily["temperature_2m_max"],
            "temp_min": daily["temperature_2m_min"],
            "rain_prob": daily["precipitation_probability_max"],
        }

    def get_windiest_day(self, city: str, days: int) -> dict:
        """Get the windiest day and its max wind speed for a city over the next n days."""
        coords = self.cities[city]
        data = self.__get({
            "latitude": coords["lat"],
            "longitude": coords["lon"],
            "daily": "wind_speed_10m_max",
            "timezone": "auto",
            "forecast_days": days,
        })
        daily = data["daily"]
        dates = daily["time"]
        winds = daily["wind_speed_10m_max"]
        max_index = winds.index(max(winds))
        return {
            "city": city,
            "date": dates[max_index],
            "wind_speed_kmh": winds[max_index],
        }

    def interpret_weather_code(self, code: int) -> str:
        """Translate a WMO weather code into a human-readable description."""
        return self.WEATHER_DESCRIPTIONS.get(code, f"Unknown code ({code})")

    def get_all_current_weather(self) -> list[dict]:
        """Get current weather for all configured cities."""
        return [
            self.get_current_weather(name, coords["lat"], coords["lon"])
            for name, coords in self.cities.items()
        ]

    def get_all_weekly_forecasts(self) -> list[dict]:
        """Get 7-day forecasts for all configured cities."""
        return [
            self.get_weekly_forecast(name, coords["lat"], coords["lon"])
            for name, coords in self.cities.items()
        ]

    def get_temperature_ranking(self, current_data: list[dict]) -> list[dict]:
        """Return cities sorted by current temperature (warmest first)."""
        return sorted(current_data, key=lambda x: x["temperature"], reverse=True)

    def get_weekly_averages(self, forecasts: list[dict]) -> list[dict]:
        """Compute average max, min, overall temp and rain probability per city."""
        averages = []
        for fc in forecasts:
            avg_max = sum(fc["temp_max"]) / len(fc["temp_max"])
            avg_min = sum(fc["temp_min"]) / len(fc["temp_min"])
            avg_overall = (avg_max + avg_min) / 2
            avg_rain = sum(fc["rain_prob"]) / len(fc["rain_prob"])
            averages.append({
                "city": fc["city"],
                "avg_max": avg_max,
                "avg_min": avg_min,
                "avg_overall": avg_overall,
                "avg_rain": avg_rain,
            })
        return averages

    def get_weekly_summary(self, weekly_averages: list[dict]) -> dict:
        """Determine the warmest, coldest, rainiest and driest city of the week."""
        return {
            "warmest": max(weekly_averages, key=lambda x: x["avg_overall"]),
            "coldest": min(weekly_averages, key=lambda x: x["avg_overall"]),
            "rainiest": max(weekly_averages, key=lambda x: x["avg_rain"]),
            "driest": min(weekly_averages, key=lambda x: x["avg_rain"]),
        }


if __name__ == "__main__":
    client = OpenMeteoClient()

    # 1. Current weather
    print("=" * 60)
    print("  CURRENT WEATHER IN EUROPEAN CITIES")
    print("=" * 60)

    current_data = client.get_all_current_weather()
    for info in current_data:
        status = client.interpret_weather_code(info["weather_code"])
        print(f"\n📍 {info['city']}:")
        print(f"   Temperature: {info['temperature']} °C")
        print(f"   Humidity:    {info['humidity']} %")
        print(f"   Wind:        {info['wind_kmh']} km/h")
        print(f"   Condition:   {status}")

    # 2. Temperature ranking
    print("\n" + "=" * 60)
    print("  TEMPERATURE RANKING (warmest to coldest)")
    print("=" * 60)

    ranking = client.get_temperature_ranking(current_data)
    for i, info in enumerate(ranking, start=1):
        print(f"  {i}. {info['city']:12s} → {info['temperature']:5.1f} °C")

    difference = ranking[0]["temperature"] - ranking[-1]["temperature"]
    print(f"\n  Difference between warmest and coldest: {difference:.1f} °C")

    # 3. Weekly forecast averages
    print("\n" + "=" * 60)
    print("  WEEKLY FORECAST — AVERAGE TEMPERATURES")
    print("=" * 60)

    forecasts = client.get_all_weekly_forecasts()
    weekly_averages = client.get_weekly_averages(forecasts)

    for avg in weekly_averages:
        print(f"\n📍 {avg['city']}:")
        print(f"   Avg. max temp: {avg['avg_max']:5.1f} °C")
        print(f"   Avg. min temp: {avg['avg_min']:5.1f} °C")
        print(f"   Avg. temp:     {avg['avg_overall']:5.1f} °C")
        print(f"   Avg. rain prob: {avg['avg_rain']:4.0f} %")

    # 4. Weekly summary
    print("\n" + "=" * 60)
    print("  WEEKLY SUMMARY")
    print("=" * 60)

    summary = client.get_weekly_summary(weekly_averages)
    print(f"  🔥 Warmest city this week:   {summary['warmest']['city']} ({summary['warmest']['avg_overall']:.1f} °C)")
    print(f"  🥶 Coldest city this week:   {summary['coldest']['city']} ({summary['coldest']['avg_overall']:.1f} °C)")
    print(f"  🌧️  Rainiest city this week:  {summary['rainiest']['city']} ({summary['rainiest']['avg_rain']:.0f} % avg. prob.)")
    print(f"  ☀️  Driest city this week:    {summary['driest']['city']} ({summary['driest']['avg_rain']:.0f} % avg. prob.)")

    # 5. Day-by-day detail for warmest city
    warmest_name = summary["warmest"]["city"]
    print("\n" + "=" * 60)
    print(f"  DAY-BY-DAY DETAIL — {warmest_name.upper()}")
    print("=" * 60)

    fc_warmest = next(f for f in forecasts if f["city"] == warmest_name)
    print(f"  {'Date':<12} {'Max (°C)':>9} {'Min (°C)':>9} {'Rain (%)':>10}")
    print(f"  {'-'*12} {'-'*9} {'-'*9} {'-'*10}")
    for date, tmax, tmin, rain in zip(
        fc_warmest["dates"],
        fc_warmest["temp_max"],
        fc_warmest["temp_min"],
        fc_warmest["rain_prob"],
    ):
        print(f"  {date:<12} {tmax:>8.1f}  {tmin:>8.1f}  {rain:>8.0f} %")

    print("\n✅ All API calls completed successfully.")