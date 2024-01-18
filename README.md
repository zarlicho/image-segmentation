Program ini menggunakan MediaPipe library untuk melakukan segmentasi selfie dengan tujuan memisahkan latar depan (orang) dari latar belakang dalam gambar atau video. Hal ini memungkinkan pengguna untuk memilih warna latar belakang secara interaktif.

Here's a breakdown of the main components and functionalities:

1. **Import Libraries:**
   - `cv2`: Perpustakaan OpenCV untuk tugas pengolahan citra.
   - `mediapipe`: Sebuah perpustakaan untuk membangun aplikasi berbasis solusi pembelajaran mesin.

```python
import cv2
import mediapipe as mp
import numpy as np
import time
```

2. **Initialize MediaPipe Components:**
   - `mp_drawing`: MediaPipe drawing utilities.
   - `mp_selfie_segmentation`: MediaPipe selfie segmentation solution.

```python
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
```

3. **Configuration:**
   - Set file gambar yang ingin digunakan (`image_path`) atau bisa juga dengan webcam (`use_webcam`).
   - Set warna default untuk backgroundnya

```python
image_path = "image/person2.jpeg"
use_webcam = False  # Set to True to use a webcam
bg_color = (0, 64, 128)  # Default background color
color_selected = False
selected_color = bg_color
```

4. **Color Exploration:**
   - Define functions and variables for capturing and exploring colors.

```python
# Functions and variables for color exploration
# (on_mouse_click, getColor, color_explore, color_selected)
```

5. **Mouse Click Event Handling:**
   - simpan warna yang di di click oleh cursor lalu otomatis tersimpan di (`color.txt`).
   - klik kanan untuk merubah backgorund sesuai dengan yang di tunjur oleh cursor.

```python
cv2.setMouseCallback('MediaPipe Selfie Segmentation', on_mouse_click)
```

6. **Initialize MediaPipe Selfie Segmentation Model:**
   - Start the selfie segmentation model.

```python
with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:
```

7. **Main Loop:**
   - Continuously process frames from the webcam or image.
   - Extract the segmentation mask and apply it to the frame.
   - Read the selected color from the `color.txt` file and use it as the custom background.
   - Display the output with information on the selected color and frames per second (FPS).

```python
while True:
    # Main processing loop
    # ...
```

8. **Key Handling:**
   - Press 'Esc' to exit the application.

```python
key = cv2.waitKey(1) & 0xFF
if key == 27:  # Press Esc to exit
    break
```

9. **Cleanup:**
   - Destroy all OpenCV windows when the application is terminated.

```python
cv2.destroyAllWindows()
```

Note: Program ini menggunakan segmentasi selfie, memungkinkan pengguna memilih warna latar belakang dengan mengkliknya. Warna yang dipilih ditampilkan dan disimpan ke dalam file, dan latar belakang orang yang tersegmentasi digantikan dengan warna yang dipilih secara real-time. Informasi FPS dan warna yang dipilih juga ditampilkan pada jendela output.
