# Face Recognition File Organizer

A Python-based face recognition system designed to automatically organize image files by identifying and sorting photos containing specific individuals. This project includes two distinct approaches for face recognition and file management.

## Project Overview

This project provides automated image organization capabilities using facial recognition technology. It processes folders containing multiple images, identifies faces matching a reference image, and moves matching files to designated output folders. The system is particularly useful for sorting large photo collections, organizing family photos, or managing image databases.

## Features

- Automatic face detection and recognition
- Image resizing for optimal processing performance
- Interactive decision-making for ambiguous cases
- Batch processing of multiple images
- Flexible tolerance settings for recognition accuracy
- Professional file organization with automatic folder creation

## Requirements

```
opencv-python
face-recognition
numpy
```

## Installation

1. Clone this repository or download the Python files
2. Install required dependencies:
```bash
pip install opencv-python face-recognition numpy
```

---

## single_facerec.py

### Description

The single face recognition script provides a streamlined approach to face recognition with simplified processing. This version assumes each image contains only one face and uses exception handling to manage cases where face detection fails.


### How It Works

1. **Initialization**: Prompts user for input folder name and destination folder name
2. **Reference Setup**: Uses the first image in the folder as the known reference face
3. **Processing Loop**: Iterates through all images in the input folder
4. **Face Detection**: Attempts to extract face encoding from each image
5. **Comparison**: Compares unknown faces against the reference using specified tolerance
6. **Decision Making**: Automatically moves matching images or prompts user for manual decision
7. **Reporting**: Provides summary of total files processed and moved

### Usage

```bash
python single_facerec.py
```


### Technical Implementation

- Uses `face_recognition.face_encodings()[0]` to extract single face encoding
- Implements try-except block for robust error handling
- Applies 0.6 tolerance threshold for face matching
- Includes automatic image resizing to 1024px maximum dimension
- Provides real-time feedback during processing


### Screenshot Placeholder

Existing Folder
> <img src="https://github.com/user-attachments/assets/1766f4b2-10bf-47ca-b5bc-cf1a9c86a284" width="600" alt="Screenshot description">


Execution
> <img src="https://github.com/user-attachments/assets/5007d5c7-f262-42f4-9fe3-69bb6b2ace28" width="600" alt="Screenshot description">


New Folder
> <img src="https://github.com/user-attachments/assets/21fc3c6e-cd79-4bc1-8f0c-6c8fa2cd4c94" width="600" alt="Screenshot description">


Old Folder
> <img src="https://github.com/user-attachments/assets/de824ed1-d39a-4e93-ac92-a502df932d36" width="600" alt="Screenshot description">


---

## multiple_facerec.py

### Description

The multiple face recognition script offers advanced processing capabilities for images containing multiple faces. This version can detect and process several faces within a single image, making it ideal for group photos and complex image collections.


### How It Works

1. **Setup Phase**: Collects user input for source and destination folders
2. **Reference Establishment**: Designates first image as the reference standard
3. **Multi-Face Detection**: Identifies all face locations within each image
4. **Batch Processing**: Processes multiple face encodings simultaneously
5. **Matching Algorithm**: Compares each detected face against reference
6. **Smart Decision Making**: Moves images with any matching faces
7. **Manual Override**: Provides interactive decision for images without faces

### Usage

```bash
python multiple_facerec.py
```

Follow the prompts to specify:
- Input folder containing source images
- Output folder for organizing matched results

### Technical Implementation

- Utilizes `face_recognition.face_locations()` for comprehensive face detection
- Processes multiple encodings using `face_recognition.face_encodings(image, locations)`
- Implements nested loop structure for multi-face comparison
- Features break statement for efficiency once match is found
- Includes interactive image display for user verification
- Provides detailed console logging for transparency

### Advanced Features

- **Multi-Face Support**: Can process images containing multiple people
- **Location Mapping**: Precisely identifies face positions within images
- **Batch Encoding**: Efficiently processes multiple faces simultaneously
- **Smart Matching**: Stops processing once a match is confirmed
- **Interactive Fallback**: Manual verification for edge cases


### Screenshot Placeholder

Existing Folder
> <img src="https://github.com/user-attachments/assets/714ffe47-e8a0-42a3-965a-902a283cce4f" width="600" alt="Screenshot description">


Execution
> <img src="https://github.com/user-attachments/assets/28841792-8833-4c63-84d6-ec7b842b60ba" width="600" alt="Screenshot description">


New Folder
> <img src="https://github.com/user-attachments/assets/3a27097f-505d-4794-9f4c-6e6deeb0278c" width="600" alt="Screenshot description">


Old Folder
> <img src="https://github.com/user-attachments/assets/ae6c49ee-8b1e-44cc-b05f-303a2628e75b" width="600" alt="Screenshot description">

---

## Common Functions

### resize_image()

Both scripts include an image resizing function that optimizes processing performance:

```python
def resize_image(image, max_size=1024):
    h, w = image.shape[:2]
    if max(h, w) > max_size:
        scale = max_size / max(h, w)
        new_size = (int(w * scale), int(h * scale))
        return cv.resize(image, new_size)
    return image
```

This function ensures efficient processing by limiting image dimensions while maintaining aspect ratio.

## Usage Guidelines

### Choosing the Right Script

- **Use single_facerec.py when:**
  - Processing individual portraits or headshots
  - Working with simple image collections
  - Prioritizing processing speed
  - Dealing with images containing primarily single subjects

- **Use multiple_facerec.py when:**
  - Processing group photos or family pictures
  - Working with complex image collections
  - Need comprehensive face detection
  - Handling images with multiple people

### Best Practices

1. Ensure the reference image (first in folder) clearly shows the target person
2. Use high-quality images for better recognition accuracy
3. Organize input folders before processing
4. Backup original images before running the scripts
5. Test with small batches before processing large collections


## Common Issues

- **No faces detected**: Ensure images contain clear, frontal faces
- **False positives**: Adjust tolerance settings or use higher quality reference images
- **Performance issues**: Verify image sizes are reasonable (script auto-resizes to 1024px)
- **File permission errors**: Ensure write permissions for destination folders

## Technical Specifications

- **Face Recognition Library**: Uses dlib-based face recognition
- **Image Processing**: OpenCV for computer vision operations
- **File Management**: Python os and shutil modules
- **Image Formats**: Supports standard formats (JPG, PNG, etc.)
- **Performance**: Optimized with automatic image resizing


## License

This project is provided for educational and personal use. Ensure compliance with local privacy laws when processing facial recognition data.
