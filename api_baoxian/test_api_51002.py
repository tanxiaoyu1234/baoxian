import pytest
import requests
from common.yaml_util import Yaml


class TestHuaTaiStart:

    def test_products_detail(self):
        print("1111111111111111111111")
        url = "https://bx.wts9999.net/insure/productDetail"
        params = {
            "productCode": "51002"
        }
        re = requests.get(url, params=params)
        print(re.json()["msg"] + "-----001")
        assert re.json()["msg"] == "request  success!"

    def test_process(self):
        print("222222222222222222222")
        url = "https://bx.wts9999.net/insure/process/51002"
        re = requests.post(url, json=None)
        print(re.json()["msg"] + "-----002")
        assert re.json()["msg"] == "request  success!"

    def test_start_policy(self):
        print("33333333333333333333")
        url = "https://bx.wts9999.net/insure/startPolicy"
        params = {
            "productCode": "51002"
        }
        json = {
            "channelSign":
                {"name": "CIN",
                 "app": "h5",
                 "params": "$$51002"}
        }
        re = requests.post(url, params=params, json=json)
        print(re.json()["msg"] + "-----003")
        yaml_json = {"insureUniqueId": re.json()["data"]["insureUniqueId"],
                      "nextStep":re.json()["data"]["nextStep"]}
        Yaml().yaml_write(yaml_json)
        assert re.json()["msg"] == "request  success!"


class TestHuaTaiSure:

    def test_modify_policy(self):
        print("444444444444444444444")
        yaml_json = Yaml().yaml_read()
        print(yaml_json["insureUniqueId"])
        url = "https://bx.wts9999.net/insure/modifyPolicy"
        params = {
            "insureUniqueId": yaml_json["insureUniqueId"],
            "gradeCode": "01"
        }
        re = requests.post(url, params=params, json=None)
        print(re.json()["msg"] + "-----003")
        assert re.json()["msg"] == "request  success!"


class TestPremium:

    def test_insure_process(self):
        print("555555555555555555555555555")
        yaml_json = Yaml().yaml_read()
        url = "https://bx.wts9999.net/insure/insureProcess"
        params = {
            "step": yaml_json["nextStep"],
            "insureUniqueId": yaml_json["insureUniqueId"]
        }
        re = requests.post(url, params=params, json={})
        print(re.json()["msg"] + "-----004")
        assert re.json()["msg"] == "request  success!"

