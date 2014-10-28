__author__ = 'reganjo'

class Flight:
    """
    """
# "SN070"
# from airtravel import Flight
    def __init__(self,number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Airline code is not upper in '{}'".format(number))
        if not number[2:].isdigit():
            raise ValueError("Flight number is not valid in '{}'".format(number))

        self._number=number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def test(self):
        from airtravel import Flight
        f=Flight("SN111")

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def num_rows(self):
        return self._num_rows

    def num_seats_per_row(self):
        return self._num_seats_per_row

    def seating_plan(self):
        return (range(1, self._num_rows+1),
                "ABCDEFGHIJK"[:self._num_seats_per_row])
