#!/usr/bin/env python

from fastapi import FastAPI
from src.Application.App import App


api = FastAPI()

app = App()

@api.get('/')
def index():
    try:
        app.api_service().run()
        return {'status': 0, 'message': 'Data saved to CSV successfully'}
    except Exception as e:
        return {'status': -1, 'message': f'An error occurs fetching data and saving to CSV: {e}'}
