# Libraries and Frameworks
An overview of each library & framework I've worked with in the past.


## JavaScript
Both ReactJS and Angular are scalable, modular, component-driven tools

### ReactJS (Library)
- Written in JavaScript
- Virtual DOM (faster update rendering)
- One-way data binding
- Complete backward compatibility
- Smaller bundle size
Note: Current most popular JS framework on StackOverflow (Aug 2020)

### Angular (Framework)
- Written in *TypeScript*, for static typing & annotations
- Real DOM (slower update rendering)
- Two-way data binding
- Must install updates sequentially
- Larger bundle size
Note: Angular 2, or Angular, is a rewrite of older framework AngularJS

### Node.js
- ExpressJS

### Other strong contenders
- VueJS (\#2)
- Express (Backend)
- JQuery



## Python/Ruby

### Django
- Monolith MVC framework
- Python is more readable and versatile
- Smaller learning curve
- More people experienced with Django - better tied with UVA curriculum
- More streamlined project structure
- Better database abstraction through view of models
- More flexibility - Handling of files, relationships between models, etc

### Ruby on Rails
- Monolith MVC framework
- Ruby is more verbose
- Less abstraction for db models
  - Rails has restrictive naming conventions
- http://danielhnyk.cz/django-vs-rails-for-beginner/ 



## CICD Tools

### Docker
- Tool for building/deploying applications in containers
  - **Containers** are isolated environments for applications
  - Less setup time than a VM
  - Shared OS - relies on host kernel’s functionality
- Solves this problem: Difference between development and production environments 
  - You can package your code into a Docker image, run and test it locally using Docker to guaranteed that the containers that were created from that Docker image will behave the same way in production


### TravisCI vs. GitHub Actions

### Kubernetes
- System for managing containerized applications in a clustered environment
- Automates the process of scaling, managing, updating and removing containers
- Kubernetes vs Docker
  - The former is meant to run across a cluster while the latter runs on a single node.
  - Can do any container, but benefits most from Docker 
  - https://containerjournal.com/topics/container-ecosystems/kubernetes-vs-docker-a-primer/


