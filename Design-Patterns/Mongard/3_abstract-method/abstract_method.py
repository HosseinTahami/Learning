"""
    Abstract Factory:
    
    - Provide an interface for creating related/dependent 
    objects without need to specify their actual class !

    Order Car --> 2 Companies and 2 Type

    Car ==> Company | Type
            -------  -------
            1. BMW  | 1. SUV
            2. Benz | 2. Coupe

        1. BMW / SUV ==> X1
        2. BMW / Coupe ==>  M2
        3. Benz / SUV ==> GLA
        4. Benz / Coupe ==> CLS
"""
from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def call_suv(self):
        ...

    @abstractmethod
    def call_coupe(self):
        ...


class Suv(ABC):
    @abstractmethod
    def create_suv(self):
        ...


class Coupe(ABC):
    @abstractmethod
    def create_coupe(self):
        ...
