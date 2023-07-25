# Teacher Guide: Advanced Flask

## SWBATs
- Pass variables and data from `app.py` to HTML files.
- Display data in HTML files using Flask (Jinjai) syntax.
- Iterate through data using Flask (Jinjai) syntax in HTML files.
- Create conditionals in HTML files using Flask (Jinjai) syntax.
- Link CSS & JS files to HTML files using Flask (Jinjai) syntax. 

## Motivation
Just like the motivation from **Flask Routing**:
- Pretty much every single app you’ve ever used is just some combination of this pattern/mechanism (MVC)
- You’re about to learn start learning how to implement **MVC**, starting with **Flask** - The controller, and using the **templates** (HTML pages) as views.  
And on top of that:
- Advanced Flask helps us make our web applications ***dynamic***; meaning we can customize better user experiences!


## Lesson Plan  


#### ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) Very Important:
    - Make sure to do a demo after each section.
    - Here's a "Prebuilt Repl.it": https://repl.it/@Loai17/Flask-App-Setup - to use for demoing.
    - This will help keep students on track and not lose focus/get confused with all the syntax.

- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) **Slide 3:** Let's discuss the previous session's microFeedback results, discuss any notes that are worth talking about according to the survey results. and make sure to address those who are in panic zone.
- **Slide 4:** Quick review, of previous session, and anything else worth reviewing according to the microFeedback survey.  

- **Slide 5: Why is Advanced Flask so awesome?**

- **Slide 7: How to pass data to views?**
    - Note animations!
    - Explain that the arguments that get assigned in `render_template()` function is the `data` that **gets sent** to the **HTML file** (our view).
    - **Point out** to the Jinjai/Flask **syntax** in `hello_vars.html` → `{{ }}` 

- **Slide 9: How to loop through passed data? (Part 1. Flask)**
    - Firstly, we send the data to our view (or template/HTML file)
    - Notice that we are using the same method we just learned in **Slide 6**. 
    - Notice that this works also if the variable was a `list`.

- **Slide 10: How to loop through passed data? (Part 2. HTML)**
    - Secondly, we **loop through** the `data`! (In our case, the list)
    - Explain that in `{% %}` you can use `for loops`. (and “if & else” statements. but we're reaching this in a bit)
    - Also explain that you have to **end** for loops and if statements using `{% endfor %}` and `{% endif %}`.

- **Slide 11: Interactive Practice (Mini lab)**
    - ![#F6E33C](https://via.placeholder.com/15/F6E33C/000000?text=+) **Mini Lab Prompt:**
        - You will now clone this [Repl.it](https://repl.it/@Loai17/Flask-App-Setup).
        - And make a list of your partner’s favorite food in your `Flask` app.
        - Pass it to `home.html` and display it using `for loops`!
        - Open up your laptops! You have 5 minutes...
        - Ready? Go!
    - After 5 minutes is done, Show what you came up with to your neighbor!
    - Close laptops screens when done.
    - **Note:** make sure **all students** nail this practice. Look out for weaker students.

- **Slide 13:**
    - Say: "We can also ***pass*** data as booleans!". And point out to `no_pets=False`.

- **Slide 14: Using conditionals in HTML (Flask Syntax)**
    - Make sure students understand that using conditionals here, works just like using conditionals in `pyhon`!
    - We just have to surround the line codes with `{% %}` so that Flask understands it.
    - Emphasize that we always should point out to Flask, where does our Flask syntax/code ends?
        - This is why it's important to always use `{% endif %}` when we're done with our Flask code.
       
- **Slide 14: Interactive Practice (Mini lab)**
    - ![#F6E33C](https://via.placeholder.com/15/F6E33C/000000?text=+) **Mini Lab Prompt:**
        - Let’s handle errors!
        - You will now continue on the first cloned Repl.it.
        - Use conditionals to check if `fav_food` list is empty, it should say `“No current items in the database!”` (or something similar.) and display this as a text in `home.html`!
            - Feel free to adjust what your **view** says, maybe come up with a funny sentence, like: `“Woah! Absolutely 0 favorite foods were found! Are you even human????”`
        - Open up your laptops! You have 5 minutes...
        - Ready? Go!
    - After 5 minutes is done, Show what you came up with to your neighbor!
    - Close laptops screens when done.
    - **Note:** make sure **all students** nail this practice as well. Look out for weaker students.

       
- **Slide 17:**
    - Explain that the function `url_for('function_name')` **links** to a route’s **function** in the main `app.py` file.
    - For example, when clicking on the `<a>` tag that is linked to `url_for('home')`, it takes us to `home.html`; because this is the result of `home` function in `app.py` flask app.
    
- **Slide 18:**
    - Also, `url_for('static', filename='file_path')` links to any file in `static` folder!
    - Same thing goes for linking `.js` files/Images...etc.

- **Slide 19: Lab time!**
    - Send students to lab time.
- At the end of session, draw students' attention back to the lecture, discuss our **Takeaways**, and leave them with a **cliffhanger** in the "Next session" slide!
    
- Don't forget to collect everyone's microFeedback before letting students out of class!




## Conclusions/Takeaways
- Still very important to emphasize on: `Our Flask app is effectively the controller (MVC)!`
- Using Flask framework, we can **pass data** from **our app**, and **send it** to our **views**… or in other words, our **HTML files**.
- Using Flask framework, we can **loop** through **passed data** in our **views**. And even use **conditionals**! This way we can turn our views to be ***dynamic***.


## Hints & Hurdles
- Students might be confused of all the syntax used in HTML files... Make sure they know **it's ok**, they don't have to *fully* understand them, just understand that this is the "syntax" for getting data from our **Flask** app, porting it to our HTML files. This is the way it is and how it works.

