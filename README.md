# WEEKLY ASSIGNMENT 2

Nicolas Ananda - 2106720973

[Heroku Link Katalog](https://weeklyassignment2.herokuapp.com/katalog/)

## Client's request and response to the Django Web Application.

Client ------> urls.py --------> views.py -----------> models.py ----------> Database -------> Template ------> Client


In conclusion, the client will submit requests to this application that are directed to a URL. When a request is made, Django checks to see if a corresponding response already exists before sending it to Views. The client will see a Template (which provides the output of the webpage) after Views have finished retrieving data from Models.py.

## Why do we use virtual environments?

For various applications, Python provides a wide range of modules and packages. We might need to install a third-party library for our project. The same directory is used for retrieval and storage by a different project that doesn't require any external packages. Because of this, each project can store and retrieve packages from its own isolated environment that was created for it using the virtual environment.

## Can we create a django web application without virtual environments?
Without virtual enviroment, it is definitely still possbile for a web application to be developed but it isn't efficient and messy, because when u install them at the default enviroment it could cause errors.

## Implementing Steps 1-4
## Step 1
First, i open views.py and write a fuction called show_catalog that will return the render function that will show the "Katalog.html" that contains the data on the variable "context"
## Step 2
This step will be used for routing the views function that will enable the HTML page to be displayed on the browser. Then, we add the variable "urlpatterns" from Lab 1 to the show_catalog function. Also we would need to register katalog in urls.py that is located on the project_django folder
## Step 3
At this step, display the list of items in a table then make a loop of list_item to access the data stored in models.py
## Step 4
After finishin all the steps we would need to upload all of it github by using the commands git add, git commit, and git push. After uploading, deploy it in heroku using the method in Lab 0


# WEEKLY ASSIGNMENT 3
