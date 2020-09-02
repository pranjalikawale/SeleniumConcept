from jproperties import Properties
#from utility.constant import Constant

class ReadObject():
    def __init__(self,constant):
        self.object_constant=constant
        self.configs = Properties()
        self.object_properties=self.get_property_object()

    def get_property_object(self):
        with open(self.object_constant.PATH_PROPERTY_FILE,'rb') as config_file:
            self.configs.load(config_file)
        items_view = self.configs.items()
        object_properties = {}

        for item in items_view:
            object_properties[item[0]] = item[1].data
        return object_properties            

    def get_property(self,object_name):
        return self.object_properties.get(object_name)


        