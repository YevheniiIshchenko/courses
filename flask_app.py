from flask import Flask, request
from faker import Faker
import string
import requests

app = Flask(__name__)

fake = Faker('uk_UA')

def read_file(filename):
    f = open(filename)
    text = f.read()
    f.close()
    return text

def users(count: int):
    res = ""
    for _ in range (count):
        res+=fake.name()+' '+fake.email()
    return res

def get_value():
    count = request.args.get("count",'100')
    if not count.isdigit():
        return "Invalid value count"
    if 0<=int(count)<=120:
        count = int(count)
    else:
        return "Invalid value count"
    return users(count)

def find_mean():
    text=read_file("hw.csv")
    lines = text.splitlines()
    sum_weight=0
    sum_height = 0
    count = 0
    for i in range(1,len(lines)-1):
        lines[i] = lines[i].replace(' ',',')
        line = lines[i].split(',,')
        sum_height+=float(line[1])*2.54
        sum_weight+=float(line[2])/2.205
        count+=1
    return str(sum_height/count)+' '+str(sum_weight/count)

def astros():
    r = requests.get("http://api.open-notify.org/astros.json")
    return str(r.json()["number"])


#view-functions
@app.route('/requirements/')
def requirements():
    return read_file("requirments.txt")


@app.route('/generate-users/')
def gen_users():
    return get_value()



@app.route('/mean/')
def mean():
    return find_mean()



@app.route('/space/')
def space():
    return astros()



if __name__ == '__main__':
    app.run()

#This string is just for pull request