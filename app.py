# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, yangfan chen!"
# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def first():
    df = pd.read_csv('static/uploads/names.csv')
    df.Picture = "<img src = \"static/uploads/"+df['Picture']+"\"height=\"100\" width = \"100\"/>"

    return df.to_html(escape=False)
    # return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['select']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath,'static/uploads',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('upload'))
    names = str(os.listdir('static/uploads'))
    return render_template('upload.html')+"UPLOADS:"+names

@app.route("/table")
def table():
    data = pd.read_csv("static/uploads/names.csv")
    return data.to_html()



@app.route('/search')
def search():
    # key = request.args.get('wd')
    # print(key)

	return "1001889074 Yangfan Chen"+"<br>"+render_template('search.html')

@app.route('/sp')
def get_result():
    key = request.args.get('wd')
    data = pd.read_csv("static/uploads/names.csv")
    data = data.loc[data['Room']==int(key)]
    return data.to_html()
    # return get_html(key)

@app.route('/search_grade')
def search_grade():
    # key = request.args.get('wd')
    # print(key)

	return "1001889074 Yangfan Chen"+"<br>"+render_template('between.html')
@app.route('/bp')
def get_grade():
    low = request.args.get('low')
    high =request.args.get('high')
    data = pd.read_csv("static/uploads/names.csv")
    print(data['Grade'])
    data = data[(data['Grade']>low)]
    data = data[(data['Grade']<high)]
    return data.to_html()

# @app.route('/auto_test_case')
# def auto_test_case():
    
#     form = forms.SearchForm()
#     return render_template('auto_test_case.html', cases=auto_test_case_objs,form=form)


if __name__ == '__main__':
    app.run(debug=True)