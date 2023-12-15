class TaxiPark:
    total_cars = []
    def sort_cost(self):
        index = 0
        while True:
            for i in range(len(self.total_cars) - 1):
                if self.total_cars[i][4] > self.total_cars[i + 1][4]:
                    self.total_cars[i][4], self.total_cars[i + 1][4] = self.total_cars[i + 1][4], self.total_cars[i][4]
                    index += 1
            if index == 0:
                break
        return self.total_cars

    def save_data(self):
        with open("Taxi_park", "w+") as fi:
            for car in self.total_cars:
                fi.write(','.join(str(item) for item in car) + "\n")
def print_file():
    with open("Taxi_park.txt", "r") as fi:
        stroki = fi.read().split(("\n"))
    return stroki

class Car(TaxiPark):
    def add_car(self, name, color, number, speed, cost, kf):
        new_car = [name, color, number, speed, cost, kf]
        self.total_cars.append(new_car)


economy_car = Car()
business_car = Car()
economy_car_2 = Car()
business_car_2 = Car()
economy_car_3 = Car()
economy_car.add_car("ВАЗ-2107", "Черный", 589, 57, 5, 100)
business_car.add_car("Mercedes-Benz S-Class", "Белый", 580, 69, 7, 110)
economy_car_2.add_car("Renault Logan", "Красный", 990, 90, 10, 120)
business_car_2.add_car("BMW 7 Series", "Синий", 989, 67, 11, 125)
economy_car_3.add_car("Toyota Camry", "Черный", 471, 80, 9, 115)

taxi_park = TaxiPark()
taxi_park.save_data()  # Вызов метода save_data() на экземпляре класса TaxiPark