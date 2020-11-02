# family_expenses
kodilla mod.9 zad 2

The purpose of this app is to organise family expenses to optimise spending and drive frugal lifestyle. If you want to do just that feel free to clone the repository. Bear in mind that you will need Python v3.9 with modules as per file requirements.txt. 

The project consists of a table that shows what has been bought, in what quantity and for how much. To implement changes, use the form below the table. All data is saved in a json file and it is advisable to establish a timeframe, e.g. a month and track spending regularly. Personally, I clear out the table at the start of each month and begin to accumulate expenses for the new month. 

Data stored in the json file (expenses.json) can be altered by clicking on the date - each date contains a hyperlink to view with modification options to update any table row, if necessary.

Please note that the folder "family_expenses_API" contains ALTERNATIVE version of this application, i.e. is meant to be used instead of the previously described one, rather than complement it. It contains the same features and requires the same dependencies (see paragraph 1). However, there is no forms, the app in this version acts solely as API between client and server data, i.e. each feature can be accessed via HTTP methods (GET, POST, PUT, DELETE) only. To use this version, you will need to replace app.py and models.py with the equivalent files from this folder, forms.py and html templates being redundant, in this case. Also, it would make sense to use Postman or any such program that allows for sending API requests.

For the time being, the app lacks the feature of summing up of the expenses, this, however, is planned to change so the user will not have to do that on their own in the future, as this is obviously the point of it all. 

HOW TO USE 

1. Option - html forms in your browser:
a) clone the repository to your device.
b) install Python and dependencies as per requirements.txt. I recommend to do this in a virtual environment in the folder with the repository.
c) on the command line run "run.sh" in the directory with the program. This makes Flask to create a server on local host: http://localhost:5000/. You will be using the path: http://localhost:5000/expenses to access the forms.
d) to add expense use the table below heading "Insert a new expense". Fill in all rows. And submit using "Go" button.
e) to modify existing expense: click on the date, each date contains a hyperlink to the table that allows for modification of current expense.
f) all data is saved in expenses.json. If you want to clear out existing table from all expenses, just delete the file and start all over again. 

2. Option - API requests, no browser.
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

This will show you the expense with ID=1. If there is no such item with ID as in path, you will get error 404. This means there is no such item. 




