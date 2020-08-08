from PIL import Image, ImageDraw
import face_recognition

image = face_recognition.load_image_file("people.jpg")

face_landmarks_list = face_recognition.face_landmarks(image)
pil_image = Image.fromarray(image)

d = ImageDraw.Draw(pil_image,"RGBA")

for face_landmarks in face_landmarks_list:
    d.line(face_landmarks["left_eyebrow"], fill=(128, 0 , 128, 100), width=3)
    d.line(face_landmarks["right_eyebrow"], fill=(128, 0 , 128, 100), width=3)
    d.polygon(face_landmarks["top_lip"], fill=(128, 0 , 128, 100))
    d.polygon(face_landmarks["bottom_lip"],fill=(128, 0, 120,100))
pil_image.show()