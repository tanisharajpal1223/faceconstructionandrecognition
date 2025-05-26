import pandas as pd

# Sample data
data = {
    'image_path': ['criminal1.jpg', 'criminal2.jpg', 'criminal3.jpg','criminal4.jpg', 'criminal5.jpg','criminal6.jpg', 'criminal7.jpg'],
    'criminal_identity': [' Daud', 'Osama', 'Unknown', 'himani', 'jeff', 'Unknown' , 'elon', 'tanisha', 'Unknown', 'Daud', 'Osama', 'Unknown']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save labeled data to a CSV file
df.to_csv('labeled_data.csv', index=False)
