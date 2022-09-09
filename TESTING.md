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
### Epic: Set up an admin page to manage posts, reviews, comments and user.
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

### Epic: Enable users to set up an accounton the website to access the full features.
#### *User Story*:
* As a user I can register an account so that I can access the full range of features on the site (must-have / completed)
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

#### *User Story:
*As a user I can login and logout to the site so that I can access my content and interact with other users content.(Must Have / completed)[#5](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/5)

**Testing Steps**:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Click on the 'Sign in' link in the navigation bar and sign in with username and password.
3. Click on the 'Sign out' link on the naviagtion bar.

**Expected Results**:
1. Message displays 'You have successfully signed in'.
2. Message displays 'You have signed out'.
3. The sign in link changes to sign in/sign out depending on users action.

**Actual Results**:
1. Message displays 'You have successfully signed in'.
2. Message displays 'You have signed out'.
3. The sign in link changes to sign in/sign out depending on users action.
**Pass/Fail: Pass**

![](documentation/User-story-ss/sign-in-pop.png)
*Sign in message*

![](documentation/User-story-ss/sign-out-pop.png)
*Sign out message*

![](documentation/User-story-ss/home-nav.png)

*Signed in view to user*

### *User Story*:
*As an admin I can set an age verification so that underage users can't access alcohol based topics. ( Must Have / complete)
[#6](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/6)

**Testing Steps**:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. If the user is over 18 click 'I am over 18' button and access is granted to site.
3. If user is under 18 click ' I am not over 18' button and is redirected to a decline page.

**Expected Results**:
1. If user is over 18 age verification redirects to home page on the website.
2. if User is under 18 age verification redirects to decline page.

**Acutal Results**: 
1. If user is over 18 age verification redirects to home page on the website.
2. if User is under 18 age verification redirects to decline page.
**Pass/Fail: Pass**

![](documentation/User-story-ss/main-ss.png)

*Age verification*

![](documentation/User-story-ss/decline-ss.png)

*Decline page*

### Epic: Create an attractive landing page to entice new users and get them to register an account.

#### *User Story*:
*As a user I can see a show case of recipes so I know what style of content is published on the site( must-have / complete)[#10](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/10)

**Testing Steps**:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Scroll down the page to view most popular cocktails on the site.
3. Scroll down to view the most recent cocktails posted.
4. Scroll down to view the 'Join us' and register option.

**Expected Results**:
1. Text visible on the Join us explaining the site.
2. Call to action 'Register' button on bottom of the page.
3. Text indicating that users must register to interact and post cocktails.
4. Three of the most recent cocktails displaying on page.
5. Nav tab 'cocktails' displays all posted cocktails visable to all users.

**Actual Results**:
1. Text visible on the Join us explaining the site.
2. Call to action 'Register' button on bottom of the page.
3. Text indicating that users must register to interact and post cocktails.
4. Three of the most recent cocktails displaying on page.
5. Nav tab 'cocktails' displays all posted cocktails visable to all users.
**Pass/Fail: Pass**

![](documentation/User-story-ss/landing-page.png)
![](documentation/User-story-ss/main-snapshot.png)

### Epic: Enable registered users to CRUD their own reciepes

### *User Story*: 
*As a registered user I can create, read, update and deleted my own recipes so that I can manage my own content. ( Must Have / completed).[#9](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/9)

**Testing Steps**:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Click the 'sign in' link on the navigation bar and sign in with username and password.
3. Navigate to [The Tipsey Tiger](https://the-tipsy-tiger.herokuapp.com/myrecipes/) to view the list of cocktails from the logged in user.
4. Click on View to see the full cocktail recipe details page.
5. Click on edit in the cocktails list to view the original recipe form, edit the field the require updating and click submit to save changes.
6. Click on delete beside the recipe in the list to delete the cocktail recipe.

**Expected Results**
1. Full recipe detail page opens when view option is clicked.
2. The cocktail recipe is updated on the site when edits are submitted.
3. Success messages displays when updates cocktail recipe is submitted.
4. Confirmation message displays when the user clicks delete.
5. Success message displays when user successfully deletes a cocktail.

**Actual Results**
1. Full recipe detail page opens when view option is clicked.
2. The cocktail recipe is updated on the site when edits are submitted.
3. Success messages displays when updates cocktail recipe is submitted.
4. Confirmation message displays when the user clicks delete.
5. Success message displays when user successfully deletes a cocktail.
**Pass/Fail: Pass**

![](documentation/User-story-ss/myrecipe-page.png)

### Epic: Show case the most populate recipes on the main landing page 
### *User story*:
*As a user I can view a list of recipes so that I can see what content is available before I decide to register. ( Must Have / completed)[#12](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/12)

**Testing Steps**:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Click on the 'cocktails' link on the navigation bar to view the recipes posted on the site.
3. Scroll down to view a summary of all recipes currently posted.

**Expected Result**: User is redirected to the recipes page.

**Actual Results**: User is redirected to the recipes page.

**Pass/Fail: Pass**

![](documentation/User-story-ss/recipe-page.png)

### Epic: Enable users to Filter content to find recipes with certain ingrediants.
#### *User Story*
As a User I can filter recipes by ingrediants so that i can find content easily.(Should have / complete)[#13](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/13)

**Testing Steps**:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Log in to site.
3. Click on the 'mycocktails' link in the navigation bar.
4. Click on the dropdown tab labeled skill to filter skill level.
5. Click on the dropdown tab labeled base to filter base alcohol in the cocktail
6. To show all cocktails leave each filter field blank.

**Expected Result**:
List of cocktails corresponding to the filter input by user is displayed or 'Sorry this type of cocktail hasn't been added yet!' if there is no match.

**Actual Result**:
List of cocktails corresponding to the filter input by user is displayed or 'Sorry this type of cocktail hasn't been added yet!' if there is no match.

**Pass/Fail: Pass**

![](documentation/User-story-ss/skill-ss.png)

*Skill filter*

![](documentation/User-story-ss/base-ss.png)

*Base filter*

### Epic: Enable registered users to be able to interact with posts from other users.

#### *User Story*:
*As a registered user I can click on a post to view a full page recipe(Must Have)[#15](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/15)

**Testing Steps**:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Login using username and password.
3. Navigate to 'cocktails' page on the navigation bar.
4. Click on cocktail recipe of choice

**Expected Result**:
User is redirected to the full cocktail recipe details page. User not logged in is redirected to the sign-in page.

**Actual Results**:
User is redirected to the full cocktail recipe details page. User not logged in is redirected to the sign-in page.

**Pass/Fail: Pass**

#### *User Story*:
*As a registered user I can Like or Unlike other users posts so I can interact with the site.( Must Have / complete)[#15](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/15)

**Testing Steps**:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Login into site
3. Click on 'cocktails' link in navigation page
4. Click on cocktail of choice.
5. Click in the glass icon to toggle a cheers/like on the cocktail recipe.

**Expected Result**:
1. When user clicks on the glass a number updates beside the icon
2. Message alerts that a cheers was left on cocktail
3. Message alerts when cheer is removed from cocktail

**Actual Result**:
1. When user clicks on the glass a number updates beside the icon
2. Message alerts that a cheers was left on cocktail
3. Message alerts when cheer is removed from cocktail

**Pass/Fail: Pass**

![](documentation/User-story-ss/cheer-ss.png)

![](documentation/User-story-ss/cheer.png)

![](documentation/User-story-ss/remove-cheer.png)

#### *User Story*
* As a registered user I can comment on other recipes to help with overall UX( Must Have / completed)[#16](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/16)

**Testing Steps**:
1. Navigate to the website of [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)
2. Login in to site
3. Click on the 'cocktail' link on the navigation bar.
4. Click on coktail recipe of choice and navigate to the bottom of the recipe details page.
5. Enter comment in comment box and click 'submit'

**Expected Result**: 
1. A message thanking the user for their thought displays at the top of the page.
2. Comment box disappear and a message 'Your comment is awaiting approval'. Comment appears in admin panel.

**Actual Results**:
1. A message thanking the user for their thought displays at the top of the page.
2. Comment box disappear and a message 'Your comment is pending admin approval'. Comment appears in admin panel.

**Pass/Fail: Pass**

![](documentation/User-story-ss/comments.png)

![](documentation/User-story-ss/comment-post.png)

![](documentation/User-story-ss/comment-approval.png)
