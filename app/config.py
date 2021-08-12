""" This file handle configuration data of the flask app """
import os


class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
