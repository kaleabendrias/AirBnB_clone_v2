# Web Framework with Flask

This repository contains a web application built with Flask, a micro web framework in Python. This README provides an overview of the project, its structure, and how to use it.

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [How to Run the Application](#how-to-run-the-application)
4. [Routes and Templates](#routes-and-templates)
5. [Database Integration](#database-integration)

---

## Introduction

### What is a Web Framework?

A web framework is a pre-built, standardized set of tools, libraries, and best practices for developing web applications. It simplifies web development by providing a structure and common functionality, allowing developers to focus on application-specific features.

### How to Build a Web Framework with Flask

This project demonstrates how to build a web framework using Flask, a popular Python micro web framework. Flask provides a simple and flexible way to create web applications, making it a great choice for both small and large projects.

### What is a Route?

A route in a web application defines how the application responds to specific URL patterns. In Flask, routes are defined using Python decorators. Each route corresponds to a specific URL, and when that URL is requested, the associated function is executed.

### Handling Variables in a Route

Routes can include variables that are part of the URL. For example, in a route like `/states/<id>`, `<id>` is a variable, and it can be accessed within the route function.

### What is a Template?

A template is an HTML file with placeholders that can be filled with dynamic data. In Flask, templates are typically written using Jinja2, a templating engine. Templates allow you to generate dynamic HTML content and display data from your application.

### Creating HTML Responses with Templates

Flask uses templates to generate HTML responses. You can create HTML pages that include dynamic data, loops, conditions, and more, all within your templates. This allows for the creation of interactive and data-driven web pages.

### Displaying Data from a MySQL Database

Flask can be integrated with various databases, including MySQL. This project demonstrates how to display data from a MySQL database in your web application. You can use SQLAlchemy, an Object-Relational Mapping (ORM) library, to interact with the database.

---

## Project Structure

The project is structured as follows:

- `app.py`: The main Flask application with route definitions.
- `templates/`: This folder contains HTML templates, including `9-states.html`, which is used to display data.
- `models/`: This folder contains the database models and configuration. In this project, SQLAlchemy is used to interact with the database.

---

## How to Run the Application

1. **Install Flask**

   Make sure you have Flask installed. If not, you can install it using `pip3`:

   ```bash
   $ pip3 install Flask
   ```

2. **Run the Application**

   To run the Flask application, execute the following command:

   ```bash
   $ python3 app.py
   ```

   The application will start and listen on `http://0.0.0.0:5000`.

---

## Routes and Templates

The Flask application defines the following routes:

- `/states`: Displays an HTML page with a list of states.
- `/states/<id>`: Displays an HTML page with a list of cities for a specific state.

The templates, located in the `templates/` folder, define the structure of the HTML pages. The `9-states.html` template is used to display the data. It includes conditional statements and loops to create dynamic content based on the data from the database.

---

## Database Integration

This project demonstrates the integration of Flask with a MySQL database. It uses SQLAlchemy to interact with the database. The database models are defined in the `models/` folder, including the `State` and `City` models.

To display data from the database, the Flask routes retrieve the necessary data from the database using SQLAlchemy and pass it to the templates. The templates use this data to generate dynamic HTML pages.

---

This README provides an overview of the web application built with Flask, including its structure, routes, templates, and database integration. You can use this project as a starting point for building your own web applications with Flask. Enjoy coding!