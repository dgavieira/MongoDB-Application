# flask packages
from flask import Flask, app
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager

# local packages
from api.routes import create_routes

# external packages
import os