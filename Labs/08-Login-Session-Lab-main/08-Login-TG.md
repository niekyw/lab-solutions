# Teacher Guide: Flask Login Session

## SWBATs
- Get some additional tips/review of how to **handle errors**!
- Know how to use **Try & Except** for error handling.
- Get introduced to **Login Session** and understand what will we be using it for.
- Use **Login Session** and adapt it to their app's needs.


## Motivation
**For Error Handling:**  
- We're at a learning stage where we are learning intense and somewhat can be very confusing topics, and as a result we may be facing frequent errors while coding! This mini section was placed here to review and remind students of how we can face and handle errors effectively and efficiently. 
- **Try & Except** doesn't crash the app when an error occurs. 
- For instructors: If there are frequent specific **other** errors most students are facing, feel free to adapt it and teach students how to resolve it in this section!

**For Flask Login Session:**
- **Login Session** allows us to have access to user data across routes.
- **Login Session** will greatly help us when we learn Firebase Auth & Database.

## Lesson Plan
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) **Slide 3:** Let's discuss the previous session's microFeedback results, discuss any notes that are worth talking about according to the survey results. and make sure to address those who are in panic zone.
- **Slide 4:** Quick review, of previous session, and anything else worth reviewing according to the microFeedback survey.
    - Say "Ok, Quick review **over**!", to draw students' attention to the lecture and inform them that we are starting today's lecture.

- **Slides 5-9: Error Handling (Slide-by-Slide Prompt)**
    - Slide 5: Let's review a couple items in **error handling** before we start! 
    - Slide 6: When facing an error when coding, you'll be presented with a block of lines that look like this. [Point out to the image on the slide]
        - Now, all of this looks like a mess! But don't panic, if we break it down a bit, we might find it easier to understand!
    - Slide 7: When error handling, we always **start from the last line** python threw at us! Let's start with reading it:
        - It will show us: `The Type of the error` (Exception), and a `“helpful message”`.
        - `Indentation Error` means there is a mix-up in the `tabs` and `spaces` you have in your code. They should be consistent. (Meaning, either all of them are `spaces`, or all of them are `tabs`, and each `tab` is exactly  `4 spaces`.)
    - Slide 8: But let's say we didn't understand what `Identation Error` means! We move up a block,this is the Line that the error occurred at; it displays (and Instructors should point out to):
        - The filename
        - The line number
        - The line of code that caused the error.
    - Slide 9: We have found our error! In line 15 & 16 we use a `tab`, while in line 17 we use `4 spaces`! We can't mix this up.
        - We can find the difference if we highlight all of our code! (Only in Sublime)

- **Slide 10: PEP (Personal Empowerment Protocol)**
    - Emphasize to students that it's very important to **embrace error messages**!
    - Error messages are like breadcrumbs for finding our solutions.
    - We shouldn't be afraid/dissapointed when we face error messages, we just have to remember practicing PEP!!
        - Go over PEP steps.
    - It's critical to keep setting this tone and culture in the classroom. It's what will make our students' mindset - a leader's mindest.
    
    
- **Slides 11-16: Try & Except (Explanation and Examples)**
    - Slide 12:
        - `Try & Except` : are a python statement used to handle errors.
        - `Try` : contains the code we suspect might error, and tries to run the code.
        - `Except` : If the the code in the Try errors the code will stop the try block and run the except block instead.
    - Slide 14: 
        - Let's look at it logically with an example, We want to wash our dishes so we go to the sink to wash the dishes.
        - If the sink has dishes so we will wash them, except if there aren't any dishes we won't be able to wash anything.
    - Slide 15: 
        - The function above turns a string into an int, but not every string can be changed to an int therefore here we can use Try & Except to help us.
        - In the Example we have the string is `"5"` so it can be changed to an int and will the code in the try normally without going to the except.
    - Slide 16:
        - j is not a number therefore the code block in the try will error and will go instead to the except and print "Input is not a number".
    
- **Slides 17-24: Login Session (Explanation and Examples)**
    - Slide 18: Login Session is a dictionary created for the user once he enters the website and is uniquely tailored to them, it is available between all routes and updates between all of them.
    - Slide 19:
        - The login session dictionary is created from the time the user goes to the website and until the time he leaves it.
        - As we said it is a dictionary unique for each individual user.
    - Slide 20: Since Login Session is a dictionary the syntax is exactly the same. to store a value we simply write the key inside brackets and assign it its value.
    - Slide 21: A user might go to route that uses a value from the Login Session, and sometimes he goes before the value is assigned, Therefore we should check if the key exists before trying to retrieve a value with it.
    - Slide 22: Retrieving the value is exactly like a dictionary.
    - Slide 23: As we said sometimes when we try to retrieve a value, we are not sure that the key exists in the Login Session therefore here we can use Try & Except to help us handle errors.


- **Slide 24: Lab time!**
    - Send students to lab time.
- At the end of session, draw students' attention back to the lecture, discuss our **Takeaways**, and leave them with a **cliffhanger** in the "Next session" slide!
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) Don't forget to collect everyone's microFeedback before letting students out of class!



## Conclusions/Takeaways
- When errors show up at our front door, simply read them to find the reason they’re here!
- Login Session will allow us to have attributes about our user between all routes.
- Login Session is a dictionary and works exactly the same.


## Hints & Hurdles
- If students are confused why they are learning this, tell them it will support us greatly when we learn databases.
- The syntax is clear and most students will understand it quickly, but the concept might be confusing so make sure to take your time with it.

