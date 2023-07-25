# Teacher Guide: Flask Forms

## SWBATs
- Get introduced to **Flask forms** and understand what will we be using it for.
- Have understanding of the **MVC Concept**'s big picture! With Flask forms, we will be able to cover the last gap from building an MVC web application.
- Understand the difference between a `GET` & `POST` requests. 
    - And be able to handle each request in our **Flask app**!
- Link HTML forms to Flask (Python), and import the **data *collected*** from the form in our HTML **view**.
    - This will allow us take information from our web application users!
    - And even save it in our database!!


## Motivation
- We already learned how to run our website on a server using `Flask`, but how do we ***take input*** from our user? This is where `Flask Forms` come in!
- `Flask Forms` will allow us to ***take input*** from our users, and save this data to our database for later use!
- With `GET` & `POST` requests, we will be able to have more control over our **web application**, and actually be able to tell our **web app** when are we asking to only ***see*** (`GET` request) the **views**, and when we want to ***send*** (`POST` request) data to the **app**.


## Lesson Plan
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) **Slide 3:** Let's discuss the previous session's microFeedback results, discuss any notes that are worth talking about according to the survey results. and make sure to address those who are in panic zone.
- **Slide 4:** Quick review, of previous session, and anything else worth reviewing according to the microFeedback survey.
    - Say "Ok, Quick review **over**!", to draw students' attention to the lecture and inform them that we are starting today's lecture.

- **Slides 5-9: Dynamic Routing!**
    - Slide 6: Let's take a look at the code... any guesses of what it does?
    - Slide 7: It's supposed to display `Hello [Name]` on the **view**, when we go to the route `/hello/[Name]`. How?
    - Slide 8: Here's how! We include all of these yellow highlighted texts... It works basically by:
        - Linking the `variable` in the `route` (For example: `/hello/<datatype: variable_name>`).
        - Include the `variable` name (`variable_name`) in the function's input arguments (For exmaple: `def function_name(variable_name)`)
        - Pass the `variable` name (`variable_name`) in `render_template()` function.
        - Finally, display it in the **view** using Flask/Jinjai syntax `{{ }}`.
    - Slide 9: Pay attention to setting up the variable's `datatype` in `<datatype: variable_name>`. (For example: `<string: name>`)
    
- **Slides 10-14: GET & POST (Explanation and Examples)**
    - Slide 10 In **website applications**, we have something called `HTTP Methods`, and they are:
        - `GET`:
            - Used for retrieving data.
            - Parameters are sent in the URL.
            - Can only send text data.
            - All data is clearly visible – not good for passwords.
        - `POST`:
            - Used for sending data.
            - Parameters are sent in the request body.
            - Can send any kind of data to the **controller**.
            - Usually used for passwords.
    - Slide 11: In simpler words, 
        - `GET` - is when you put in a link/route in the *url bar*, and **GET/Recieve/View** an HTML page (a view) in return!
        - `POST` - is when you are already on that **view**/HTML page you just got, and you give the page new information! 
            - Such as login info.
            - Or filling a form.
    - Slide 12: Here's a `GET` example! When you go to [Instagram.com](https://instagram,com), the first thing that’s happening to you is getting an instagram html page/view!
        - For example when you log into **IG**, you get the `homepage` to be **displayed**!
    - Slide 13: BUT, when you go to editing your profile, you would have a form for the user to **fill**, and when you **click on submit**, you are doing a `POST` request, to save your new data! Makes sense now?
    - Slide 14: **Remember,** `GET` is the **default method** in the browser.

- ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Slide 22: Interactive Practice (Turn & Talk)**
    - Thinking about how Facebook website works, turn to your patner.
    - Come up with 3 GET request examples.
    - Come up with 3 POST request examples
    - You have 90 seconds.
    - Ready? Go!
    - *After 90 seconds, discuss student answers and write them on the board.*

- **Slide 16:**
    - The `methods` parameter specifies which `HTTP methods` this route is **allowed to use**.
    - `request` is an object that **holds information** about the **current** `HTTP request`.
    - `request.method` is the method of the **current** `HTTP request`.
    - If you run this piece of code, you’d have a `GET` request by default because you’re not requesting a `POST` request/sending any data.
   - You will make a `POST` request in the case of **submitting** a ***form*** filled with **information**.
   
