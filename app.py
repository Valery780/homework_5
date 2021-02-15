from flask import Flask
from faker import Faker
import pandas as pd
import base58
import requests
from csv import reader 

app = Flask(__name__)
fakegen = Faker()

# requirements.txt

@app.route("/requirements/")
def open_req():
    i = open(file="requirements.txt")
    output = i.read()
    return f"{output}"

# fake user names and emails

@app.route("/generate-users/<int:XX>")
def generate_users(XX): 
    global output
    if XX == 0:
        return "Unable to generate users"
    fake = Faker(["en_US"])
    for i in range(XX):
        i = 0
        lst = list()
        output = lst.append([fake.first_name(), fake.email()])
    return f"{output}"

# process csv file
@app.route('/mean/')
def process_file():

    info = csv.reader(csv_file, delimiter = '\t')
    
    height_v = info['"Height(Inches)"']
    weight_v = info['"Weight(Pounds)"']

    index = info.index
    lines_amount = len(index)

    av_height = sum(height_v) / lines_amount
    av_weight = sum(weight_values) / lines_amount
    
    return f'Parsed file: "hw05.csv" 
    \nTotal values in file: {lines_amount} 
    \nAverage height: {round(av_height * 2.54)} cm 
    \nAverage weight: {round(av_weight * 2.2)} kg'

# astronauts
@app.route('/space/')
def astronauts_space():
    r = requests.get('http://api.open-notify.org/astros.json')
    output = r.json()["number"]
    return f'Number of astronauts in space: {output}'

# base58 (encode)
@app.route('/base58encode/<STRING>')
def base58_encode(STRING):
    output = base58.base58encode(STRING)
    return output

# base58 (decode)
@app.route('/base58decode/<STRING_IN_BASE58>')
def base58_decode(STRING_IN_BASE58):
    output = base58.base58decode(STRING_IN_BASE58)
    return output
    

if __name__ == "__main__":
    app.run()









