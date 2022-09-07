## Automated Testing
### Settings for testing in local environment
Having followed the instructions recomended in the course material, there was errors in connecting to Posgres database for testing. In order to use the Sqlite database instead, the following code was added.

In settings.py:
![](documentation/Test-screenshots/data-base.png)


In env.py (to toggle between the databases False for Postgres, True for Sqlite):
```
os.environ["DEVELOPMENT"] = "True"
```
Then run the migrations to update the database
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Unittest
Unittest was used for automated testing of the project. Urls, Models, and views were tested. A total test coverage of 85% was achieved.

![](documentation/test-screenshots/coverage-report.png)