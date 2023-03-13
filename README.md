# shovl. : Finding High Quality Virtual Reality Products
As software engineers, it's our job to use our computer science skills to solve problems. We built shovl to address the problem of finding reputable vendors that can produce high quality virtual reality products.

## The Problem with Current Vendor Sites
Many vendor sites, such as Goodfirms, Clutch.co, and The Manifest, have sponsored results and inconsistent data. This makes it difficult to get all the relevant information in one place.

## shovl Overview
Shovl is a full stack web application built in Python. It provides a clean, user-friendly interface to search for B2B vendors in a dozen sectors of technology, such as AR/VR, Artificial Intelligence, Blockchain, and Cybersecurity. Shovl aims to bring users an unbiased and honest ranking of vendors, allowing them to make informed decisions. Users can also save their favorite vendors to their profile for later.

## Program Overview
Shovl has two main components: a web scraper and a PostgreSQL database. The web scraper stores the raw vendor data in a CSV file and runs it through our special ranking algorithm. This ranked data is stored in the database, along with encrypted user data that keeps track of login authentication and a vendor watchlist. The front end is done in Django, a full-stack Python-based framework that renders templates in HTML and CSS.

## Getting Started
To get started with shovl, you'll need Python 3 and PostgreSQL installed.
