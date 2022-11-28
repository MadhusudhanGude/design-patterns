from abc import ABC, abstractmethod

class Compoent(ABC):

    @abstractmethod
    def render(self):
        pass
    
class Button(Compoent):

    @abstractmethod
    def render(self):
        pass

class Checkbox(Compoent):

    @abstractmethod
    def render(self):
        pass

class MacOSButton(Button):

    def render(self):
        print("You have created MacOSButton.")

class WindowsButton(Button):

    def render(self):
        print("You have created WindowsButton.")

class MacOSCheckbox(Checkbox):

    def render(self):
        print("You have created MacOSCheckbox.")

class WindowsCheckbox(Checkbox):

    def render(self):
        print("You have created WindowsCheckbox.")

class GUIFactory(ABC):

    @abstractmethod
    def createButton(self):
        pass

    @abstractmethod
    def createCheckbox(self):
        pass


class MacOSFactory(GUIFactory):

    def createButton(self):
        return MacOSButton()

    def createCheckbox(self):
        return MacOSCheckbox()


class WindowsFactory(GUIFactory):

    def createButton(self):
        return WindowsButton()

    def createCheckbox(self):
        return WindowsCheckbox()


class Application(object):

    def __init__(self, factory):
        self.button = factory.createButton()
        self.checkbox = factory.createCheckbox()

    def render(self):
        self.button.render()
        self.checkbox.render()

if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    app = Application(MacOSFactory())
    app.render()

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    app = Application(WindowsFactory())

    app.render()
