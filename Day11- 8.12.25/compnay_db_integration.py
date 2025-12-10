
from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

DB = {
    "host": "localhost",
    "user": "root",
    "password": "Kanishq@0610",
    "database": "company",
    # "cursorclass": pymysql.cursors.DictCursor,
    # "autocommit": True
}

