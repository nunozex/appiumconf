from DriverFactory import DriverFactory
import re


class ConvertElements:

    def __init__(self):
        self.driver = DriverFactory().get_driver()

    def get_xml(self):
        return self.driver.page_source

    def get_elements(self):
        element_pattern = re.compile("<android.widget[^>]*>")
        return re.findall(element_pattern, self.get_xml())

    def format_elements(self):
        text_pattern = re.compile('text="(.*?)"')
        type_pattern = re.compile('class="android.widget.(.*?)"')
        content_desc_pattern = re.compile('content-desc="(.*?)"')
        enable_pattern = re.compile('enabled="(.*?)"')
        selected_pattern = re.compile('selected="(.*?)"')
        bounds_pattern = re.compile('bounds="(.*?)"')
        resource_id_pattern = re.compile('resource-id="(.*?)"')

        elements = []

        for element_not_formated in self.get_elements():
            element = dict()
            element["text"] = re.search(text_pattern, element_not_formated).group(1)
            element["type"] = re.search(type_pattern, element_not_formated).group(1)
            element["content_desc"] = re.search(content_desc_pattern, element_not_formated).group(1)

            if re.search(enable_pattern, element_not_formated).group(1) == "true":
                element["enable"] = True
            else:
                element["enable"] = False

            if re.search(selected_pattern, element_not_formated).group(1) == "true":
                element["selected"] = True
            else:
                element["selected"] = False

            coord_pattern = "\[(\d+),(\d+)\]\[(\d+),(\d+)\]"
            bounds = re.search(bounds_pattern, element_not_formated).group(1)
            initial_x = int(re.search(coord_pattern, bounds).group(1))
            initial_y = int(re.search(coord_pattern, bounds).group(2))
            final_x = int(re.search(coord_pattern, bounds).group(3))
            final_y = int(re.search(coord_pattern, bounds).group(4))
            element["bounds"] = ((initial_x, initial_y), (final_x, final_y))

            element["resource_id"] = re.search(resource_id_pattern, element_not_formated).group(1)
            elements.append(element)
        return elements
