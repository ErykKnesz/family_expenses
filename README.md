# family_expenses

The purpose of this app is to organise family expenses to optimise spending and drive frugal lifestyle. If you want to do just that feel free to clone the repository. Bear in mind that you will need Python v3.9 with modules as per file requirements.txt. 

The project consists of a table that shows what has been bought, in what quantity and for how much. To implement changes, use the form below the table. All data is saved in a json file and it is advisable to establish a timeframe, e.g. a month and track spending regularly. Personally, I clear out the table at the start of each month and begin to accumulate expenses for the new month. 

Data stored in the json file (expenses.json) can be altered by clicking on the date - each date contains a hyperlink to view with modification options to update any table row, if necessary.

Please note that the folder "family_expenses_API" contains alternative version of this application. It contains the same features and requires the same dependencies (see paragraph 1). However, there is no forms, the app in this version acts solely as API between client and server data, i.e. each feature can be accessed via HTTP methods (GET, POST, PUT, DELETE) only. To use this version, run the Flask server in the folder "family_expenses_API" (make sure only one FLASK session is running, so you might need to close the session opened in folder ""family_expenses", if you have run it before). You will need to communicate with the server by HTTP requests, so it makes sense to use Postman or any such program that allows for sending API requests.

For the time being, the app lacks the feature of summing up of the expenses, this, however, is planned to change so the user will not have to do that on their own in the future, as this is obviously the point of it all. 

HOW TO USE 

1. Option - html forms in your browser:
a) clone the repository to your device.
b) install Python and dependencies as per requirements.txt. I recommend to do this in a virtual environment in the folder with the repository.
c) on the command line run Flask server in the directory with the program. This makes Flask to create a server on local host: http://localhost:5000/. You will be using the path: http://localhost:5000/expenses to access the forms.
d) to add expense use the table below heading "Insert a new expense". Fill in all rows. And submit using "Go" button.
e) to modify existing expense: click on the date, each date contains a hyperlink to the table that allows for modification of current expense.
f) all data is saved in expenses.json. If you want to clear out existing table from all expenses, just delete the file and start all over again. 

2. Option - API requests, no browser (Postman or other such tool required).
a) step a) and b) as in the first option. 
c) see point c) in first option, however, you will need to run it in folder "family_expenses_API" not in "family_expenses".
d) to add expense use request as in the following example (of course, it does not need to be a table...):
POST http://localhost:5000/api/v1/expenses/
Content-Type: application/json

{
    "date": "01.08.2020",
    "item": "table",
    "quantity": 1,
    "expense": 499
}

If you get 201 message, you successfully added new expense. If you get 400 - your data is wrong, check formatting and completeness as per above example.

e) To view a list of existing expenses:
GET http://localhost:5000/api/v1/todos/
Content-Type: application/json

f) To view a given expense seperately, add ID at the end of path, e.g:
GET http://localhost:5000/api/v1/todos/1
Content-Type: application/json

This will show you the expense with ID=1. If there is no such item with ID that you have entered, you will get error 404.

g) To delete a given expense, e.g. expense with ID=1, use:

DELETE http://localhost:5000/api/v1/todos/1

If you receive the following feedback, then your request has been successful:

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 21
Server: Werkzeug/1.0.1 Python/3.9.0
Date: Mon, 02 Nov 2020 17:37:36 GMT

{
  "result": true
}

h) you can also edit previously posted expense, by use of PUT http request, e.g.:

PUT http://localhost:5000/api/v1/expenses/1
Content-Type: application/json

  {
    "date": "28.02.2020",
    "expense": 3.5,
    "item": "cola",
    "quantity": 1
  }
  
 Just make sure you inlcude the id of the item in the path (in this example it's "1"). If you try to alter non-existent item, you will receive error 404. If you make a formatting mistake or fail to include all necessary key-value pairs, you will get error 400 message.

I attach my expenses.json file as an example. 
