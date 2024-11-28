import cv2
import face_recognition
from deepface import DeepFace

known_face_encoding = []
known_face_name = []

# Load known images
known_person_image = face_recognition.load_image_file(r"Asit picture.jpg")
known_person1_image = face_recognition.load_image_file(r"Dheeraj picture.png")
known_person2_image = face_recognition.load_image_file(r"shahid.jpg")
known_person3_image = face_recognition.load_image_file(r"Sharaddha.jpg")
known_person4_image = face_recognition.load_image_file(r"Tamanna.jpeg")
known_person5_image = face_recognition.load_image_file(r"virat.png")

# Encode known faces
known_face_encoding.append(face_recognition.face_encodings(known_person_image)[0])
known_face_encoding.append(face_recognition.face_encodings(known_person1_image)[0])
known_face_encoding.append(face_recognition.face_encodings(known_person2_image)[0])
known_face_encoding.append(face_recognition.face_encodings(known_person3_image)[0])
known_face_encoding.append(face_recognition.face_encodings(known_person4_image)[0])
known_face_encoding.append(face_recognition.face_encodings(known_person5_image)[0])

# Known names
known_face_name.append("Asit kumar")
known_face_name.append("Dheeraj kumar")
known_face_name.append("Shahid kapoor")
known_face_name.append("Sharaddha khapra")
known_face_name.append("Tamanna Bhatia")
known_face_name.append("Virat kohli")

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    face_location = face_recognition.face_locations(frame)
    face_encoding = face_recognition.face_encodings(frame, face_location)

    for (top, right, bottom, left), face_encoding_single in zip(face_location, face_encoding):
        distances = face_recognition.face_distance(known_face_encoding, face_encoding_single)
        min_distance_index = distances.argmin()

        if distances[min_distance_index] < 0.6:  # You can adjust the threshold as needed
            name = known_face_name[min_distance_index]
            efficiency = 1 - distances[min_distance_index]
            efficiency_text = f"Efficiency: {efficiency:.2%}"

            # Age estimation
            try:
                age_prediction = DeepFace.analyze(frame[top:bottom, left:right], actions=['age'], enforce_detection=False)
                age = age_prediction[0]['age']
                age_text = f"Age: {age}"
            except Exception as e:
                age_text = "Age: N/A"

        else:
            name = "Unknown"
            efficiency_text = ""
            age_text = ""

        # Draw rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        cv2.putText(frame, efficiency_text, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, age_text, (left, bottom + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()