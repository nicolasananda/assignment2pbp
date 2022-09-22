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
After finishing all the steps we would need to upload all of it github by using the commands git add, git commit, and git push. After uploading, deploy it in heroku using the method in Lab 0


# WEEKLY ASSIGNMENT 3

Nicolas Ananda - 2106720973

[Heroku Link My Watch List](https://weeklyassignment2.herokuapp.com/mywatchlist/)

## Explain the difference between JSON, XML, and HTML!

The main difference between HTML, XML, and JSON can mainly be seen from 3 things, the structure, the content and the formatting. 

For JSON (JavaScript Object Notation) it is based from the JavaScript language and it utilizes similar code used for JavaScript Object, therefore making it easier to convert it to objects. Although JSON is based from JavaScript but it's format is text only making JSON to be able to be coded in any language.

HTML (HyperText Markup Language) is a language built for websites. It's content are structured making it being displayed neatly. It is usually written with tags that are able to present the amount of information displayed.


XML (eXtensible Markup Language), it is quite similar with HTML which uses tags to display information but the diffrence is XML is designed to transport data where as HTML is used to display it

## Explain why we need the data delivery when implementing on a platform!

Data delivery is necessary because how a client and server communicate with one another is primarily through data delivery. Data is returned by the server in response to a client request. For instance, the server will return an HTML file if the client (browser) requests an HTML page. In response to a request for raw data from the client (browser), the server will provide an XML or JSON file.

## Explain how you completed the tasks in this assignment

First, I created a new app called `mywatchlist` , then I added the URL path of `mywatchlist` in the `project_django/settings.py` and add `path('mywatchlist/', include('mywatchlist.urls')` in `project_django/urls.py` , then I created the models in `mywatchlist/models.py` after that I created 10 data entries in `mywatchlist/fixtures/initial_mywatchlist_data.json`, then I implement some codes in `mywatchlist/views.py` to show the data. Lastly, I pull,add , commit and push it to GitHub

## Postman API
![messageImage_1663776874635](https://user-images.githubusercontent.com/112491776/191635422-75f7d00e-3878-4fdf-90d4-fb49ee46aa39.jpg)

![messageImage_1663776844847](https://user-images.githubusercontent.com/112491776/191635536-9986508a-2a05-4114-b5fc-468b8796586a.jpg)

![messageImage_1663776827274](https://user-images.githubusercontent.com/112491776/191635544-74b70041-1a93-45d4-a3bf-b06a05066705.jpg)

