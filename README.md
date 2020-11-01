# family_expenses
kodilla mod.9 zad 2

The purpose of this app is to organise family expenses to optimise spending and drive frugal lifestyle. If you want to do just that feel free to clone the repository. Bear in mind that you will need Python v3.9 with modules as per file requirements.txt. 

The project consists of a table that shows what has been bought, in what quantity and for how much. To implement changes, use the form below the table. All data is saved in a json file and it is advisable to establish a timeframe, e.g. a month and track spending regularly. Personally, I clear out the table at the start of each month and begin to accumulate expenses for the new month. 

Data stored in the json file (expenses.json) can be altered by clicking on the date - each date contains a hyperlink to view with modification options to update any table row, if necessary.

Please note that the folder "family_expenses_API" contains ALTERNATIVE version of this application, i.e. is meant to be used instead of the previously described one, rather than complement it. It contains the same features and requires the same dependencies (see paragraph 1). However, there is no forms, the app in this version acts solely as API between client and server data, i.e. each feature can be accessed via HTTP methods (GET, POST, PUT, DELETE) only. To use this version, you will need to replace app.py and models.py with the equivalent files from this folder, forms.py and html templates being redundant, in this case. Also, it would make sense to use Postman or any such program that allows for sending API requests.

For the time being, the app lacks the feature of summing up of the expenses, this, however, is planned to change so the user will not have to do that on their own in the future, as this is obviously the point of it all. 


