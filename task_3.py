class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place > 100:
            print("Баллы начисляются только первым 100 участникам")
        elif place < 1:
            print("Спортсмен не может занять нулевое или отрицательное место")
        else:
            points = 101 - place
        return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if meters < 0:
            print("Количество метров не может быть отрицательным")
        else:
            points = meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total

points_for_place = PointsForPlace()

# Вывод: 91
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()

# Вывод: 5.0
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()

# Вывод: 91
print(total_points.get_points_for_place(10))

# Вывод: 5.0
print(total_points.get_points_for_meters(10))

# Вывод: 141.0 = (100 * 0.5) + 91
print(total_points.get_total_points(100, 10))
