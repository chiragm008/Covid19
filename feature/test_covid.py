import requests
import pytest
from endpoint.EndPointFactory import EndPoint



@pytest.mark.parametrize("country", EndPoint.test_country)
def test_ActiveCases(country):
    response = requests.get(EndPoint.Default + f"country/{country}" + EndPoint.Status1, params=EndPoint.ToDate, verify=False)
    print("Status Code= ", response.status_code)
    print("Request URL= ", response.url)
    TotalJsonList = response.json()
    RequiredJson = TotalJsonList[-1]
    TotalActiveCases = RequiredJson['Cases']
    print(f"Total Active Cases in {country}= ", TotalActiveCases)

@pytest.mark.parametrize("country", EndPoint.test_country)
def test_RecoveredCases(country):
    response = requests.get(EndPoint.Default + f"country/{country}" + EndPoint.Status2, params=EndPoint.ToDate, verify=False)
    print("Status Code= ", response.status_code)
    print("Request URL= ", response.url)
    TotalJsonList = response.json()
    RequiredJson = TotalJsonList[-1]
    TotalRecoveredCases = RequiredJson['Cases']
    print(f"Total Recovered Cases in {country}= ",TotalRecoveredCases)
