# TheCandyShop

## Table of Contents:
* [Project Brief](#Project-Brief)
* [Entity Relationship Diagram](#ERD)
* [CI Pipeline](#ci-pipeline)
    * [Project Tracking - Jira](#project-tracking)
    * [Version Control - Git](#version-control)
    * [Build Server - Jenkins](#build-server)
* [SQL](#sql)
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
    * [Unit Testing](#Unit-Testing)
    * [Integration Testing](#Integration-Testing)
* [The Application](#The-Application)
    * [Create](#create)
    * [Read](#read)
    * [Update](#update)
    * [Delete](#delete)
* [Known Issues](#known-issues)
* [Improvements for the future](#future-workimprovements)


## Project Brief
The project brief was to design and build a web application from what we've learnt over the past 4 weeks, that consists of the following:
- Project Management
- Python Fundamentals
- Python Testing
- Git
- Basic Linux
- Python Web Development
- Continuous Integration
- Cloud Fundamentals
- Databases

To complete the above, I would need to do:
- Kanban Board: Trello or an equivalent Kanban Board
- Database: GCP SQL Server or other Cloud Hosted managed Database.
- Programming language: Python
- Unit Testing with Python (Pytest)
- Integration Testing with Python (Selenium)
- Front-end: Flask (HTML)
- Version Control: Git
- CI Server: Jenkins
- Cloud server: GCP Compute Engine

The aim was to create a CRUD (Create, Read, Update and Delete) application with the Flask micro-framework. I had to use an SQL database to store data to be able to use the CRUD functionality. This database had to consist of at least two tables that share a relationship. 
The framework for my project can be seen below:
![framework](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/framework.PNG) 


## ERD
The Entity relationship diagram helped me plan out the tables I was to create in my database and outline the relationships between them. This was then helpful when creating the database tables in MySQL Workbench , assigning primary and foreign keys and also knowing what columns each table consisted of.  
The screenshot below shows the ERD I created for my Candy shop application.
![ERD](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/ERD.PNG)

As seen in the ERD, I have created three tables: item, purchase and user. 
The user table will consist of the fields: username, email and address.
The item table will consist of the fields: item_name, price, description and quantity.
The purchase table will consist of the fields: fk_user_id and fk_item_id. 
For each field, I have given it a data type of either int, varchar or dec and written NOT NULL so that the fields can't be left empty.
The user table has a one to many relationship with item and purchase. 
The purchase table has a one to many relationship with item.

## CI Pipeline
The CI Pipeline consists of: project tracking, version control, development environment and build server. Below is the diagram of my complete CI Pipeline. 
![CI Pipeline](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/CI.PNG)

### Project Tracking
To track and manage my project, I used Jira. I had to create user stories of everything that would be needed in my project and put them under Epics. I created four epics: planning, database, coding in Python using Flask and Testing. All the user stories are stored in the product backlog and were moved to each sprint when they needed to be completed.
I created sprints and put individual deadlines so that i can manage my time better and make sure to get the entire project done on time. Once a sprint was complete, I would create a new one with the user stories that need to be completed next. 

The picture below shows the Jira roadmap.
![Jira Roadmap](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Jira%20Roadmap.PNG)

The picture below shows the Jira Board.
![Jira Board](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Jira%20Board.PNG)  

The entire Jira board can be found here: https://michelle548129.atlassian.net/jira/software/projects/CS/boards/3

My burndown chart is shown below:
![Burndownn chart](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Burndown%20chart.PNG)

### Version Control
I used Git for my Version Control. I created a new repositiory on GitHub for this project. The repo can be found here: https://github.com/michelle548129/TheImpossibleQuiz.git
I used Git so that I could continually commit my work there and be able to pull previous versions if needed. This came in handy when the code stopped working due to an error, so the previous code could be pulled from git.
I created a dev branch so that new code could be written and run there first. Once it was working and fully functional, it was pushed onto the main. This prevented me from only using main and having a bunch of errors that prevented my application from running. Anything that was pushed onto main was working at all times. The dev branch was essentially my 'testing' branch where I could figure out how to implement different functions.

The network diagram below shows all the commits made and the main and dev branch. As you can see, I was mainly working on the dev branch and commiting there, then when the code worked, I pushed it onto main. 
![Image showing the network diagram](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Network%20graph.PNG)
 

### Build Server
For my build server, I used Jenkins which allowed my project to be built and tested automatically. First, I created a new firewall rule on Google Cloud Platform. 
![Creating firewall rule](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/firewall.PNG)

![Creating Jenkins instance](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/jenkins%20instance.PNG)
![Creating Jenkins freestyle project](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/jenkins.PNG)


## SQL
I created my database on MySQL Workbench. Below is the SQL code I used to create my three tables that I created on my ERD earlier. It shows the item, user and purchase tables with all the fields shown on the ERD created within them. They are then joined together using Foreign keys. 
![SQL code](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/SQL%20code.PNG)

Here is a screenshot of the item table I created:
![Item table](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/itemtable.PNG)


## Risk Assessment
I created a risk assessment for possible hazards that can occur and how I could overcome them. It's important to analyse these situations and be prepared for them as well as have a plan for them so that when a hazard occurs, it can be easily overcome. It's also helpful to think of ways to prevent these hazards in advance to minimise the risk of them occuring. 
As you can see, when the control and response measures are put into place, the likelihood of these hazards occuring or the affect they'll have will drastically descrease. 
![Image showing the Risk Assessment Table](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Risk%20Assessment.PNG)


## Testing
![test.sh](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/testsh.PNG)

### Unit Testing


### Integration Testing


## The Application
The main objective in this project was to create an application that fulfils the CRUD functionality. Below I will discuss how I've implemented the CRUD functions to my project.
 
### Create:
#### CREATE used for user:
I have implemented 2 CREATE functions in my application. 
The first is to register a user. In the application, the user is able to register with their details through a form and the data is automatically stored in the 'user' table in the SQL database. 
![Register form](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/createwebpage.PNG)
![User Input for registering](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/addusercreate.PNG)
![User Table](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/usertable.PNG)
As you can see, when the user enters their details to register, the 'user' table in the MySQL database adds the data there.

#### CREATE used for item:
The same function is done for the 'item' table.
![Add item form](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/additemform.PNG)
![Adding in new item](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/newitemadded.PNG)
![New item in list](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/itemlistupdated.PNG)
As you can see, here, the admin of the shop is able to add new items to the shop. When the item has been added, it is added to the 'item' table and list of items on the website is also updated, containing the newly put item.


### Read:
I have included the READ function so that the list of items is displayed on the shop. This enables users to see what candy bars the shop has to be bought. The list is read from the 'item' table created on the MySQL database, hence any data in that table will be displayed on the website.

![List of items](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/itemlistupdated.PNG)

I have also created a drop down function so that the data in both the user adn item tables are displayed. If the user wants to make an order, they need to select the name of the customer and the product they would like to buy.

![Drop down function](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/dropdown.PNG)


### Update:
For the UPDATE functionality, I have implemented it so that the user is able to update the quantity of the candy available. This lets them change the stock if needed. This change also update the data in the item table.

![Update quatity form](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/updateform.PNG)
![Quantity updated](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/updating.PNG)


### Delete:
I have implemented the DELETE function by allowing the user to delete an item if they need to. This can be if the candy is no longer is stock or if it'll no longer be sold. Like with all the other CRUD functions, deleting an item form the website will also delete the item form the MySQL database. 

![Deleting Review](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/updateform.PNG)
![Deleting Review](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/deleted.PNG)



## Known Issues


## Future Work/Improvements
