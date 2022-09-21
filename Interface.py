
from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
db = client.Coding_Results
coll = db.Codes

app = Flask(__name__)

def exam():

    put_markdown("# PRELIMINARY CODING TEST")

    ref_no = input("Enter your reference number: ", type = "text", required = True)
    name = input("Enter your name: ", type = "text", required = True)

    put_text("Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.")
    a1 = textarea('Code 1', code={
    'mode': "python",
    'theme': 'darcula',}, value='# Write your python code')


    put_text("Given an unsorted list of some elements(may or may not be integers), Find the frequency of each distinct element in the list using a dictionary.")
    a2 = textarea('Code 2', code={
    'mode': "python",
    'theme': 'darcula',}, value='# Write your python code')

    put_text("Given two positive integers start and end. The task is to write a Python program to print all Prime numbers in an Interval.")
    a3 = textarea('Code 3', code={
    'mode': "python",
    'theme': 'darcula',}, value='# Write your python code')

    popup('Important Mesage',
        [put_text('Thank you!\nYour responses have been saved.\nMail will sent for final result').style('color: green; font-size: 20px'),
        put_buttons(['Close'], onclick=lambda _: close_popup())], size=PopupSize.NORMAL)


    results = {
        'name': name,
        'reference' : ref_no,
        'sol_1' : a1,
        'sol_2' : a2,
        'sol_3' : a3
    }
    coll.insert_one(results)

app.add_url_rule('/', 'webio_view', webio_view(exam, session_expire_seconds=120),  methods = ['GET','POST','OPTIONS'])

app.run(host = "localhost", port = 5000)

if __name__ == '__main__':
    exam()
