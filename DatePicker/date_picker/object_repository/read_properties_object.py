from jproperties import Properties

class ReadPropertiesObject():
    def __init__(self,path):
        #self.object_constant=constant
        self.configs = Properties()
        self.object_properties=self.get_property_object(path)

    def get_property_object(self,path):
        with open(path,'rb') as config_file:
            self.configs.load(config_file)
        items_view = self.configs.items()
        object_properties = {}

        for item in items_view:
            object_properties[item[0]] = item[1].data
        return object_properties          

    def get_property(self,object_name):
        web_element=self.object_properties.get(object_name)
        locator_type=web_element.split(':>:')[0]
        locator_value=web_element.split(':>:')[1]
        return locator_type,locator_value
        
