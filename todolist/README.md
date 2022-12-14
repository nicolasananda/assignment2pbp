# Assignment 4 Essay

https://weeklyassignment2.herokuapp.com/todolist/login/?next=/todolist/

## What does {% csrf_token %} do in the <form> element? What happens if there is no such "code snippet" in the <form> element? 
Cross-Site Request Forgery (CSRF) is an attack that forces authenticated users to submit a request to a Web application against which they are currently authenticated. CSRF attacks exploit the trust a Web application has in an authenticated user. (Conversely, cross-site scripting (XSS) attacks exploit the trust a user has in a particular Web application). A CSRF attack exploits a vulnerability in a Web application if it cannot differentiate between a request generated by an individual user and a request generated by a user without their consent.

## Can we create the <form> element manually (without using a generator like {{ form.as_table }})? Explain generally how to create <form> manually.
It is possible to create a form manually. The {{ form.as_table }} generator uses a Python file containing form objects as a reference to display in the HTML file, but you can also create the form directly in the HTML file itself.
  
## Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.
Data flows from forms where the user first enters the data, which is then later stored in the database model and then it will be passed to the HTML page. Then displaying it to the user
  
## Explain how you implement the checklist above.
1. Create an app called todolist
2. Add todolist into project_django settings and urls
3. Create the models in models.py
4. Run python manage.py makemigrations and python manage.py migrate
5. Create functions in views.py
6. Append url_patterns
7. Create todolist.html, login.html, register.html, create_task.html
6. Push, Add and Commit to Github and deploy to Heroku
