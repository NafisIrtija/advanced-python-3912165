# Example file for Advanced Python by Joe Marini
# Programming challenge for working with Exceptions

# Implement the InvalidTempError exception class here
class InvalidTempError(Exception):
    """Raised if the temperature is set below 100 degrees or above 500 degrees"""
    def __init__(self, temp):
        if temp < 100:
            message = "The temperature is below 100 degrees"
        else:
            message = "The temperature is above 500 degrees"
        super().__init__(message)


class DigitalOven:
    def __init__(self):
        self.temp = 0

    def set_temp(self, temp):
        if (temp < 100 and temp != 0) or temp > 500:
            raise InvalidTempError(temp)
        self.temp = temp

    def get_temp(self):
        return self.temp

def test_oven(test_temp):
    global oven
    try:
        oven.set_temp(test_temp)
    except InvalidTempError as e:
        print("Error: ", e)
    else:
        print(f"Temperature is successfully set to {oven.get_temp()}")
    finally:
        print(f"Current temp setting is {oven.get_temp()}")

# An "InvalidTempError" Exception should be raised if the temperature
# is set below 100 degrees or above 500 degrees
oven = DigitalOven()
test_oven(250)
test_oven(50)
test_oven(0)
test_oven(600)
