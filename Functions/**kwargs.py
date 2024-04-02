
def sayData(**kwargs):

    for key, value in kwargs.items():

        # print(type(kwargs)) #return's the dict object.
        print(f"{key}: {value}");

sayData(name= "Amna")
sayData(name="Aman", password= 1234567)
sayData(name="Aman", password= 1234567, place= "Bazpur")