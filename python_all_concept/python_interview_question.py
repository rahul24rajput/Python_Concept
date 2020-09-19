# Django Web Development Technology Stack-Interview FAQ

This content is taken from ["Django Enterprise Development in Action"] (https://www.the5fire.com/983.html), this is the book that makes [大妈 （Zoom.Quiet)] (https: // github .com / ZoomQuiet) Review, suggestions from aunt.

The life cycle of the publication is relatively short. It is simply released on Github and gathers everyone's wisdom to build a reference that can be used by all who want to learn Python Web development or Django. Everyone checked for missing and filled vacancies, and further improved their "combat capability."

At present, only questions or knowledge points that may be asked, there is no corresponding answer. The answers are welcome to participate through issues.

Warehouse address: https://github.com/the5fire/django-interview-questions, welcome star, welcome contributions.

## 1. Python Basics

* Are you familiar with the basic syntax? introduce.
* What keywords are there and explain what they do?
* What are the built-in methods and explain what they do?
* Explain what is dynamic language? What does dynamic strong typing mean?
* Is there a concept of coding standards? Which coding standard is used?
* Explain deep and shallow copies
* Lambda usage and usage scenarios?
* Explain what a closure is and what it does?
* Implement a simple decorator to cache the results of a function?
* Differences and usage scenarios of several container types in Python?
* List comprehension use and scenario?
* The use of yield.
* What are the commonly used built-in libraries? Give examples of their usage.
* What are the "dunder methods" (magic methods) you know and what they do?
* Explain the concept of object-oriented and its role in programming?
* How to implement singleton pattern?
* How to serialize Python objects?
* Is it proficient in writing multi-threaded and multi-process programs?
* Use socket to write a simple HTTP Server, and return success successfully.
* How to understand GIL in Python? How does it affect our daily development?
* Explain the differences between coroutines, threads, and processes.


## 2. Django basics

#### the whole frame

* How to understand the MVC pattern in design patterns, how do you use this pattern in your daily life?
* How to understand the MTV model in Django?
* Introduce what modules are familiar to you in Django, and what are their functions?
* How to look at the Admin that comes with Django, and talk about your experience.
* How to understand the role of WSGI?
* How to implement the WSGI protocol yourself?
* Why don't you enable `` DEBUG = True '' configuration when officially deploying?

#### Model layer

* How do I understand what Django Migrations does?
* Have you ever experienced manual editing of Migrations files? What are the reasons and what should I pay attention to?
* Introduce the concept of ORM.
* How to understand the role of ORM in the Django framework?
* Introduce the N + 1 problem under ORM, the reason for it, and the solution.
* Introduce the role of Model in Django.
* What are the configurable items of the Meta attribute class of the Model, what is its role, and daily use.
* Introduce the role of QuerySet and your commonly used QuerySet optimization measures?
* Introduce the use of Pagination.
* Introduce the role of Field in Model.
* How to customize Manager? What scenarios need customization?
* Has the efficiency of Raw SQL been compared with the efficiency of ORM, and what are the results? How to understand this difference?
* What is the permission logic provided by Django and what is its granularity?

#### View layer

* What are the differences and application scenarios of function view and Class-based View in Django?
* How to add login required decorator to Class-based View?
* What is the role of Middleware in the Django system?
* What are the default configuration MIDDLEWARES in settings? What are their roles? Can it be removed?
* How does the Django system determine if a user is a logged-in user?
* How do I log in to a browser without cookies?
* What is the role of request and HttpResponse in Django?
* How to handle the image upload logic and display logic?
* Introducing the cache granularity of Django used.

#### Form layer

* Introduce the role of Form in Django.
* What is the relationship between Field in Form and Field in Model?
* How to verify a field in the Form layer?

#### Template layer

* How to understand the designer-friendly claims of Django templates?
* How to plan Django template inheritance and include in daily development?
* What are the commonly used tags and filters?
* What about static files in templates?
* How to handle the URL defined in the system in the template?
* How do I customize tags and filters?


## 3. Advanced Django

* How to troubleshoot performance issues with Django projects?
* How to deploy a Django project, and the differences between different deployment methods?
* How to handle static files in the project during deployment?
* How to implement custom login authentication logic?
* How to understand the relationship between Model, Form, ModelForm and Field, Widgets in Django?
* What is the principle of Paginator and how to implement the paging logic yourself?
* What is the role of Field in Model?
* What is SQL injection, and how does ORM solve this problem?
* What is the full name of CSRF? How does Django solve this problem?
* What does XSS attack mean and how should I avoid it during development?
* What is the function of Signal and its implementation logic?
* What is the role of the `` CONN_MAX_AGE '' parameter in the DATABASE configuration and the usage scenario?
* What is the implementation logic of `` CONN_MAX_AGE ''?
* Is it possible to create a user directly with Django's built-in User model: `` User (username = 'the5fire', password = 'the5fire'). Save () ''?
* What's wrong with the above creation method? What should I do with user passwords?
* How to implement user authentication login logic using Django-rest-framework?
* What is the role of the Session module in Django?
* How to customize the permission granularity in Django and implement your own permission logic?
* How to catch exceptions of online systems?
* How to analyze the problem that the response time of an interface is too long, assuming that the response time is 2 seconds, a request involves a database and cache query.


## 4. Deployment related

* How to automate the process of deploying a project to a production environment?
* What are the commonly used automated deployment tools?
* What monitoring tools are used, what are their functions, and what are their shortcomings?
* What does Supervisor do? Why use it?
* What does Gunicorn do? Why use it?
* How to stress test the system? And traffic estimates?
* What is the role of Nginx? Can it be configured independently? Do you have any optimization experience?
* What is the release logic and how can I ensure that the new version can be rolled back quickly when an exception occurs?


## 5. MySQL Database

* How do I determine which fields I need to index?
* When do I need to set the field attribute to `` unique = True ''?
* How to troubleshoot the index hit of a SQL statement?
* How to troubleshoot slow SQL statements?

## 6. Redis

* What are the characteristics of Redis you know? Why use it?
* Supported data types
* How to plan keys reasonably?
* For example, I need to write all the articles and classification data into Redis, and read the classification and article data directly from Redis in Django, and ask how to plan data storage and how to handle paging?
* Does it support transactions? for example.
* What are the data elimination strategies?
* When you find that some Redis queries take too long to respond, how to troubleshoot? What could be causing this?
* What is the deployment structure of Redis you use or understand?
* Do you know the persistence strategy of Redis, and what is the difference between different strategies?
* Talk about the Redis master-slave synchronization strategy you know.


## 7. Common Algorithms

* Dictionary type implementation algorithm in Python?
* What do you know about garbage collection in high-level languages? What is used in Python?
* Introduce the cache-related algorithms you know?
* Introduce the algorithms you know about load balancing?
* Introduce the database index related algorithms?


## 8. Summary

A lot of the content listed above is beyond the scope of Django, but it still belongs to the knowledge required in the field of web development.

As far as Django is concerned, it is just one of Python's many web development frameworks. Simply mastering the use of Django will not allow you to meet the needs of enterprises for web development. Therefore, take this book as your starting point for starting web development. After you have a solid grasp of Django, you can start from this and cover all aspects of web development.


*ad*

Jingdong: ["Guide to Effective and Effective Python Web Framework for Django Enterprise Development" (Hu Yang) [Summary of Book Review]-Jingdong Books] (https://item.jd.com/12537842.html)

Dangdang: [Guide to Practical and Efficient Python Web Frameworks for Django Enterprise Development] (http://product.dangdang.com/26509799.html)
