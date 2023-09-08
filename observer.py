class WeatherStation:

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

    def set_humidity(self, humidity):
        self.humidity = humidity
        self.notify_observers()


class TemperatureDisplay:

    def __init__(self, weather_station):
        self.weather_station = weather_station
        weather_station.register_observer(self)

    def update(self, temperature, humidity):
        self.temperature = temperature
        self.display()

    def display(self):
        print("Temperature: {} degrees Celsius".format(self.temperature))

class HumidityDisplay:
    def __init__(self, weather_station):
        self.weather_station = weather_station
        weather_station.register_observer(self)

    def update(self, temperature, humidity):
        self.humidity = humidity
        self.display()

    def display(self):
        print("Humidity: {}%".format(self.humidity))


if __name__ == "__main__":
    weather_station = WeatherStation()
    temperature_display = TemperatureDisplay(weather_station)
    humidity_display = HumidityDisplay(weather_station)
    weather_station.set_temperature(40)
    weather_station.set_humidity(20)
