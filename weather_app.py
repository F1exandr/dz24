import unittest
from weather_app import WeatherApp

class TestWeatherApp(unittest.TestCase):
    def test_get_weather(self):
        app = WeatherApp()
        weather = app.get_weather("Moscow")
        self.assertIsInstance(weather, dict)
        self.assertIn("temperature", weather)
        self.assertIn("description", weather)

if __name__ == "__main__":
    unittest.main()