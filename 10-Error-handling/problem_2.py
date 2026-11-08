class ScoreCalculator:
    def __init__(self, name):
        self.name = name

    def calculate_score(self, total_points, matches):
        total_points = int(total_points)
        matches = int(matches)

        if matches == 0:
            raise ZeroDivisionError("Matches must be greater than zero")

        return total_points / matches


sc = ScoreCalculator("leo")

try:
    result = sc.calculate_score(1000,10)

except ValueError as e:
    print("Invalid numeric input:", e)

except ZeroDivisionError as e:
    print("Invalid matches:", e)

except TypeError as e:
    print("Invalid data type:", e)

else:
    print("Calculated successfully:", result)

finally:
    print("Calculation completed")