- **Slide 17: What is a Form?**
    - The **form** is the basic element that lets users interact with our **web application**.
    - Flask alone doesn't do anything to help us handle forms, but the **Flask-WTF** extension let's us use the popular `WTForms` **package** in our **Flask applications**. 
        - This package makes defining **forms** and **handling submissions** easy.

- **Slides 19-21: Creating a form in HTML**
    - Slide 19: Here's an HTML form, submitting this form should make a `POST` request; this is why we specify in the `<form>` tag the parameter `method = "POST"`.
    - Slide 20: `action = "/create"` is where the form should be submitted to. (We can specify a `route`, or a `{{url_for('function_name')}}`
        - Pay attention to the `name` parameter in `<input>` tags, we will use it to access each input tag and take our data!
    - Slide 28: Here's how the form would look like in HTML!


- ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) **Slide 22: Interactive Practice (Mini Lab)**
    - You’re an engineer at a Startup, and you’re building a feedback form (because feedback is really important!)
    - Open up your laptops, create a new Rep.it/file 
    - Try to code this form in HTML.
    - You have 3 minutes.
    - Customize the text content as you wish 
    - Ready? Go!
    - *Show your partner after 3 minutes*
    
- **Slide 23: Configurations lines in Flask**
    - The `secret key` helps protecting web **forms** against a nasty attack called "Cross-Site Request Forgery" (a type of malicious exploit of a website where unauthorized commands are transmitted from a user that the web application trusts).
    - It will basically help us protect our **web application data** from being stolen by hackers!
    
- **Slides 24-27: Handling Form Submissions in Flask!**
    - Slide 24: Let's handle the **animals form** (We previously created) in our **Flask Routes and Functions!**
        - As you can see, this route can take `GET` or `POST` requests.
        - And here's our `GET` request handling: if it is a GET request, return the template `form.html` to the user to see! (The **view**)
    - Slide 25: If it is a `POST` request, we basically need to save the new information, and then return the template `response.html`!
    - Slide 26: When we say `request.form['firstname']`, this means we are taking the data that the user put in the 'firstname' field of the form. 
        - Same works for `['animal']`, and any other `<input>` we might add!
        - We are saving the **form** data to variables. (In our case, they're called `name` and `animal`)
    - Slide 27: `save_to_database` is a function inside `databases.py` that interacts with the database. 
        - In this case, it saves the info `name` and `animal` to our `.db` file.
        - Emphasize that `save_to_database` is just an example of what could be done, students shouldn't get confused of this. If they do, assure them it's ok, they don't have to fully understand what does this function do... just how we take data from forms!
    - Slide 28: Lastly, We are showing a different view to the user after submission, an HTML page called `response.html`. 
        - We are also sending the data we got as variables to our view!
        - Our view should show the user a message letting them know they successfully submitted the form!
        - Again, this is just an example, not all web applications have to do this.
        
- **Slide 28: Let's go over the MVC Map one last time!**
    - Go over the MVC map, with reference to each file/block of code to help students pieces of understanding fall all together.
    - It's important to emphasize that with the topics we have learned so far, we are able to create a fully implemented **MVC** framework to our **website applications!**
    - Feel free to draw the MVC map on the board, and navigate through your code on the projector. 


- **Slide 29: Lab time!**
    - Send students to lab time.
- At the end of session, draw students' attention back to the lecture, discuss our **Takeaways**, and leave them with a **cliffhanger** in the "Next session" slide!
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) Don't forget to collect everyone's microFeedback before letting students out of class!



## Conclusions/Takeaways
- When errors show up at our front door, simply read them to find the reason they’re here!
- By using Flask forms, we are able to get information/***input*** from a user!!!
- We have 2 browser methods: `GET` & `POST`!


## Hints & Hurdles
- `GET` & `POST` are often very confusing to students, don't spend too much time on Slide 16... Slide 17 explains it better.
- Always refernce back to MVC in order to help students understand the ***bigger picture***!

