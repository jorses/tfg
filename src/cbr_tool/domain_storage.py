import glob
import os
import json


class StoreDomain():

    def __init__(self, attribute_list, path=os.getcwd(), domain_name=None):
        """ Handy initialization """
        self.load(attribute_list, path, domain_name)

    def load(self, attribute_list, path, domain_name):
        """ Given a dataset searches for a domain in the specified folder.
            If found, loads it into the class itself. If not found loads an empty template.
        """

        for fnm in glob.glob(os.path.join(path, "*.json")):
            with open(fnm) as f:
                data = json.load(f)
            if data["attribute_list"] == attribute_list:
                self.modify(data)
                self.fnm = fnm
                break

        if not hasattr(self, "fnm"):
            print("No matching knowledge found for your domain, setting an empty one")
            self.attribute_list = attribute_list
            self.domain_name = domain_name or str(attribute_list)
            self.knowledge = {
                "dataset_stats": {},
                "column_stats": {}
            }
            self.fnm = glob.glob(os.path.join(path, str(self.domain_name)+".json"))

    def save(self):
        """ Saves itself as an object in .json format
        """

        print("" "", self.fnm)
        with open(self.fnm, 'w') as f:
            json.dump(self.__dict__, f)

    def modify(self, data):
        """ Modifies the class from a physical representation (dict) of it
        """

        self.domain_name = data["domain_name"] if "domain_name" in data else self.domain_name
        self.attribute_list = data["attribute_list"] if "attribute_list" in data else self.attribute_list
        self.knowledge = data["knowledge"] if "knowledge" in data else self.knowledge
        self.fnm = data["fnm"] if "fnm" in data else self.fnm

    def print_info(self):
        """ Util to print attributes
        """

        print(self.__dict__)
