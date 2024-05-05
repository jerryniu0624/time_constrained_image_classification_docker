from flask import Flask, request, jsonify, render_template
from torch_utils import transform_image,get_prediction
from werkzeug.utils import secure_filename
import os
import sys
import datetime
import json
expiration_date = datetime.date(2024, 4, 25) + datetime.timedelta(days=180)
current_date = datetime.date.today()

assert current_date < expiration_date
if current_date > expiration_date:
    exit()

app = Flask(__name__)# ,static_folder= os.getcwd() + '/static',template_folder=os.getcwd() + '/templates'
# if getattr(sys, 'frozen', False):
#     template_folder = os.path.join(sys._MEIPASS, 'templates')
#     app = Flask(__name__, template_folder=template_folder)
# else:
#     app = Flask(__name__)
    
# MY_FOLDER = os.path.join('app', 'static/uploads') # debug时
# MY_FOLDER = os.path.join('static/uploads') # 在终端运行时
MY_FOLDER = os.path.join(sys._MEIPASS, 'static/uploads') # 本地运行可执行文件时
UPLOAD_FOLDER = MY_FOLDER

ALLOWED_EXTENTIONS = {'png','jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS

@app.route('/',methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'GET':
        
        filename = request.values.get('filename')
        print(request.values)
        # file = request.files['file']
        # filename = file.filename
        # file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # file.save(file_path)
        
        # if file is None or file.filename == "":
        #     return jsonify({'error':'no-file'})
        # if not allowed_file(file.filename):
        #     return jsonify({'error':"format not supported"})
        
        try:
            # file.seek(0)
            # image_bytes  = file.read()
            tensor = transform_image(filename)
            prediction = get_prediction(tensor) # ([1, 1, 28, 28])
            data = {'prediction': prediction.item(),
                    'filename': filename,
                    'errcode': 1}
            # result = 'The classification result of file:' + str(filename) + ' is ' + str(prediction.item())
            # dict_str = json.loads(result)
            # print(data)
            return data
        except:
            return {'error':'error during prediction',
                    'errcode': 0} # jsonify()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', debug=False, threaded=False, port=8018)