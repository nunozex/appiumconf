from ConvertElements import ConvertElements
# from DriverFactory import DriverFactory
import time


class CreateJavaPages:

    def __init__(self):
        converted_elements = ConvertElements()
        #self.driver = DriverFactory().get_driver()
        time.sleep(10)
        self.elements = converted_elements.format_elements()

    def get_element_by_type(self, element_type):
        elements_from_type = []
        if element_type != "TextView" and element_type != "EditText" and element_type != "Button" and \
                element_type != "ImageView":
            print("Please, choose a valid Element Type. Right now the types available are: TextView, "
                  "EditText, Button and ImageView.")
        else:
            for element in self.elements:
                if element.get("type") == element_type:
                    elements_from_type.append(element)
        return elements_from_type

    @staticmethod
    def get_find_element(element):
        if element.get("resource_id") != "":
            return "DriverFactory.getDriver().findElementById(\"" + element.get("resource_id") + "\");"
        elif element.get("content_desc") != "":
            return 'DriverFactory.getDriver().findElementByXPath("//android.widget.' + element.get("type") +\
                   '[@content-desc=\'' + element.get("content_desc") + '])'
        elif element.get("text") != "":
            return 'DriverFactory.getDriver().findElementByXPath("//android.widget.' + element.get("type") +\
                   '[@text=\'' + element.get("text") + '])'

    def create_click_element(self, element, java_class_name):
        file = open(java_class_name, "w")
        method_name = "Blabla"
        file.write("public void click" + element.get("type") + method_name + "(){\n")
        file.write("    element = " + self.get_find_element(element)  + "\n")
        file.write("    element.click();\n")
        file.write("}")
        file.close()


my_class = CreateJavaPages()
element = None
for elemento in my_class.get_element_by_type("ImageView"):
    element = elemento
my_class.create_click_element(element, "Oaoao.java")
