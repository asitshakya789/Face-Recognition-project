import cv2
import face_recognition

known_face_encoding = []
known_face_name = []

known_person_image = face_recognition.load_image_file(r"C:\Users\asits\OneDrive\Desktop\face38\Picture (22).jpg")
known_person1_image = face_recognition.load_image_file(r"C:\Users\asits\OneDrive\Desktop\face38\photo (2).jpg")
known_person2_image = face_recognition.load_image_file(r"C:\Users\asits\OneDrive\Desktop\face38\1662703260529.jpeg")
known_person3_image = face_recognition.load_image_file(r"C:\Users\asits\OneDrive\Desktop\face38\Virat_Kohli.jpg")
known_person4_image = face_recognition.load_image_file(r"C:\Users\asits\OneDrive\Desktop\face38\Screenshot 2023-12-19 174703.png")
known_person5_image = face_recognition.load_image_file(r"C:\Users\asits\OneDrive\Desktop\face38\Screenshot 2023-12-19 010945.png")

known_person_encoding = face_recognition.face_encodings(known_person_image)[0]
known_personl_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]
known_person4_encoding = face_recognition.face_encodings(known_person4_image)[0]
known_person5_encoding = face_recognition.face_encodings(known_person5_image)[0]

known_face_encoding.append(known_person_encoding)
known_face_encoding.append(known_personl_encoding)
known_face_encoding.append(known_person2_encoding)
known_face_encoding.append(known_person3_encoding)
known_face_encoding.append(known_person4_encoding)
known_face_encoding.append(known_person5_encoding)

known_face_name.append("Asit kumar")
known_face_name.append("Dheeraj kumar")
known_face_name.append("Narendra Modi ")
known_face_name.append("Virat kohli")
known_face_name.append("Kaushal kumar")
known_face_name.append("Amit kumar")

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
        else:
            name = "Unknown"
            efficiency_text = ""

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        cv2.putText(frame, efficiency_text, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
