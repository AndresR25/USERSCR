from flask import Flask, render_template, request, redirect
from USERSCR.Models.user import User
from USERSCR import app

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("add.html",users = User.get_all())

@app.route('/user/new')
def new():
    return render_template("read.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')