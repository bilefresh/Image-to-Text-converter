from flask import Flask, render_template, request, send_file
from vision_api import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        f = request.files['file']
        file = f.read()

        image_type = str(request.form['type'])
        print(image_type)
        global txt_name, result
        txt_name = f.filename
        print(txt_name)
        result = convert(file, image_type, txt_name)

        file = txt_name+".txt"
        return send_file(file, as_attachment=True)
        
    return render_template('index.html')
		
if __name__ == '__main__':
   app.run(debug = True)
