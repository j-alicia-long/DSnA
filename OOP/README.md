# Object-Oriented Programming
OOP Fundamentals, mostly written in Java


## Abstraction
Hiding internal details to reduce design complexity
- Methods: Encapsulation, Inheritance


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


## Abstract class vs. Interface
