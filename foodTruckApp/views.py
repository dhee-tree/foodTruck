import requests
from decouple import config
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'trucks': get_contents(),
        'number_range': range(20),
    }
    return render(request, 'index.html', context)


def get_contents():
    url = config('SODA_API')

    # Send an HTTP GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()

        facility_dict = {}

        # write a for loop to iterate over the length of the data
        for i in range(len(data)):
            # add data to facility dict use i as the key and a list containing the facility type, latitude, and longitude as values
            facility_dict[i] = [data[i].get("facilitytype"), data[i].get("latitude"), data[i].get("longitude")]

        # print(facility_dict)

        # get the first 10 items from the facility dict
        # facility_dict = dict(list(facility_dict.items())[0:10])

        # get the truck with the key 10
        print(facility_dict[10])
        return facility_dict

    else:
        # If the request was not successful, print the status code
        print(f"Request failed with status code: {response.status_code}")


get_contents()
