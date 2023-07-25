# Teacher Guide: Flask Routing

## SWBATs
- Know what a **server** is.
- Get introduced to **Flask** and have understanding of how they are going to use it.
- Learn how to use flask.
- Understand the relation of **Flask** to **MVC**. 
- Run their first (local) **web server** using **Flask** and `Python`.
- Create their first web application routes! 


## Motivation
- Pretty much every single app you’ve ever used is just some combination of this pattern/mechanism (MVC)
- You’re about to learn start learning how to implement **MVC**, starting with **Flask** - The controller, and using the **templates** (HTML pages) as views.

## Lesson Plan
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) **Slide 3:** Let's discuss the previous session's microFeedback results, discuss any notes that are worth talking about according to the survey results. and make sure to address those who are in panic zone.
- **Slide 4:** Quick review, of previous session, and anything else worth reviewing according to the microFeedback survey.  

- **Slide 7: What is a Server?**
    - Simply, A web server is a computer that runs websites. The basic objective of the web server is to store, process and deliver web pages to the users.
    - Refer back to the restaurant example from mvc.

- **Slide 8: What is Flask?**
    - Flask is a web framework. This means flask provides you with tools, libraries and technologies that allow you to build a web application.
    - Just like we `import turtle` to use it's pre-built functions, we `import flask` to do the same!

- **Slide 11: Why Use Flask?**
    
- **Slide 12:**
    - Say: "These are the basic essential lines to have our flask app running!"

- **Slide 20:**
    - Let's explain our code using the MVC map!
    - Feel free to either use the MVC map slide, or copy it to the board and showing the code on the slides.
    
- **Slide 21:**
    - Explain: This is how the folder structure should be in their development environment (project folder).
    - Main Project Folder (should include):
        - `main.py` / `app.py` (The controller flask app)
        - any other `.py` files
        - `templates` (folder named templates):
            - It should contain all `.HTML` files.
        - `static` (folder named static):
            - It should contain all `.js` and `.css` files, and any other "static" file (such as images)
            - Students should create these folders and name them in small case letters.

- **Slides 23-28: What is/How to use Routing?**
    - Pretty straight forward.
    - Fall back on MVC concept to make it easier to students to understand.

- **Slide 29: Lab time!**
    - Send students to lab time.
- At the end of session, draw students' attention back to the lecture, discuss our **Takeaways**, and leave them with a **cliffhanger** in the "Next session" slide!
    
- Don't forget to collect everyone's microFeedback before letting students out of class!




## Conclusions/Takeaways
- Our Flask app is effectively the controller (MVC)!
- Using Flask framework, we can create routes and point them to our desired HTML templates! (Or views)
- Flask is a useful tool for building web applications quickly and robustly.

## Hints & Hurdles
- Students might be confused of all the setup lines for `app.py`... Make sure they know **it's ok**, they don't have to *fully* understand them, just understand that these are the "configuration" lines for **Flask**. (As in, Flask needs these lines in order to run)
- Show students a demo at some point of the difference between `debug = True` and `debug = False`. Explain how keeping it `True` while building something is useful.
- This topic might feel abstract. In some ways, while learning a new language, with time you'll have more intuition... It's just like that in computer science.
    - Reference back to how each and every one of the students learned **at least 1** language other than their mother tongue's. The process of learning a new language in computer science is the same.
