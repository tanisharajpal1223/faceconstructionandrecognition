# faceconstructionandrecognition
Face Construction and Recognition Criminal Identification System
This project demonstrates the use of a pre-trained FaceNet model for face recognition, adapted to a Criminal Identification System. It allows law enforcement or security agencies to:

Add new criminal records with personal details and a face image.

Detect criminals in real time using a camera.

Upload an image of a person to identify whether they exist in the criminal database.

Retrieve detailed information about matched individuals (e.g., name, height, criminal history, and ethnicity).

🔍 Features
1. Add a Criminal to the Database
Users can add a new criminal profile by inputting:

Name

Height

Ethnicity

Criminal records

Face image

The image is processed using the FaceNet model to generate a unique face embedding, which is stored for future recognition.

2. Real-time Face Recognition (Live Camera Feed)
The system captures video frames in real time.

Faces detected in the frame are processed and compared against the database.

If a match is found:

A "Criminal Found" message is displayed with a beep alert.

Details of the criminal are shown.

If no match:

A message "Unmatched" is displayed.

3. Upload and Match Face from Image
Users can upload a photo.

The system will process the image and compare it with stored criminal embeddings.

If a match is found:

Criminal's detailed information is displayed.

If no match:

"Unmatched" message is shown.

🧠 Face Recognition using FaceNet
FaceNet Overview:
The system uses the FaceNet model developed by Google, described in the paper:

FaceNet: A Unified Embedding for Face Recognition and Clustering by Florian Schroff, Dmitry Kalenichenko, and James Philbin.

FaceNet maps faces into a high-dimensional embedding space where the distance between two embeddings reflects face similarity.

Model Details:
The model is pre-trained and saved in the file facenet_model.h5.

Embeddings are generated for every face image using this model.

Faces are compared using Euclidean distance between embeddings.

⚙️ Core Components
Model Loading:
model = load_model('facenet_model.h5')
Face Preprocessing:
The function preprocess_faces() prepares raw images for the model:

Face detection

Resizing

Normalization

Embedding Generation:
embedding = model.predict(preprocessed_face)
Face Comparison:
def distance(emb1, emb2):
    return np.linalg.norm(emb1 - emb2)
A threshold is defined to decide if two faces match:

python
if distance(emb1, emb2) < distance_threshold:
    # Match found
🛠 Requirements
Python 3.x

TensorFlow / Keras

OpenCV

NumPy

Other supporting libraries (Pillow, etc.)

🚀 Getting Started
Clone the repository.

Install dependencies.

Add criminal profiles using the UI or CLI.

Start the real-time camera or upload a photo to identify a person.

📝 Notes
The facenet_model.h5 must be present in the working directory.

Adjust the distance_threshold for your specific dataset to fine-tune accuracy.

Real-time recognition performance depends on your system's processing power.



