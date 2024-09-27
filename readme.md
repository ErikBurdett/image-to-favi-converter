# Image Converter Script

This project is a Python script that resizes and converts images from one format to another. It supports converting images into three formats (`jpg`, `png`, `ico`) and resizing them into three sizes (32x32, 128x128, 512x512). The script processes `.jpg`, `.png`, and `.webp` images and stores the output in a structured directory format.

## Features

- Supports image formats: `.jpg`, `.png`, and `.webp`.
- Converts images to: `jpg`, `png`, and `ico`.
- Resizes images to: `32x32`, `128x128`, and `512x512`.
- Organizes output images into separate directories for each image and size.
- Can be easily customized to add more formats or sizes.

## Prerequisites

- Python 3.x
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository or download the script to your local machine:
    ```bash
    git clone https://github.com/your-username/image-converter.git
    cd image-converter
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

> **Note:** If `requirements.txt` is missing, install `Pillow` manually:
```bash
pip install Pillow
```

## Usage: 

1. Place the images you want to convert in the images directory.

2. Run the script: 

```bash 
python favi.py
```

3. After the script runs, you will find the converted images in the conversion/ directory. Each image will have its own subdirectory, with further subdirectories for each size.

Example directory Structure: 

```bash 
/conversion/
    └── image1/
        ├── 32x32/
        │   ├── image1.jpg
        │   ├── image1.png
        │   └── image1.ico
        ├── 128x128/
        │   ├── image1.jpg
        │   ├── image1.png
        │   └── image1.ico
        └── 512x512/
            ├── image1.jpg
            ├── image1.png
            └── image1.ico
``` 

## Script Config: 
The script converts images in three sizes (32x32, 128x128, 512x512) and three formats (jpg, png, ico). You can modify the script to support more formats or sizes by editing the following sections:

```python 
sizes = [(32, 32), (128, 128), (512, 512)]
```

```python 
formats = ['jpg', 'png', 'ico']
```

## Requirements: 
Python 3.x
Pillow (Python Imaging Library)


Feel free to contact erikaburdet@gmail.com for more information/questions. 