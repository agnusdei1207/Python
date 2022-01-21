from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/fileupload', methods=['POST'])
def filleupload():
    f = request.files['file']
    dirname = os.path.dirname(__file__) + '/uploads/' + f.filename    # __file__ : 현재파일인 경로를 알려준다.
    f.save(dirname)
    return 'uploads 성공'


if __name__=="__main__":
    app.run()
