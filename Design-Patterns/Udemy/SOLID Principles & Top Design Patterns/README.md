# Design Patterns

- Well-tessted, reusable solutions.
- Solution template for common software Engineering problems.
- Flexible & Adaptable.
- Common Meta-Language between developers.
- Carry over different programming languages.


## 1- Creatonal:
**Creational Design Patterns** manage ***object creaton*** mechnisms.
- Singleton Pattern
- Factory Method Pattern
- Builder Pattern

## 2- Structural:
**Structural Design Patterns** Deals with ways of managing complex object hierarchies.
- Adapter Pattern

## 3- Behavioral:
**Behavioral Design Patterns** Deals with ways of identifying and imporving object messaging with ***loosely coupled*** ways.
- Strategy Pattern
- Observer Pattern
- State Pattern

# UML
UML or `Unified Modeling Language`,is a standardized, general-purpose modeling language used in software engineering and systems engineering to visualize, specify, construct, and document the artifacts of a software system.


# Hallmarks of Good Architecture

## 1- Loose Coupling
Week knowledge association between components.
Changes to one component least affect existence or performanceo of another component.

## 2- Separaton of Concerns
Breaking your architecture into tiers. This can be done with `Modularization`, `Encapsulation` and `Arrangement` in software layers.
## 3- Law of Demeter (LoD)
A given object should assuem as little as possible about the structure or properties of anything else. It is also know as `Principle of Least Knowledge`.
- Each unit should have only limited knowledge about other units
- Each unit should only talk to its friends; don't talk to strangers.
- Only talk to your immediate friends.

## 4- SOLID

### Single Responsibility Principle
There should never be more than one reason for a class to change. Each class should only have only one central responsibility.

- Examples:
    ---
    - Persistence
    - Pre/Post Conditions - Validation
    - Notification
    - Logging
    - Formatting
    - Parsing (JSON, XML, CSV, ...)
    - Error Handling


### Open Closed Principle
Software entities should be open for extension, but closed for modification.
- Example:
Imagine we have a `Calculator Class` with 4 main methods, (`add`,`sub`,`mul`,`div`) and now we want a scientific claculator and a financial calculator, instead of changing the `Calculator Class` extend it and create 2 other classes such as `FinanceCalculator` and `ScienceCalculator`.

### Liskov Substitution Principle
Funcions that use pointers, or references to base classes, must be able to use objects of derived classes without knowing it.

### Interface egration Principle
Clients should not be forced to depend upon interfaces thay they do not use.
- Declaring methods in an interface that the caller doen't need pollutes the interface and leads to a `bulky` or `fat` interface.

### Dependency Inversion Principle
Depend upon abstractions, not concretions.