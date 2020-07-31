import requests
import pytest
from endpoint.EndPointFactory import EndPoint


@pytest.mark.parametrize("date", EndPoint.Date)
@pytest.mark.parametrize("country", EndPoint.CountryCode)
def test_CovidCasesAndRecovered(date, country):
#Code to get the total number of cases and total recovered using a country code
    response = requests.get(EndPoint.BaseURI + EndPoint.StatusByCountryAndDate + f"{country}", params={"date": f"{date}"}, verify=False)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)
    data = response.json()
    print(data)
    TotalCases = data["cases"]
    TotalRecovered = data["recovered"]

#Code to get the country name using the given country code and to print the total and recovered cases
    response = requests.get(EndPoint.BaseURI + EndPoint.Country + f"{country}", verify=False)
    data1 = response.json()
    CountryName = data1["name"]
    print(f"Total Cases in {CountryName} as on {date} =", TotalCases)
    print(f"Total Recovered in {CountryName} as on {date} =", TotalRecovered)
    Data_Validate(country, date, TotalCases, TotalRecovered)



#function to validate the expected outcome using assert condition
def Data_Validate(country, date, TotalCases, TotalRecovered):
    if date == "2020-04-01":
        if country == "IN":
            assert TotalCases == 1998
            assert TotalRecovered == 148
        elif country == "IT":
            assert TotalCases == 110574
            assert TotalRecovered == 16847

    elif date == "2020/05/01":
        if country == "IN":
            assert TotalCases == 37257
            assert TotalRecovered == 10007
        elif country == "IT":
            assert TotalCases == 207428
            assert TotalRecovered == 78249

    elif date == "2020/06/01":
        if country == "IN":
            assert TotalCases == 198370
            assert TotalRecovered == 95754
        elif country == "IT":
            assert TotalCases == 233197
            assert TotalRecovered == 158355

    elif date == "2020/07/01":
        if country == "IN":
            assert TotalCases == 585493
            assert TotalRecovered == 347979
        elif country == "IT":
            assert TotalCases == 240760
            assert TotalRecovered == 190717

