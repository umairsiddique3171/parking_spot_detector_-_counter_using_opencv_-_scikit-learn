import pickle
import numpy as np
import cv2


EMPTY = True
NOT_EMPTY = False

model_path = r"C:\Users\US593\OneDrive\Desktop\parking_spot_detector_&_counter\parking_spot_empty_or_non-empty_classifier\random_forest_model.p"
model = pickle.load(open(model_path, "rb"))

def predict(img,model):
    img_resized = cv2.resize(img, (40, 20))
    img_gray = cv2.cvtColor(img_resized,cv2.COLOR_BGR2GRAY)
    flattened_imgs = np.reshape(img_gray, (1,800))
    flat_data = np.array(flattened_imgs)
    y_output = model.predict(flat_data)
    return y_output[0]


def empty_or_not(spot_bgr):

    y_output = predict(spot_bgr,model)
    if y_output == 0:
        return EMPTY
    else:
        return NOT_EMPTY


def get_parking_spots_bboxes(connected_components):

    (totalLabels, label_ids, values, centroid) = connected_components
    slots = []
    coef = 1
    for i in range(1, totalLabels):
        # Now extract the coordinate points
        x1 = int(values[i, cv2.CC_STAT_LEFT] * coef)
        y1 = int(values[i, cv2.CC_STAT_TOP] * coef)
        w = int(values[i, cv2.CC_STAT_WIDTH] * coef)
        h = int(values[i, cv2.CC_STAT_HEIGHT] * coef)
        slots.append([x1, y1, w, h])
    return slots

def calc_diff(im1, im2):
    return np.abs(np.mean(im1) - np.mean(im2))

