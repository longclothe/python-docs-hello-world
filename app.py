# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, yangfan chen!"
# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from numpy.core.numeric import NaN
from werkzeug.utils import escape, secure_filename
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def first():
    df = pd.read_csv('static/uploads/names.csv')
    df.Picture = "<img src = \"static/uploads/"+df['Picture']+"\"height=\"100\" width = \"100\"/>"

    df.insert(df.shape[1],"Change",["" for i in range(df.shape[0])])
    
    for i in range(df.shape[0]):
        df["Change"][i]="<a href=\"/change_grade_picture?name="+"\'"+df['Name'][i]+"\'"+"\"><button>Click it !</button></a>"
    return "<font size=\"6\" color=\"red\">This is 1001889074 Yangfan Chen</font>"+"<br>"+df.to_html(escape=False)
    # return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['select']
        basepath = os.path.dirname(__file__)  
        upload_path = os.path.join(basepath,'static/uploads',secure_filename(f.filename))  
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

	return "<font size=\"6\" color=\"red\">This is 1001889074 Yangfan Chen</font>"+"<br>"+render_template('search.html')

@app.route('/sp')
def get_result():
    key = request.args.get('wd')
    data = pd.read_csv("static/uploads/names.csv")
    # data = data.loc[data['State']==key]
    data = data[data.Caption.contains(key)]

    data.Picture = data['Picture']+"<img src = \"static/uploads/"+data['Picture']+"\"height=\"100\" width = \"100\"/>"

    return data.to_html(escape=False)
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

@app.route('/change_grade_picture',methods=['POST', 'GET'])
def change_grade_picture():
    name=request.args.get('name').strip('\'')
    # print(name)
    if request.method == 'POST':
        new_points = request.form.get('points')
        new_picture = request.form.get('pic_name')
        df = pd.read_csv("static/uploads/names.csv")
        df.Grade[df['Name']==name] = new_points
        df.Picture[df['Name']==name] = new_picture
        df.to_csv("static/uploads/names.csv",index=False)
        # df = pd.read_csv("static/uploads/names.csv",index_col=False)
        return redirect(url_for('first'))

    return render_template('change_grade_picture.html')

@app.route('/search_picture')
def search_picture():


    return "<font size=\"6\" color=\"red\">This is 1001889074 Yangfan Chen</font>"+"<br>"+render_template('search_picture.html')

@app.route('/picture_result')
def get_picture_result():
    key = request.args.get('name')
    data = pd.read_csv("static/uploads/names.csv")
    data = data.loc[data['Name']==key]
    
    # data.insert(data.shape[1],"Picture_Name",["" for i in range(data.shape[0])])

    # for i in range(data.shape[0]):
        
    #     data["Picture_Name"][i]=data['Picture'][i]

    data.Picture = data['Picture']+"<img src = \"static/uploads/"+data['Picture']+"\"height=\"100\" width = \"100\"/>"

    # data.insert(data.shape[1],"Picture_Name",["" for i in range(data.shape[0])])



    # for i in range(data.shape[0]):
    #     if data["Picture"][i]== NaN:
    #         data["Picture_Name"][i]=NaN
    #     else:
    #         data["Picture_Name"][i]=data['Picture'][i]
    return "<font size=\"6\" color=\"red\">This is 1001889074 Yangfan Chen</font>"+"<br>"+data.to_html(escape=False)


@app.route('/search_room')
def search_room():


    return "<font size=\"6\" color=\"red\">This is 1001889074 Yangfan Chen</font>"+"<br>"+render_template('search_room.html')


@app.route('/room_result')
def get_room_result():
    key = request.args.get('room')
    data = pd.read_csv("static/uploads/names.csv")
    # data = data.loc[data['Room']==int(key)]
    


    data.Picture = "<img src = \"static/uploads/"+data['Picture']+"\"height=\"100\" width = \"100\"/>"
    

    data.insert(data.shape[1],"Change",["" for i in range(data.shape[0])])
    
    for i in range(data.shape[0]):
        data["Change"][i]="<a href=\"/change_room_number?name="+"\'"+data['Name'][i]+"\'"+"\"><button>Change Room Number !</button></a>"
    data = data.loc[data['Room']==int(key)]

    return "<font size=\"6\" color=\"red\">This is 1001889074 Yangfan Chen</font>"+"<br>"+data.to_html(escape=False)

@app.route('/change_room_number',methods=['POST', 'GET'])
def change_room_number():
    name=request.args.get('name').strip('\'')
    # print(name)
    if request.method == 'POST':
        new_number = request.form.get('new_number')
        # new_picture = request.form.get('pic_name')
        data = pd.read_csv("static/uploads/names.csv")
        data = data.loc[data['Name']==name]
        data.Room[data['Name']==name] = new_number
      
        data.to_csv("static/uploads/names.csv",index=False)
        # df = pd.read_csv("static/uploads/names.csv",index_col=False)
        return redirect(url_for('search_room'))

    return render_template('change_room_number.html')





if __name__ == '__main__':
    app.run(debug=True)