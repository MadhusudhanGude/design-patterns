from abc import ABC, abstractmethod

class Component(ABC):

    @abstractmethod
    def render(self, config={}):
        pass

class Button(Component):

    def render(self, config):
        print("You have created Button.")
        return '<button class="{0}" type="button"> {1} </button>'.format(
            config.get('class'), config.get('name'))

class TextBox(Component):

    def render(self, config):
        print("You have created TextBox.")
        return '<input type="text" id="{0}" name="{1}" minlength="{2}" maxlength="{3}">'.format(
            config.get('id'), config.get('name'),config.get('minlength'), config.get('maxlength'))



def GUIFactory(component_type='Button'):
    components = {
        "Button": Button,
        "TextBox": TextBox
    }
    return components[component_type]()

if __name__ == "__main__":
    config = [
            {
                'componentType': 'Button',
                'config': {
                    'class': 'custom_css_class',
                    'name': 'My Fav Button'
                }
            },
            {
                'componentType': 'TextBox',
                'config': {
                    'id': 'first_name',
                    'name': 'first_name',
                    'minlength': 2,
                    'maxlength': 20
                }
            }]
            
    for each_config in config:
        component = GUIFactory(each_config.get('componentType'))
        print(component.render(each_config.get('config')))