import cv2
import face_recognition

imagem = cv2.imread('essa.jpg')
face_loc = face_recognition.face_locations(imagem)[0]
#print('face_loc',face_loc)
face_image_encodings=face_recognition.face_encodings(imagem, known_face_locations=[face_loc])[0]


#cv2.rectangle(imagem, (face_loc[1], face_loc[0]), (face_loc[1], face_loc[2]), (0, 255, 0))
#cv2.imshow("imagem",imagem)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret == False:
        break

    frame = cv2.flip(frame, 1)

    face_locations = face_recognition.face_locations(frame)
    if face_locations != []:
        for face_location in face_locations:
            face_frame_encodings = face_recognition.face_encodings(frame,known_face_locations=[face_location])[0]
            result = face_recognition.compare_faces([face_frame_encodings], face_image_encodings)
            print('Result', result)

            if result[0] == True:
                text="Victor"
                color = (125,220,0)
            else:
                text = "Desconhecido"
                color = (50, 50, 250)

            cv2.rectangle(frame, (face_location[3],face_location[2]),(face_location[1],face_location[2]), color, -1)
            cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (0, 255, 0), 2)
            cv2.putText(frame, text,(face_location[3],face_location[2] + 20), 2, 0.7, (255, 255, 255), 1)



    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == 27 & 0xFF:
        break

cap.release()
cv2.destroyAllWindows()

