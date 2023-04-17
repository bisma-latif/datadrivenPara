from pytest import fixture

import json

from selenium import webdriver

data_path = 'test_data.json'


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

# @fixture(params=[webdriver.Chrome])
# def browser(request):
#     driver = request.param
#     browsers = driver()
#     yield browsers
#     browsers.quit()

@fixture(params=load_test_data(data_path))
def test_data(request):
    data = request.param
    yield data


