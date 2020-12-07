from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")
    

@app.route('/post', methods = ['GET','POST'])
def insert_data():
    return "This is a post url "    

@app.route('/see_flask_py_content', methods = ['GET','POST'])
def insert_data1():
    return render_template("a.html")

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
