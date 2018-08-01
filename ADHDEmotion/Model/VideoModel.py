import cv2
class VideoModel():
    def readVideo(self, filename):
        cap = cv2.VideoCapture(filename)

        while cap.isOpened():
            print cap.isOpened()
            ret, frame = cap.read()


            if frame is not None:
                # convert to gray scale
                gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #face cascade
                face_cascade = cv2.CascadeClassifier("data/xml/haarcascade_frontalface_default.xml")
                #eye cascade
                eye_cascade = cv2.CascadeClassifier("data/xml/haarcascade_eye.xml")
                #mouth cascade
                mouth_cascade = cv2.CascadeClassifier("data/xml/haarcascade_mcs_mouth.xml")


                #detect faces
                faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

                for(x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    #upper face
                    roi_gray_up = gray_img[y:y+(h/2), x:x+w]
                    roi_color_up = frame[y:y+(h/2), x:x+w]
                    #bottom face
                    roi_gray_bt = gray_img[y+int(round(h/1.5)):y+h, x:x+w]
                    roi_color_bt = frame[y+int(round(h/1.5)):y+h, x:x+w]
                    #detect eyes
                    eyes = eye_cascade.detectMultiScale(roi_gray_up, 1.5, 7)
                    nLimit = 0
                    for (xe, ye, we, he) in eyes:
                        if nLimit == 2:
                            break
                        nLimit += 1
                        cv2.rectangle(roi_color_up, (xe, ye), (xe+we, ye+he), (0, 255, 0), 2)


                    #detech mouth
                    mouths = mouth_cascade.detectMultiScale(roi_gray_bt, 1.6, 11)
                    nLimit = 0
                    for(xm, ym, wm, hm) in mouths:
                        if nLimit == 1:
                            break
                        nLimit += 1
                        cv2.rectangle(roi_color_bt, (xm, ym), (xm+wm, ym+hm), (0, 0, 255), 2)



            else:
                break

            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


