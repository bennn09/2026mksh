#day06_01_spyder_opencv_capture.py
#從Chat得到的程式
#修改自day04_7_processing_java_video_libary_Capture_start_read
import cv2


# 開啟攝影機 (0 表示第一台攝影機)
cam = cv2.VideoCapture(0)

# 設定解析度 (與 Processing 相同 640×480)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #視訊寬度
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #視訊高度

while True: #迴圈一直跑直到,break跳出迴圈結束
    # 讀取一張影像
    ret, frame = cam.read()

    if not ret:#若沒有成功,就離開
        print("無法讀取攝影機")
        break

    # 顯示畫面
    cv2.imshow("Camera", frame)

    #按Esc離開
    if cv2.waitKey(1)==27:
        break

cam.release()# 正確關閉攝影機
cv2.destroyAllWindows()#把剛剛開啟的OpenCV視窗全部關閉