from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
  
def gen_frames():
#     cam = find_camera(camera_id)  # return the camera access link with credentials. Assume 0?
    # cam = cameras[int(id)]
    cap = cv2.VideoCapture(0)  # capture the video from the live feed
 
    while True:
 
        # # Capture frame-by-frame. Return boolean(True=frame read correctly. )
        success, frame = cap.read()  # read the camera frame
        if not success:
            break
        else:
            frame = cv2.resize(frame, (240,240))
            ret, buffer = cv2.imencode('.jpg', frame)
    
            #객체인식관련 코드 
           #
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
 
 
@app.route('/video_feed', methods=["GET"])
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
 
if __name__ == '__main__':
    app.run(host='59.0.236.2',port=2000)
    app.debug=True
