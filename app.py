# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, yangfan chen!"
# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath,'static/uploads',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
# from flask_uploads import UploadSet, IMAGES
# from flask_uploads import configure_uploads, patch_request_class
# ​
# # 文件上传
# photos = UploadSet('photos', IMAGES)
# # 设置上传文件的地址
# app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()
# # 上传的初始化
# configure_uploads(app, photos)
# # 配置上传文件大小，默认64M，设置None则会采用MAX_CONTENT_LENGTH配置选项
# app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
# patch_request_class(app, size=None)
