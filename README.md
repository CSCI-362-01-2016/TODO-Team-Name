#TODO-Team-Name
1) Requirements
- Python 2.7
- JythonMusic

2) How to get JythonMusic and Python 2.7

- You can install the Jython Music package here: -https://jythonmusic.me/download/

- Use the following commands to install python 2.7 from repository if you are having trouble with execution

-  sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7
-  sudo apt-get update 
-  sudo apt-get install python2.7

3) How to run Testing Framework
- Navigate to Test Automation directory
- Execute the following:

-- **./scripts/runAllTests.sh**

4) Results will open as an html file in your default browser.
- The Results column compares the output to expected output(oracle) and determines whether the test passed or failed.
- The final results html is located in the TestAutomation/reports directory

5) The format of each test case is as follows:

- Test number
- Requirement
- Component being tested
- Method being tested
- Inputs
- ExpectedOutput

6) To add a new test:
- Add a test case txt file to the TestAutomation/testCases in the forementioned format
- Add the python test to TestAutomation/project/Jython/library, with the same name as line one of your txt file
