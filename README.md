# TheCandyShop

## Table of Contents:
* [Project Brief](#Project-Brief)
* [Entity Relationship Diagram](#ERD)
* [CI Pipeline](#ci-pipeline)
    * [Project Tracking - Jira](#project-tracking)
    * [Version Control - Git](#version-control)
    * [Development Environment](#development-environment)
    * [Build Server - Jenkins](#build-server)
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
    * [Unit Testing](#Unit-Testing)
    * [Integration Testing](#Integration-Testing)
* [The Application](#The-Application)
    * [Create](#create)
    * [Read](#read)
    * [Update](#update)
    * [Delete](#delete)
    * [Database](#database)
    * [Versions](#versions)
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
The CI Pipeline consists of: project tracking, version control, development environment and build server. 
![CI Pipeline](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/CI.PNG)

### Project Tracking
For project tracking, I used Trello in order to build a project tracking board. Each of the different tasks was added to the project backlog and during the course of the sprint, each item was moved from the backlog to in progress, to completed and finally to pushed to main once the task had been pushed to main on the Github repository. The board at the start of the project can be seen below:
![Jira Roadmap](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Jira%20Roadmap.PNG)
The following link will take you to the 
![Jira Board](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Jira%20Board.PNG) to view the full board. 
