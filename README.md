
Project located in FinalFinalProject Folder
HOW TO RUN PROGRAM:

1. Open up the FinalProject folder in VSCode
2. Open terminal
3. Go to the “FinalProject” directory
4. Install a virtual environment: pip install pipenv
5. to create a virtual environment run command: “pipenv shell”
6. Install django by running command: pipenv install django
7. Run 
- python manage.py makemigrations 
- python manage.py migrate
- python manage.py runserver

8. Sign up by entering user name and password, then hit submit
9. Login using the username and password you just created
10. Fill out your information on Profile Management Page, then hit Submit. You can visit this page at any time in order to edit your information.
11. Fill out information on Fuel Quote Form Page, hit “Get Quote” to see your Suggested Price per Gallon and Total Amount. Hit “Submit Quote” to submit your information
12. The Fuel Quote History will give you a view of all the Fuel Quote Forms you have submitted.

HOW TO VIEW DATABASE:
1. Open another terminal
2. Go to the “FinalProject” directory
3. To open the database, run Command: sqlite3  db.sqlite3
4. To see all the tables in the database, run Command: .tables
5. To see the content of each table, run command: select * from [table name];

HOW TO RUN UNIT TESTS:
1. Open another terminal/make sure pipenv shell is open
2. Go to the “FinalProject” directory
3. To run unit tests, run command: ./manage.py test


HOW TO RUN CODE COVERAGE REPORT:
1. Open another terminal
2. Go to the “FinalProject” directory
3. To install coverage, run command: pip install coverage
4. Run command: coverage run --source='.' manage.py test myapp
5. Run command: coverage report
6. before running a coverage report again, run command: “coverage erase”
	then start again from step 4.
