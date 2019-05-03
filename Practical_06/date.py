class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}, {}, {}".format(self.day, self.month, self.year)

    def add_days(self, n):
        self.day += n