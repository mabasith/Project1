#!/usr/bin/dev python
import face_recognition
image = face_recognition.load_image_file("people.jpg")
face_encodings = face_recognition.face_encodings(image)
if (len(face_encodings) == 0):
    print("No face where found")
else:
    first_face_encoding = face_encodings[0]
    print(first_face_encoding)