from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for adding the different items to
    the Pizza objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass


    @abstractmethod
    def add_crust(self) -> None:
        pass

    @abstractmethod
    def add_chicken(self) -> None:
        pass

    @abstractmethod
    def add_onion(self) -> None:
        pass

    @abstractmethod
    def add_cheese(self) -> None:
        pass

    @abstractmethod
    def add_tomato(self) -> None:
        pass

    @abstractmethod
    def add_olives(self) -> None:
        pass

    
    @abstractmethod
    def add_capsicum(self) -> None:
        pass

class ConcreteBuilder(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def add_crust(self) -> None:
        self._product.add("Pizza crust with sauces")

    def add_chicken(self) -> None:
        # Logic to check if the item is available in the inventory.
        self._product.add("Chicken")

    def add_onion(self) -> None:
        self._product.add("Onion")

    def add_tomato(self) -> None:
        self._product.add("Tomato")

    def add_cheese(self) -> None:
        self._product.add("Cheese")

    def add_olives(self) -> None:
        self._product.add("Olives")

    def add_capsicum(self) -> None:
        self._product.add("Capsicum")


class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Pizza items: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_veg_pizza(self) -> None:
        self.builder.add_crust() 
        self.builder.add_onion()
        self.builder.add_tomato()

    def build_minimal_chicken_pizza(self) -> None:
        self.builder.add_crust()
        self.builder.add_chicken()
        self.builder.add_onion()
        
    def build_loaded_chicken_pizza(self) -> None:
        self.builder.add_crust()
        self.builder.add_chicken()
        self.builder.add_onion()
        self.builder.add_cheese()
        self.builder.add_olives()
        self.builder.add_capsicum()
        self.builder.add_tomato()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print("Standard veg pizza: ")
    director.build_minimal_veg_pizza()
    builder.product.list_parts()

    print("\n")

    print("Standard chicken pizza: ")
    director.build_minimal_chicken_pizza()
    builder.product.list_parts()

    print("\n")

    print("Loaded chicken pizza: ")
    director.build_loaded_chicken_pizza()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.add_crust() 
    builder.add_onion()
    builder.add_tomato()
    builder.add_capsicum()
    builder.add_cheese()
    builder.product.list_parts()
