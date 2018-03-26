Belt Exam (Python/Django) - Travel Buddy
Individual Belt Exam Project created 24 March 2018 and completed 25 March 2018

INTRODUCTION:
--------------------
This is a Django/Python project designed, built, and deployed to cloud services over a period of 2 days.

INTRO:
--------------------

-This application was built as part of a Coding Dojo belt exam culminating 2 months of material including HTML, CSS, JavaScript, 
jQuery, Ajax, Python, Flask, Django and the various was of using these technologies to develop a modern day application.  As the 
second belt exam we were given 48 hours to start and finsh an application including testing and deployment with the following requirements:

1. Login and Registration with validations. Validation errors should appear on the page. Logout as well. Password should be at least 8 characters.
2. Display the logged user's created/joined travel plans; also displays other users' travel plans. Display should be specific per user.
3. Ability to join other users' travel plans. Once the logged user joins, the travel plan record should move to the Trip Schedule tables and be removed from the other trips table.
4. Display of a particular travel plan which also indicates the list of users who joined that plan.
5. Ability to add new travel plans. Validation applies. The newly added travel plan should appear on logged user's Trip schedule table.
5. You must be able to deploy your work to Amazon EC2 and provide the IP address or subdomain/domain name to where your work has been deployed.

![Image of Yaktocat](http://mawfia.com/documents/python_django_belt.png)


HOW TO USE:
---------------------
Choose login or register, to login in use username: "test@test.com" password: "1qazZAQ!", or register to create an account.  After logging in or registering you will see all trips from eveyone with an account.  You can choose to join a trip or create your own.


TECHNOLOGY USED:
-----------------
1.  Python3.6.4 and MySQL were used for all back-end and data storage logic.

2.  A Virtual Environment was used to manage all module and library dependencies.

3.  CSS3 and HTML5 were used for initial form validation.

4.  Bcrypt was used as a salt/hash algorithm to obsfuscate each user's password stored in MySQL.

5.  Django, Nginx, and Gunicorn were used for server deployment, routing, and execution with data and template client-side service requests handled with Jinja2 and JavaScript.

6.  The application is deployed on a AWS account for cloud services including Ubuntu configuration and management.

This web application may be viewed at: http://54.201.84.245

Current Maintainer:
 * Michael Williams

This project has been sponsored by:
Coding Dojo

