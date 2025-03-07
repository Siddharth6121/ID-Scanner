# import pytesseract
# import cv2
# import re
# import pandas as pd
# from datetime import datetime
# import argparse

# def preprocess_image(image_path):
#     """
#     Preprocess the image for better OCR results.
#     """
#     # Load the image
#     image = cv2.imread(image_path)
#     if image is None:
#         raise ValueError("Image not found or unable to load. Check the file path.")
    
#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # Apply thresholding
#     _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
#     return thresh

# def extract_text(image):
#     """
#     Extract text from the preprocessed image using Tesseract OCR.
#     """
#     text = pytesseract.image_to_string(image)
#     return text

# def extract_data(text):
#     """
#     Extract relevant data (name, birthdate, age) from the OCR text using regex.
#     """
#     data = {}
    
#     # Regex patterns for name, birthdate, and age
#     name_pattern = r"Name:\s*([A-Za-z\s]+)"
#     dob_pattern = r"DOB:\s*(\d{2}/\d{2}/\d{4})"
#     age_pattern = r"Age:\s*(\d+)"
    
#     # Extract name
#     name_match = re.search(name_pattern, text)
#     if name_match:
#         data['Name'] = name_match.group(1).strip()
    
#     # Extract birthdate
#     dob_match = re.search(dob_pattern, text)
#     if dob_match:
#         data['Birthdate'] = dob_match.group(1).strip()
#         # Calculate age
#         birthdate = datetime.strptime(data['Birthdate'], "%m/%d/%Y")
#         today = datetime.today()
#         age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#         data['Age'] = age
    
#     # Extract age (if explicitly mentioned)
#     age_match = re.search(age_pattern, text)
#     if age_match:
#         data['Age'] = int(age_match.group(1))
    
#     return data

# def save_to_csv(data, output_file):
#     """
#     Save the extracted data to a CSV file.
#     """
#     df = pd.DataFrame([data])
#     df.to_csv(output_file, index=False)

# def main(image_path, output_file):
#     """
#     Main function to process the image and extract data.
#     """
#     try:
#         # Preprocess the image
#         processed_image = preprocess_image(image_path)
        
#         # Extract text
#         text = extract_text(processed_image)
#         print("Extracted Text:\n", text)
        
#         # Extract data
#         data = extract_data(text)
#         print("Extracted Data:", data)
        
#         # Save data to CSV
#         save_to_csv(data, output_file)
#         print(f"Data extracted and saved to {output_file}")
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     # Set up command-line argument parsing
#     parser = argparse.ArgumentParser(description="Extract data from ID images.")
#     parser.add_argument("--image_path", required=True, help="Path to the input image.")
#     parser.add_argument("--output_file", required=True, help="Path to the output CSV file.")
#     args = parser.parse_args()
    
#     # Run the main function
#     main(args.image_path, args.output_file)

import pytesseract
import cv2

# Set Tesseract path explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Load an image
image = cv2.imread('image1.jpeg')

# Extract text
text = pytesseract.image_to_string(image)
print("Extracted Text:\n", text)