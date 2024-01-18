# MediaPipe Selfie Segmentation with Custom Background Color

This program utilizes the MediaPipe library for selfie segmentation to separate the foreground (person) from the background in an image or video stream. Additionally, it allows the user to interactively choose a custom background color. The selected color replaces the background in real-time.

## Prerequisites

Make sure you have the necessary libraries installed:

- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)

```bash
pip install opencv-python mediapipe numpy
```

## Usage

1. Set the path for the input image (`image_path`) or enable the webcam (`use_webcam`).
2. Define the default background color (`bg_color`).
3. Run the script.

```bash
python selfie_segmentation.py
```

### User Interaction

- **Left-click**: Capture the color at the clicked point and save it to a file (`color.txt`).
- **Right-click**: Print the selected color in hexadecimal format.

### Exiting the Program

Press 'Esc' to exit the application.

## Color Exploration

The program allows users to interactively explore and select a custom background color. The selected color is displayed on the output window and saved to a file for later use.

## Credits

- This program uses the [MediaPipe](https://mediapipe.dev/) library for selfie segmentation.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize and use this program for your projects!
