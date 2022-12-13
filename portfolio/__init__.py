from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

print(2)

aboutme_dict = {
    "My Skills": {
        "Backend Development - Django": "Build TDD oriented Django Static Websites using Django Model View Template Architecture using both SQL Databases and NoSQL Databases (mongoDB).",
        "Backend Development/API - Flask": "Build websites and APIs with Flask micro-framework using MySQL or MongoDB.",
        "Backend Development - Golang (Gin)": "Build websites using Gin as the backend framework using SQL relational database.",
        "Microservices - Golang": "Build microservices with Go.",
        },
    "Experiences": {
        "Portfolio Website": "Built a portfolio website using Flask as a backend micro-framework. Deployed with AWS EC2.",
        "Python Novice Blog": "Built a Python django blog using PostgreSQL relational database for users, user likes, user profile and user posts as well post comments and user comments, deployed with Heroku.",
        "Study Guide Web App": "Built a study guide web app using Flask and MongoDB. It allows to store information into a NoSQL database which can later be tapped into to create a test and study concepts.",
        "Weekly Planner Web App": "Built a weekly planner that stores tasks to do for a particular date selected. It calculates amount of hours available in a particular date, you cannot overload day with tasks amounting over 8 hours. Weekly Planner allows to check completed items."},
    "Certifications": {
        "Django 4 and Python Full-Stack Developer Masterclass": "Basic HTML, Basic CSS. Django Function Based Views, Class Based Views, Model Based Views. Django Models to interact with SQL backend databases. Django Forms and Django built-in Authentication.",
        "100 Days of Code: The Complete Python Pro Bootcamp for 2023": "Learn Python Syntax, variables, built-in data structures, Python Libraries, Build Pythong GUIs with TKinter, Build backend web apps with flask."
    }
}


    # {
    #     "name": "Portfolio Website",
    #     "thumb": "img/",
    #     "hero": "img/",
    #     "categories": [languages],
    #     "slug": "portfolio-website",
    #     "prod": "link to project"
    # }

projects_list = [
    {
        "name": "Python Novice Blog",
        "thumb": "images/pynoviceblog.png",
        "hero": "",
        "categories": ["Python", "Django", "PostgreSQL", "Heroku"],
        "slug": "django-blog-website",
        "prod": "https://www.pythonnoviceblog.com/"
    },
        {
        "name": "Portfolio - Carlos García",
        "thumb": "images/portfolio.png",
        "hero": "",
        "categories": ["Python", "Flask", "MongoDB", "AWS"],
        "slug": "portfolio-website",
        "prod": "#"
    }
]

recognition_list = [
    {
        "type": "Customer Recognition",
        "text": "Recognition made by customer to team lead, for having a customer happiness oriented service.",
        "img": "images/recognitions1.png"
    },
    {
        "type": "Peer Recognition",
        "text": "Recognition made by peers for being goal oriented and fixing issues from the root cause.",
        "img": "images/recognitions2.png"
    },
    {
        "type": "Leadership Recognition",
        "text": "Recognition made by manager to the whole the company due to innovative thinking and performance.",
        "img": "images/recognitions3.png"
    }
]



@app.route("/")
def home():
    active_tab = request.args.get("tab")
    if not active_tab:
        active_tab = [item for item in aboutme_dict.keys()][0]
    else:
        if active_tab not in aboutme_dict:
            active_tab = [item for item in aboutme_dict.keys()][0]


    selected_tab_dict = aboutme_dict[active_tab]

    return render_template(
        "home.html",
        skills_experiences=aboutme_dict, 
        active_tab=active_tab, 
        selected_tab_dict=selected_tab_dict,
        projects_list=projects_list,
        recognition_list=recognition_list
    )




if __name__ == "__main__":
    app.run(debug=True)
