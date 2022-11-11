# flask-kanban-app
A simple productivity tool created with flask. This app includes all the basic functionalities of a Kanban Board (creating new tasks, moving tasks between stages, and delete the tasks), but also includes an extra functionality to update the textual content of a text through the button "update"

## How to run (Windows):
1. Set up the virtual environment (on the command prompt):
    1. Install the virtual environment \
  `pip install virtualenv`
    2. Find the project folder: \
    `cd path_to_file`
    3. Set up the virtual environment\
    `virtualenv env`
    4. Initialize it: \
    `.\env\Scripts\activate\`
2. Install all requirements \
  `pip install -r requirements.txt`
3. Run app.py \
  `python app.py`
4. Visit local host port 5000 on your local browser to interact with the app \
    `http://localhost:5000/`


## How to run (MAC):
1. Set up the virtual environment (on the command prompt):
    1. Install the virtual environment \
  `pip install virtualenv`
    2. Find the project folder: \
    `cd path_to_file`
    3. Set up the virtual environment\
    `python -m venv venv`
    4. Initialize it: \
    `venv\Scripts\activate.bat`
2. Install all requirements \
  `pip install -r requirements.txt`
3. Run app.py \
  `python app.py`
4. Visit local host port 5000 on your local browser to interact with the app \
    `http://localhost:5000/`


Thanks to the amazing CS162 TA, Ha Tran, for all her help along the project. Credits also to the great [tutorial video](https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=2410s) from freeCodeCamp.org for providing a very intuitive guide to complete this project. Credits to Manuel Pinto for the cool [transitioning background](https://1stwebdesigner.com/15-css-background-effects/) you can see in the flask application
