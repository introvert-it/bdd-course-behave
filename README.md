# BDD Course - python behave

### How to run tests
1. Create a `virtualenv` using PyCharm or in terminal (`virtualenv venv`).
2. Activate virtualenv. 
   - On Linux / MacOS: `. ./venv/bin/activate`
   - on Windows: `.\venv\Scripts\activate`
   - If you use PyCharm for running the tests, please open `File -> Settings -> Project: bdd-course-behave -> 
   Python interpreter` and make sure that your virtualenv is selected. If not, click "add interpreter" -> 
   "add local interpreter", select "existing" and pick the one that you just created. Click "Apply".
3. Install the requirements for the project. Terminal: `pip install -r requirements.txt`; 
PyCharm: open `requirements.txt` file, click in it and choose the option to install the requirements.
4. Create test configuration:
   - create a JSON file that will contain tests configuration named `env_configuration.json` in the root (top) 
   folder of this project;
   - get the app url: ask the trainer to provide it ;)
   - put the following line into it: `{"app_url": "<app url>"}`
5. Now you can run the tests. To do that, please open the terminal and run:
    `behave tests/features`

### How to set up behave debugging in PyCharm community edition
Please, follow these simple steps: 
https://levelup.gitconnected.com/how-to-use-pycharm-ce-debugger-with-behave-3396f5b0865d.

### How to create allure results

1. Install allure standalone using [these]([allure-report](allure-report)
[allure-results](allure-results)) steps. Please, note that you need Java
installed before you try installing allure standalone.
2. Open terminal.
3. Run `pip install requirements.txt` to make sure that `allure-pytest-bdd`
is installed.
4. Run tests with allure reports option: 
`behave -f allure_behave.formatter:AllureFormatter -o allure-results ./tests/features`
5. Generate allure report: `allure generate`
6. Open allure report: `allure open`, you should see the report open in 
default browser.

_Note:_ when you're done, click Ctrl + C in the terminal to stop the process
to stop running allure process.

More info about allure can be found [here](https://allurereport.org/docs/how-it-works/)