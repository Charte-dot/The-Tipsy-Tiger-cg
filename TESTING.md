## Automated Testing
### Settings for testing in local environment
Having followed the instructions recomended in the course material, there was errors in connecting to Posgres database for testing. In order to use the Sqlite database instead, the following code was added.

In settings.py:
![](documentation/test-screenshots/data-base.png)


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

## Manual Testing
The project was thoroughly tested by the developer and multiple user from friends and family members. Following User stories created the steps and results are as follows.

### Testing User Stories
#### Epic: 
Set up an admin page to manage posts, reviews, comments and user.
To test the admin page created to fulfill this epic begin with the following steps:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Click on the 'Sign In' tab on the navigation bar.
3. Sign in with admin credientials
4. Navigate to [admin page](https://the-tipsy-tiger.herokuapp.com/admin)

### *User Story*
* As an admin I can post content so that there is a decent library of recipes.( Must have / completed)[#1](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/1)

Description: The admin can create and post content to keep site updated.

**Testing steps**
1. In the admin panel on the left side of the page, click add button under the recipe heading.
2. In the recipe form, enter content in each field.
3. Click save to create the cocktail recipe.

![](documentation/User-story-ss/admin-ss.png)

**Expected Result**: A cocktail recipe is saved by default to the list of recipes in the admin panel.

**Actual Result**: A cocktail recipe is saved to the admin panel.

![](documentation/User-story-ss/admin-ss2.png)

**Pass/Fail: Pass**

### *User Story*
* As an admin I can approve content so that the it's only relevant content posted.( must have / completed)
[#2](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/2)

Description: The site admin is able to create, read, update and delete cocktails.

**Testing steps**
* To create a recipe:
1. in the admin panel menu on the left click add button on the recipe catagory.

![](documentation/User-story-ss/admin-ss3.png)

2. In the recipe form enter contents of chosen cockatail.
3. Change the status to published in the dropdown menu.
4. Click save to created the cocktail recipe.

**Expected result**: The recipe is saved as 'published' to the list of recipes and viewable on the main site.

**Actual Results**: The recipe is saved as 'published' to the list of recipes and viewable on the main site.
**Pass/Fail: Pass**

* To read/update a recipe:

1. In the admin panel list select a recipe title to read the full recipe.
2. To update the recipe update the fields required and click save.

**Expected Result**: The viewed/updated recipe is saved to the list of recipes.
**Actual Result**: The viewed/updated recipe is saved to the list of recipes
**Pass/Fail: Pass**

* To delete a recipe:
1. To delete a recipe in the admin panel, selected the recipe to be deleted in the checkbox beside the title.
2. In the action dropdown menu above the list select 'delete' and 'go' to delete the recipe.

**Expected Result**: The viewed/deleted recipe is deleted from the admin panel and not viewable on the main site.
**Actual Results**:The viewed/deleted recipe is deleted from the admin panel and not viewable on the main site.
**Pass/Fail: Pass**

### *User Story*
As an admin I can approve comments so that I can filter inappropriate content.( must have/ completed)[#3](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/3)

![](documentation/User-story-ss/verified-content.png)

**Testing steps**:
1. In the admin panel select comments to view a list of draft and published comments.
2. In the list select a review in the checkbox.
3. In the action dropdown menu above the list select 'approve selected comment' or 'delete selected comment' then 'go'.

**Expected Results**:
1. The approved comment is published on the website.
2. The unapproved comment is removed from the list of comments.

**Actual Results**: 
1. The approved comment is published on the website.
2. The unapproved comment is removed from the list of comments.
**Pass/Fail: Pass**

#### Epic: 
Enable users to set up an accounton the website to access the full features.
#### *User Story*:
* As a user I can register an account so that I can access the full range of features on the site (must-have)
[#4](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/4)

**Testing Steps**:
1.  Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Click on the 'register' tab on the navigation menu.
3. Create an account with username, email(optional) and password.

**Expected Results**:
1. Message displays 'You have successfully signed in'.
2. Sign in link in the navigation changes to Sign Out.
3. My cocktails tab is now displayed in the navigation bar.

**Actual Results**: 
1. Message displays 'You have successfully signed in'.
2. Sign in link in the navigation changes to Sign Out.
3. My cocktails tab is now displayed in the navigation bar.
**Pass/Fail: Pass**

![](documentation/User-story-ss/register-form.png)
*Registration form*

![](documentation/User-story-ss/sign-in-pop.png)
*Sign in message*


