# BDD Course - python behave

### How to run tests
1. Create a `virtualenv` using PyCharm or in terminal (`virtualenv venv`).
2. Activate virtualenv. On Linux / MacOS: `. ./venv/bin/activate`, on Windows: `.\venv\Scripts\activate`. If
    you use PyCharm for running the tests, just skip this step ;)
3. Install the requirements for the project. Terminal: `pip install -r requirements.txt`; 
PyCharm: open `requirements.txt` file, click in it and choose the option to install the requirements.
4. Create test configuration:
   - create a JSON file that will contain tests configuration named `env_configuration.json` in the root (top) 
   folder of this project;
   - get the app url: ask the trainer to provide it ;)
   - put the following line into it: `{"app_url": "<app url>"}`
5. Now you can run the tests. To do that, please open the terminal and run:
    `behave tests/features`
