# flask 모듈 임포트
from flask import Flask, render_template, Response
import datetime
import camera

# flask 객체 생성
app = Flask(__name__)
# 라우터 등록
@app.route('/') # 메인 페이지 주소
def index():
    return render_template('main.html')

@app.route('/fireStatus') # 화재현황
def fireStatus():
    return render_template('fireStatus.html')

@app.route('/fire') # 화재
def fire():
    return render_template('fire.html')

@app.route('/camera') # 카메라
def camera_test():
    return render_template('camera.html')

@app.route('/loc_occur') 
def loc_occur():
    return render_template('fire_occur.html')

@app.route('/human_damage') 
def human_damage():
    return render_template('fire_human_damage.html')

@app.route('/money_damage') 
def money_damage():
    return render_template('fire_money_damage.html')

def gen(camera):
    while True:
        #get camera frame
        frame = camera.frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               
@app.route('/video_feed')
def video_feed():
    return Response(gen(camera.VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# 서버실행
app.run('127.0.0.1',5000,debug=True)