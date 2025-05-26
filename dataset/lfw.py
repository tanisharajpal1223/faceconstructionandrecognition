from sklearn.datasets import fetch_lfw_people
lfw_dataset = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
faces_data = lfw_dataset.image
labels = lfw_dataset.target
