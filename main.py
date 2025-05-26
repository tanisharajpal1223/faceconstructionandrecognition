import os
import cv2
import face_recognition

from tkinter import Tk, Label, Button, filedialog, simpledialog, Toplevel
from PIL import Image, ImageTk

known_criminals_folder = "images"
known_encodings = []
known_names = []
criminal_bios = {}

flag = 0

def load_known_criminals():
    for file_name in os.listdir(known_criminals_folder):
        image_path = os.path.join(known_criminals_folder, file_name)
        name = os.path.splitext(file_name)[0]
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_encodings.append(encoding)
        known_names.append(name)

def match_criminal():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"
            flag = 1
            if True in matches:
                matched_indices = [index for index, match in enumerate(matches) if match]
                first_match_index = matched_indices[0]
                name = known_names[first_match_index]
                flag = 0

                if name in criminal_bios:
                    bio_data = criminal_bios[name]
                    show_bio_data_dialog("Matched Criminal Bio Data", bio_data)

            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 0), 2)  # Black rectangle
            if flag == 0:
                cv2.putText(frame, "Matched Criminal: " + name, (left - 40, top - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                            (255, 255, 255), 2)  # White text
            else:
                cv2.putText(frame, "Not Matched", (left, top - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255),
                            2)  # White text
        cv2.imshow('Forensic Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def add_criminal():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                           filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")))
    if file_path:
        image = cv2.imread(file_path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(rgb_image)[0]
        name = simpledialog.askstring("Add Criminal", "Enter the name of the criminal:")
        if name:
            age = simpledialog.askstring("Add Criminal", "Enter the age of the criminal:")
            height = simpledialog.askstring("Add Criminal", "Enter the height of the criminal:")
            race = simpledialog.askstring("Add Criminal", "Enter the race of the criminal:")
            criminal_records = simpledialog.askstring("Add Criminal", "Enter the criminal records of the criminal:")

            bio_data = f"Name: {name}\nAge: {age}\nHeight: {height}\nRace: {race}\nCriminal Records: {criminal_records}"

            if bio_data:
                known_encodings.append(encoding)
                known_names.append(name)
                criminal_bios[name] = bio_data
                file_name = name + ".jpg"
                save_path = os.path.join(known_criminals_folder, file_name)
                cv2.imwrite(save_path, image)

                # Display the added criminal image and success message in the same dialog box
                dialog = Toplevel(root)
                dialog.title("Criminal Added")

                # Add the image to the dialog using grid layout
                added_image = Image.fromarray(rgb_image)
                added_photo = ImageTk.PhotoImage(added_image)

                added_label = Label(dialog, image=added_photo)
                added_label.image = added_photo
                added_label.grid(row=0, column=0, padx=10, pady=10)

                # Add the success message below the image
                success_label = Label(dialog, text="Criminal added successfully.", font=("Helvetica", 10))
                success_label.grid(row=1, column=0, pady=10)

                # Wait for the dialog to close before printing the success message
                dialog.wait_window(dialog)
                print("Criminal added successfully.")

def upload_and_match():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                           filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")))
    if file_path:
        unknown_image = face_recognition.load_image_file(file_path)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        matches = face_recognition.compare_faces(known_encodings, unknown_encoding)
        name = "Unknown"
        if True in matches:
            matched_indices = [index for index, match in enumerate(matches) if match]
            first_match_index = matched_indices[0]
            name = known_names[first_match_index]

            if name in criminal_bios:
                bio_data = criminal_bios[name]
                show_bio_data_dialog("Matched Criminal Bio Data", bio_data)

        match_label.config(text="Matched Criminal: " + name)

def show_bio_data_dialog(title, bio_data):
    dialog = Toplevel(root)
    dialog.title(title)
    dialog.geometry("300x200")
    dialog.configure(background="#000000")  # Black background

    bio_label = Label(dialog, text=bio_data, font=("Helvetica", 10), background="#000000",
                      foreground="#FFFFFF")  # White text
    bio_label.pack(pady=20)

# Tkinter setup
root = Tk()
root.title("Forensic Face Recognition")
root.geometry("500x400")

# Load background image
bg_image_path = os.path.join("background", "imgback.jpg")
bg_image = Image.open(bg_image_path)
bg_photo = ImageTk.PhotoImage(bg_image)

# Set background image
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Configure root
root.configure(background="#000000")  # Black background

label = Label(root, text="Welcome to the Forensic Face Recognition System", font=("Helvetica", 12),
              background="#D3D3D3", foreground="#000000")  # White text
label.pack()

# Define a style for the button with black background and green text
button_style = {'background': '#008000', 'foreground': '#FFFFFF', 'borderwidth': 2, 'relief': 'flat'}

match_button = Button(root, text="Match Criminal", command=match_criminal, **button_style)
match_button.pack(pady=10)

add_button = Button(root, text="Add Criminal", command=add_criminal, **button_style)
add_button.pack(pady=10)

upload_button = Button(root, text="Upload and Match", command=upload_and_match, **button_style)
upload_button.pack(pady=10)

match_label = Label(root, text="Matched Criminal: ", background="#D3D3D3", foreground="#000000")  # Black background, White text
match_label.pack()

root.mainloop()
