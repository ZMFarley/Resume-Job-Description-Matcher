# Welcome
Welcome to The Resume Job Matcher (RJM), an ML project intended as the final project submission for our group  for CIS490 (Machine Learning) at UMass Dartmouth. The intention of this project were to combine a React/TS UI with word similarity models and a classifer to compare and match how well a resume fits for a given job description. 

# How to Use 
See the attached requirements.txt for all relevant and necessary dependencies to run RJM properly. 

As such, ensure the operating machine has Python 3.xx installed, and use the following commands: -m venv .venv to create a virtual enviornment, and .\.venv\Scripts\activate, to allow for its operation.

However, for regular use of the application itself, first open two terminals in command prompt (or any of your choosing), and open the virtual enviornment using .\.venv\Scripts\activate. Then in one terminal, cd to core and run uvicorn api:app --reload --host 127.0.0.1 --port 8000 to enable the uvicorn web server for FastAPI to operate on, and in the other terminal, cd to frontend, and run npm dev, to enable the locally hosted browser application to run.


# Dataset Information


# Work Flow Diagram

# Future Plans 
