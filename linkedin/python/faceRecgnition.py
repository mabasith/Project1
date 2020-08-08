import face_recognition
image_of_person_1 = face_recognition.load_image_file("person_1.jpg")
image_of_person_2 = face_recognition.load_image_file("person_2.jpg")
image_of_person_3 = face_recognition.load_image_file("person_3.jpg")

person_1_face_coding = face_recognition.face_encodings(image_of_person_1)[0]
person_2_face_coding = face_recognition.face_encodings(image_of_person_2)[0]
person_3_face_coding = face_recognition.face_encodings(image_of_person_3)[0]

known_face_encodings = [person_1_face_coding,person_2_face_coding,person_3_face_coding]
unknown_image = face_recognition.load_image_file("unknown_8.jpg")
face_locations = face_recognition.face_locations(unknown_image, number_of_times_to_upsample=2)
unknown_face_encodings = face_recognition.face_encodings(unknown_image ,known_face_locations=face_locations)

for unknown_face_encoding in unknown_face_encodings:
    results = face_recognition.compare_faces(known_face_encodings,unknown_face_encoding)

    name = "unknown"
    if results[0]:
        name ="Person_1"
    elif results[1]:
        name ="Person_2"
    elif results[2]:
        name ="Person_3"
    print("found {name} in the photo!")