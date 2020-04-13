"""API request for the daily flight quotes.

Requires:
-requests
-json
-operator
"""
import requests
import json
from operator import itemgetter

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/PT/EUR/en-US/PT/GIG/2020-02"

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "APIKey"
}

response = requests.request("GET", url, headers=headers)

response = response.json()
total = response['Quotes'][-1]['QuoteId']

with open('record.json', 'w') as outfile:
    json.dump(response, outfile, indent=4)

rates = []

for i in range(0, total):

    date = response['Quotes'][i]['OutboundLeg']['DepartureDate']
    price = response['Quotes'][i]['MinPrice']

    origin = response['Quotes'][i]['OutboundLeg']['OriginId']

    dest = response['Quotes'][i]['OutboundLeg']['DestinationId']
    carrier = response['Quotes'][i]['OutboundLeg']['CarrierIds'][0]

    new_entry = {
        'Date': date[:10:],
        'Rate': price,
        'Origin': origin,
        'Destin': dest,
        'Carrier': carrier
    }
    rates.append(new_entry)


newRates = sorted(rates, key=itemgetter('Rate'))

for _ in range(0, len(newRates)):
    print(newRates[_])
