# The Tipsy Tiger Cocktail Guide

![Mockup](documentation/User-story-ss/Mock-up.png)

### *Live link to [The Tipsy Tiger Cocktail Guide](https://the-tipsy-tiger.herokuapp.com/)*

# Table of contents:
- ##  [Context](#context)

- ##  [UX](#UX)
     - [Agile](#Agile)
     - [Project Goal](#Project-goal)
     - [Target Audience](#Target-audience)
     - [Epics and user stories](#Epics-user-stories)
     - [Flowchart](#Flowchart)
     - [Scope](#Scope)
     - [Wireframes](#Wireframes)


- ##  [Features](#Features)
     - [Structure](#Structure)
     - [Existing Features](#Existing-features)
     - [Age verfication](#Age-verfication)
     - [All pages](#All-pages)
     - [Home page](#Home-page)
     - [About page](#About-page)
     - [Cocktail Recipe Page](#Cocktails-recipe-page)
     - [My Cocktails Page](#My-cocktails-page)
     - [Recipe detail page](#Recipe-detail-page)
     - [Sign-In form](#Sign-In-Form)
     - [Register form](#Register-form)


## Context 
The Tipsy Tiger Cocktail Guide is a recipe style website, that displays cocktail recipes created and posted by users on the site. 

The website is simple:
- Non registered users can view the site and can register for an account in an easy process.
- Logged in users have a range of options available.
- User can view full page cocktail recipe details.
- User can create their own cocktail recipe.
- User can edit their own cocktail recipes
- User can delete their own cocktail recipes
- User can interact with other posts on the site in the form of comments or liking the cocktail

## UX

### Agile
The Agile methodology was used to plan and create the project. Google sheets and Github were the tools used to demonstrate this.
1. Projects were used to divide the project into three iterations with a simple kanban board.
2. Milestones were used to create User Stories with a custom template.
3. Issues were used to create each individual User Story. Each story defines the title, statement, and acceptance criteria.

* Each user story was grouped into an Epic and placed within one of the three iterations.The User Stories were classified as 'must-have', 'could-have', & 'should-have' in order to priortise the work. As progress was made on each user story it was moved from 'to do' across to 'In Progress' column. When each user story wass complete it was moved across to 'done' column.

* However it was difficult in Github since the projects application changed, to adequately link iterations - Epic - User Stories. To help keep further track and make it easier to follow the Agile methodology I used Google Sheets to create a [project kanban board](https://docs.google.com/spreadsheets/d/1T_LNmWw8ennfcJeJCG63nfQmfHPUSE6cgO4ReGNBRmg/edit?usp=sharing) to track progress in the event Github Projects didn't fulfill the Agile requirements the project had. Although I linked User Stories (Issues) to Epics (Milestones) and placed these in Iterations (Milestones), Epics did not automatically show the % progress to completion once user stories were moved in the kanban board on Github projects.

### Project Goal
* The goal of this project was to create a cocktail recipe site with tried and tested cocktails for get together's. As the world was separate for a while due to covid, socializing habits changed and more people stayed at home and entertained when it was safe to do so. While there is still a need for pubs and clubs, more and more home parties are being organized. From bbq's to baby showers and milestone birthday parties. With this in mind, The Tipsy Tiger Cocktails Guide was created. To help people add something special to the celebrations.

### Target audience

The target User is someone:
* Who wants to add a homemade cocktail to impress their guests.
* Who wants to be able to modifify and control alcohol limit in each drink.
* Who wants to add the personal touch to celebrations.
* Who wants to engage with others who have the same interest in cocktails.
* Who wants to share their own creations and recipes.

### Epics and User Stories 
In order to efficently build the site, 10 Epics and 19 user stories were created to cover all the bases of the final site. 
1. Epic: Set up an admin page to manage posts, reviews, comments and user with comments.

* User Stories: 
    * As an admin I can post content so that there is a decent library of recipes.[#1](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/1)

    * As an admin I can approve content so that the it's only relevant content posted[#2](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/2)

    * As an admin I can approve reviews so that I can filter inappropriate content[#3](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/3)


2. Epic: Enable users to set up an account on the website to access the full features.

* User Stories: 
    * As a user I can register an account so that I can access the full range of features on the site[#4](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/4)

    * As a user I can login and logout of the site so that I can access my content and interact with other users content.[#5](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/5)

    * As an admin I can set an age verification so that underage users can't access alcohol based topics.[#6](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/6)


3. Epic: Create an attractive landing page to entice new users and get them to register an account.

* User Stories:
    * As a user I can see a show case of recipes so I know what style of content is published on the site[#7](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/7)

    * As a user I can access the recipes from a new tab so I don't loose my position on the site.[#8](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/8) 

    
4. Epic: Enable registered users to CRUD their own reciepes.

* User Stories:

    * As a registered user I can create, read, update and deleted my own recipes so that I can manage my own content.[#9](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/9)
    

5. Epic: Show case the most populate recipes on the main landing page

* User Stories:

    * As a user I can view a list of recipes so that I can see what content is available before I decide to register.[#10](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/10)

    * As a user I can view a paginated list of recipes so I can move through the content easily.[#11](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/11)

    * As an unregistered user I still access content so that I can decide to register at a later time[#12](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/12)


6. Epic: Enable users to Filter content to find reciepes with certain ingrediants.

* User Stories:

    * As a User I can Search recipes by ingredients so that i can find content easily.[#13](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/13)

    * As a User I can filter recipes by skill and base so I can easily find cocktails[#14](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/14)


7. Epic: Enable registered users to be able to interact with posts from other users.

* User Stories:

    * As a registered user I can Like or Unlike other users posts so I can interact with the site.[#15](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/15)

    * As a registered user I can comment on other recipes to help with overall UX[#16](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/16)


8. Epic: Enable users to CRUD own reviews and comments.

* User Stories:

    * As a registered user I can create/read/update/delete my own review posts so that I can manage my own content[#17](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/17)


9. Epic: Enable user to sign-in/ register with Google/facebook account.


* User Stories:

    * As a user I can register an account with social networks so that I can verify my account easily[#18](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/18)


10. Epic: Enable user to upload pictures with recipes that are added.

* User Stories:
 
    * As a user I can upload a picture to enhance the content that I post to the site.[#19](https://github.com/Charte-dot/The-Tipsy-Tiger-cg/issues/19)


### Flowchart
 * I designed a basic flowchart on [Lucid Chart](https://lucid.app/lucidchart/8619b2ff-1840-4d3a-b234-ac143540d744/edit?page=0_0&invitationId=inv_9469ea28-80f3-48d1-943c-643df72710da#) first.This was to give me a template to follow and to make sure my original design that I had planned was the outcome and final layout of the application. This was an essential piece to the project along side the epics and user stories as it helped me keep track of how the application would be displayed to the user and the steps the user would take within the application.

- How would the flow of the website be laid out?
- How would I deal unregistered users?
- What benefits where there for registered and logged in users? 
 
 ![](documentation/User-story-ss/flowchart.png)

### WireFrames
I designed a basic wireframe to compliment the Epics, User stories and flow chart.This was to give me a template to follow and to make sure my original design that I had planned was the outcome and final layout of the application. Some feature have been change due to time constraints.

* Age verification
![](documentation/wireframes/Wireframe1.png)

* Home page
![](documentation/wireframes/Wireframe2.png)

* About page
![](documentation/wireframes/Wireframe3.png)

* Cocktail recipe page
![](documentation/wireframes/Wireframe4.png)

* My cocktail Page
![](documentation/wireframes/Wireframe5.png)

* Cocktail recipe form
![](documentation/wireframes/Wireframe6.png)

* Registration form
![](documentation/wireframes/wireframe7.png)

* Sign in form
![](documentation/wireframes/Wireframe8.png)


### Scope

The scope of the project was quiet extensive at the beginning. The over all goal was to give users full CRUD on all of their content. Due to time constraints this meant user's only had CRUD functionality on cocktail recipes and as this was deemed a must have and took priorty. More functionality for logged in users will be added in the future. Further front-end admin functions will be added as this project is limited to back-end django admin panel. 

## Features
### Structure 
The website consists of six pages:
* Home
* About
* Cocktails
* My Cockatails
* Register
* Sign-in/Sign-Out
Home, about and cocktail pages and be viewed by all users. My cocktails is limited to registered and logged in users.

### Existing Features
### Age verification
* As the recipe site is based on alcohol themes, an age verification asks the user if they are over 18 

![](documentation/User-story-ss/main-ss.png)
*Main page age verfication*

* If the user is not over 18 and clicks the 'not over 18 link a decline page is activated.

![](documentation/User-story-ss/decline.png)
*Age verfication decline*

#### All pages
    
*Navigation bar*:
  * Brand logo linking back to the home page.

![](documentation/User-story-ss/logo-nav.png)
   *Logo*

* Links to the Home, About, Cocktails, My Cocktails, Register and Sign-in/Sign-out Pages: Home, about and cocktail pages and be viewed by all users. My cocktails is limited to registered and logged in users.
If the user is not signed in the Sign in and Register links are visible in the navbar. If the user is signed in the Sign In and Register links are replaced by a Sign Out link and the My Cocktails page link is visible:

![](documentation/User-story-ss/nav-bug2.png)
   *Navigation for unregistered users*

![](documentation/User-story-ss/Register-nav.png)*Navigation for logged in users*

* The Navigation bar sticks to the top of the page and remains in view while the user is scroling for easy access around the site.

![](documentation/User-story-ss/sticky-nav.png)
   *Sticky Nav*

   
* The navigation bar collapses for smaller screen sizes
   
![](documentation/User-story-ss/ss-menu.png)
   *Smaller nav bar*

   
   - Footer: Clear visiable links to social media sites, Facebook, Twitter and Instagram

![](documentation/User-story-ss/Footer.png)
   *Footer*

### Home page
* Hero Image with overlay test of the site name.

![](documentation/User-story-ss/Hero-img.png)
*Hero image*

* Text directing user to the cocktail recipe page.

![](documentation/User-story-ss/cocktail-link.png)
*Cocktail recipe page link*

* Snapshot of three most recent cocktails posted with title, date added and Author. This page updates automatically ever time a new cocktail is added.

![](documentation/User-story-ss/main-snapshot.png)
* Home Page Cocktail Snapshot*

* Call to action button 'Register' at the bottom of the page to direct users that want to register to the registration form.

![](documentation/User-story-ss/register-link.png)
*Registeration link*

### About Page
* Image with text information about the website, with links to recipe page, register page and login page.

![](documentation/User-story-ss/about-ss.png)
*About page with link*

### Cocktail recipe page
* Images with description of skill level and alcohol base type visible to all users. Cocktail title is a link to full recipe details if the user is logged in, if not this redirects to the Sign-In Page. Glasses representing a like and comment icons have total number interactions beside them.

![](documentation/User-story-ss/ss-recipes-page.png)
*Cocktail page*

* A filter for the skill level and alcohol base above the cocktail page enables users to filter the cocktails to a skill level of choice and a choice of alcohol based cocktail. Clickable icon to submit the filter choices.

![](documentation/User-story-ss/skill-ss.png)
*Skill Filter*

![](documentation/User-story-ss/base-ss.png)
*Base Filter*

* The cocktail title links to the full recipe details which can only be accessed by registered or logged in users. User who are not logged in are redirected to the sign-in page.

![](documentation/User-story-ss/title.png)
*Cocktail Title*

* A call to action 'Add a cocktail' button will directed logged in users to my recipes page and non logged in users to the sign in page. This allows intuitive navigation on the site.

![](documentation/User-story-ss/add-recipe-page.png)

### My Cocktail page
* This page can only be accessed by logged in users. The navigation link only appears when the user is logged in.

* The list of cocktails added by the user are organised in a table, with the most recently created at the top of the list. This table displays the title, view cocktail, edit cocktails and delete cocktail. 

![](documentation/User-story-ss/myrecipe-page.png)
*cocktails table*

* View Cocktail opens the full recipe page for that cocktail.
* Edit cocktail opens the edit form to allow the user to make amendments to the recipe.

![](documentation/User-story-ss/edit-cocktail.png)
*Edit form*

* A pop up message alerts the user that the cocktail has successfully edited.

![](documentation/User-story-ss/edit-txt.png)
*Edit message*

* Delete cocktail enables a user to delete the cocktail. This removes the cocktails from the users own cocktail list and from view on the home page and cocktail page. 

![](documentation/User-story-ss/delete-cocktail.png)
*Delete cocktail confirmation*

![](documentation/User-story-ss/cocktail-delete-txt.png)
*Successful delete message*


### Recipe Detail Page
 Accessed only by logged in users by clicking on the View tab in the 'my cocktails' table or by the title link on the 'cocktails' page.

![](documentation/User-story-ss/recipe-details-ss.png)
*Recipe details page*

* The clinking glass Icon can be clicked to give a 'Cheers' and remove the 'Cheers from a recipe. The cheers feature is a play on a like feature.

* The number of 'Cheers' given to a cocktail recipe is displayed beside the icon in recipe details page and beside the icon in the cocktails page.

* Message to confirm each action is displayed.

![](documentation/User-story-ss/cheers-ss.png)
*Cheers confirmation message*

![](documentation/User-story-ss/remove-cheers.png)
*Removal of cheers message*

* The about section of the recipe includes, number of comments, serve amount per recipe, skill level, alcohol base and an 'Updated on field'.

![](documentation/User-story-ss/About-recipe.png)
*About page on recipe details*

* If the user has created a recipe and the recipe is currently posted the author of the recipe will have two extra features on their on created recipe. An edit option and a delete option appear on the bottom of the recipe. This is only viewable to the Author of that recipe.
This is to promote intuitive navigation. 

![](documentation/User-story-ss/Author.png)
*Extra feature for the author of the recipe*


![](documentation/User-story-ss/non-author.png)
*View for non author of the recipe*

* Comments:
At the bottom of the recipe ingrediants and steps is the Comment section to display comments in descending order by date.

![](documentation/User-story-ss/comments2.png)
*Comments*

* Below the published comments is a from to submit a comment.
* After submission of comment an 'pending approval' message is shown until admin approve the comment.

![](documentation/User-story-ss/comments.png)
*Comment form*

![](documentation/User-story-ss/comment-approval.png)
*Awaiting admin approval*

![](documentation/User-story-ss/comment-post.png)
*Thanks for your thoughts message*

### Sign-In Form

* User Signs in by entering Username and password created when registering.

* An Action button for sign-in which redirects back to the home page once user is signed in. 

![](documentation/User-story-ss/sign-in.png)
*Sign-in form*

![](documentation/User-story-ss/sign-in-pop.png)
*Sign-In pop up message*


### Register Form

* Users can register for an account by entering a username, an optional email and a password.

* A choice of  call to action buttons. Sign-up completes the registration and redirects user back to the home page. Home button redirects user to home page but no account has been registered. 

![](documentation/User-story-ss/register-form.png)
*Registeration form*

![](documentation/User-story-ss/sign-in-pop.png)
*Registeration success message*