from flask import Flask, render_template,request
from check import check_headers 


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    url_input = ''
    res = {}
  
    if request.method == 'POST':
        url_input = request.form['url_input']  
        res = check_headers(url=url_input)  

    return render_template("index.html", url_input=url_input, result=res)


if __name__ == '__main__':
    app.run()
