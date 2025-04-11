#!/bin/sh


sqlite3 -header -csv db.sqlite3 "select * from api_app_measurementitem;" > data.csv
