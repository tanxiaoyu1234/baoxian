import os
import yaml


class Yaml:

    # def yaml_path(self):
    #     cur_path = os.path.dirname(__file__)
    #     return cur_path + "/api_search.yaml"

    def yaml_read(self):
        with open("C:/Users/10441/PycharmProjects/baoxian/test_data/huatai_51002.yaml", mode='r', encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def yaml_write(self, data):
        with open("C:/Users/10441/PycharmProjects/baoxian/test_data/huatai_51002.yaml", mode='w', encoding="utf-8") as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    def yaml_clear(self):
        with open("C:/Users/10441/PycharmProjects/baoxian/test_data/huatai_51002.yaml", mode='w', encoding="utf-8") as f:
            f.truncate()
