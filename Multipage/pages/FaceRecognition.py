from deepface import DeepFace
import cv2
import time
import streamlit as st

windowsHolder = st.empty()
value = st.empty()
def main():
    cap = cv2.VideoCapture(0)
    while True:
        time.sleep(0.5)
        _, img = cap.read()

        if img is None:
            break

        #cv2.imshow("Window", img)
        windowsHolder.image(img,channels="BGR")
        extract_faces(img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

    return

def extract_faces(raw_img):
    print("Starting recognition")
    test = DeepFace.extract_faces(raw_img, detector_backend="mtcnn",align=True)

    if test:
        faces = []

        for face_obj in test:
            facial_area = face_obj["facial_area"]
            faces.append(
                (
                    facial_area["x"],
                    facial_area["y"],
                    facial_area["w"],
                    facial_area["h"],
                )
            )

        detected_faces = []
        for x, y, w, h in faces:
            detected_face = raw_img[int(y) : int(y + h), int(x) : int(x + w)]
            detected_faces.append(detected_face)
            recognition(detected_face)
            return

def recognition(img):
    dfs = DeepFace.find(
        img_path=img,
        db_path="/Users/futuregadgetlab/Desktop/DB",
        detector_backend="mtcnn",
        model_name="Facenet512",
        distance_metric="euclidean_l2",
        enforce_detection=False,
        silent=True
    )

    found_non_empty_df = False

    for df in dfs:
        if len(df) != 0:
            for _, row in df.iterrows():
                if row["Facenet512_euclidean_l2"] < 0.6:
                    print("Matched!")
                    with value.container():
                        st.write("Matched! Welcome to expo 2023")
                    st.balloons()
                    found_non_empty_df = True
                    break

            if found_non_empty_df:
                break  # Exit the outer loop if a match is found in any DataFrame
        time.sleep(5)

    if not found_non_empty_df:
        with value.container():
            st.warning("You don't exist, my friend!")
if __name__ == "__main__":
    main()