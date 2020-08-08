import PIL.Image
import PIL.ImageDraw
import face_recognition
image = face_recognition.load_image_file("people.jpg")
face_lankdmarks_list = face_recognition.face_landmarks(image)
number_of_faces = len(face_lankdmarks_list)
pil_image = PIL.Image.fromarray(image)
draw = PIL.ImageDraw.Draw(pil_image)

for face_lankdmarks in face_lankdmarks_list:
    for name, list_of_points in face_lankdmarks.items():
        print("The {} in this face has the following points:{}")
        draw.line(list_of_points,fill="red",width=2)
pil_image.show()