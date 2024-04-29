# Python App Exercise

## Run the application
- To run this application, you can activate a virtual environment for python and after that, install requirements
- To install requirements, execute: pip install -r requirements.txt
- After that, you will modify the pythonpath to include the curren project
- Once everything is done, execute: uvicorn main:api --reload to launch the API in dev

## Tests
- From the project root folder, execute python -m unittest src/tests/test_api_service.py
