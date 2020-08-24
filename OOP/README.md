# Object-Oriented Programming
OOP Fundamentals, mostly written in Java

## What is OOP?
Object-oriented programming (OOP) allows for better understanding and maintenance of the code, particularly for big software. The four main pillars of OOP are:
* **Abstraction** - Modeling; hiding internal details
* **Encapsulation** - Data/method bundling & restricted access
* **Inheritance** - Code reuse
* **Polymorphism** - Different behavior within different contexts


## Abstraction
Hiding internal details to reduce design complexity
- Ex. Abstract class, interface
- Abstraction Methods: Encapsulation, Inheritance

### Abstract class vs. Interface
- An **abstract class** allows you to create functionality that subclasses can implement or override.
  - Allows code reuse with default functionality for subclasses
- An **interface** only allows you to define functionality, not implement it.
  - Achieve loose coupling by separating the definition of a method from the inheritance hierarchy


## Encapsulation
1) Bundling data and methods within one unit, to hide internal representation
- Ex. a class in Java
2) Access restriction to class members and objects
- Ex. private, protected, public


## Inheritance
Code reuse: A child class schema is created based on a parent class

### Multiple Inheritance
- One child inherits from two parent classes

In Python: Multiple inheritance is done as an ordered list (in the order of parents listed)
- Solves the diamond problem, where both parents inherit from the same grandparent and there is ambiguity in method override resolution.
![Diamond Inheritance](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Diamond_inheritance.svg/440px-Diamond_inheritance.svg.png)


## Polymorphism
Objects behave differently in different situations

### Compile-time Polymorphism (Static Dispatch)
- Method overloading
### Runtime Polymorphism (Dynamic Dispatch)
- Method overriding - a call to an overridden method is resolved at runtime


## Other OOP concepts
### Association
- Defines the multiplicity between objects
### Aggregation
- A special case of association
- Where objects have their own life cycle but there exists an ownership (“HAS-A”)
### Composition
- A special case of aggregation
- When the contained object in “HAS-A” relationship can’t exist on it’s own
