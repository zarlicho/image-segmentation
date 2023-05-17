import cv2
import mediapipe as mp
import numpy as np
import time

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

image_path = "image/person2.jpeg"
use_webcam = False # change to True for use webcam!

if use_webcam ==True:
    image=cv2.VideoCapture(0)
else:
    image = cv2.imread(image_path)
# bg_color = (120, 57, 0)  # default background color (gray)
bg_color = (0, 64, 128)
color_selected = False
selected_color = bg_color
print(bg_color)
color_explore = np.zeros((150, 150, 3), np.uint8)
color_selected = np.zeros((150, 150, 3), np.uint8)

def getColor(R, G, B):
    return R, G, B

def on_mouse_click(event, x, y, flags, param):
    global color_selected

    B = 0
    G = 0
    R = 0

    if use_webcam == True:
        ret, frame = image.read()
        if not ret:
            return

        B = frame[y, x][0]
        G = frame[y, x][1]
        R = frame[y, x][2]
    else:
        B = image[y, x][0]
        G = image[y, x][1]
        R = image[y, x][2]

    color_explore[:, :] = (B, G, R)

    if event == cv2.EVENT_LBUTTONDOWN:
        color_selected[:, :] = (B, G, R)
        B = color_selected[10, 10][0]
        G = color_selected[10, 10][1]
        R = color_selected[10, 10][2]
        data = "{R},{G},{B}".format(R=R, G=G, B=B)
        with open("color.txt", "w+") as f:
            f.write(data)

    if event == cv2.EVENT_RBUTTONDOWN:
        B = color_selected[10, 10][0]
        G = color_selected[10, 10][1]
        R = color_selected[10, 10][2]
        print(hex(R), hex(G), hex(B))


cv2.namedWindow('MediaPipe Selfie Segmentation')
cv2.setMouseCallback('MediaPipe Selfie Segmentation', on_mouse_click)

with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:


    while True:
        start = time.time()
        if use_webcam==True:
            ret,frame=image.read()
            # Convert the BGR image to RGB.
            image_bgr = cv2.flip(frame, 1)
            image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

            # To improve performance, optionally mark the image as not writeable to pass by reference.
            image_rgb.flags.writeable = False

            # Pass the image through the model
            results = selfie_segmentation.process(image_rgb)
            # Convert the RGB image to BGR
            image_rgb.flags.writeable = True
            image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

            # Create a mask based on the segmentation results
            mask = (results.segmentation_mask > 0.95).astype(np.uint8)

            # Read color from file
            with open("color.txt", "r") as f:
                data = f.read()
                color_values = data.split(",")
                if len(color_values) == 3:
                    R = int(color_values[0])
                    G = int(color_values[1])
                    B = int(color_values[2])
                    selected_color = getColor(R, G, B)

            # Convert selected_color to the same data type as image_bgr
            selected_color = selected_color[::-1]  # Reverse the order of RGB values
            selected_color = np.array(selected_color, dtype=np.uint8)
            print(selected_color)

            # Apply the mask to the image
            output_image = np.where(mask[..., np.newaxis], image_bgr,selected_color)

            end = time.time()
            totalTime = end - start

            fps = 1 / totalTime
            output_image_copy = output_image.copy()
            with open("color.txt","r") as f:
                print("data color by text file",f.read())

            if np.any(color_selected):
                # print(selected_color)
                cv2.rectangle(output_image_copy, (0, 0), (150, 50), selected_color.tolist(), -1)
                cv2.putText(output_image_copy, 'Selected Color', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            cv2.putText(output_image_copy, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            cv2.imshow('MediaPipe Selfie Segmentation', output_image_copy)

            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # Press Esc to exit
                break

        else:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # To improve performance, optionally mark the image as not writeable to pass by reference.
            image_rgb.flags.writeable = False

            # Pass the image through the model
            results = selfie_segmentation.process(image_rgb)
            # Convert the RGB image to BGR
            image_rgb.flags.writeable = True
            image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

            # Create a mask based on the segmentation results
            mask = (results.segmentation_mask > 0.95).astype(np.uint8)

            # Read color from file
            with open("color.txt", "r") as f:
                data = f.read()
                color_values = data.split(",")
                if len(color_values) == 3:
                    R = int(color_values[0])
                    G = int(color_values[1])
                    B = int(color_values[2])
                    selected_color = getColor(R, G, B)

            # Convert selected_color to the same data type as image_bgr
            selected_color = selected_color[::-1]  # Reverse the order of RGB values
            selected_color = np.array(selected_color, dtype=np.uint8)
            print(selected_color)

            # Apply the mask to the image
            output_image = np.where(mask[..., np.newaxis], image_bgr,selected_color)

            end = time.time()
            totalTime = end - start

            fps = 1 / totalTime
            output_image_copy = output_image.copy()
            with open("color.txt","r") as f:
                print("data color by text file",f.read())

            if np.any(color_selected):
                # print(selected_color)
                cv2.rectangle(output_image_copy, (0, 0), (150, 50), selected_color.tolist(), -1)
                cv2.putText(output_image_copy, 'Selected Color', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            cv2.putText(output_image_copy, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            cv2.imshow('MediaPipe Selfie Segmentation', output_image_copy)

            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # Press Esc to exit
                break

    cv2.destroyAllWindows()
