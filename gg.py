from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    my_name = "stranger"
    return f'Hello, {my_name}!'

@app.route('/me')
def me():
    return render_template("strona1.html")

@app.route('/contact', methods=['GET','POST'])
def kontakt():
    if request.method == 'GET':
        print('We received GET')
        return render_template("strona2.html")
    elif request.method == 'POST':
        print('We received POST')
        print(request.form)
        return redirect('/')