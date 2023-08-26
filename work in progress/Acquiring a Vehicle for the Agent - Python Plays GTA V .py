# coding: utf-8
# # Object Detection Demo
# License: Apache License 2.0 (https://github.com/tensorflow/models/blob/master/LICENSE)
# source: https://github.com/tensorflow/models
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from grabscreen import grab_screen
import cv2
import keys as k
import time

keys = k.Keys({})

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# ## Object detection imports
# Here are the imports from the object detection module.

from utils import label_map_util
from utils import visualization_utils as vis_util

# # Model preparation
# What model to download.
MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90

# ## Download Model
opener = urllib.request.URLopener()
opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
tar_file = tarfile.open(MODEL_FILE)
for file in tar_file.getmembers():
    file_name = os.path.basename(file.name)
    if 'frozen_inference_graph.pb' in file_name:
        tar_file.extract(file, os.getcwd())

# ## Load a (frozen) Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

# ## Loading label map
# Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)


# ## Helper code
def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)


def determine_movement(mid_x, mid_y, width=1280, height=705):
    x_move = 0.5 - mid_x
    y_move = 0.5 - mid_y
    hm_x = x_move / 0.5
    hm_y = y_move / 0.5
    keys.keys_worker.SendInput(keys.keys_worker.Mouse(0x0001, -1 * int(hm_x * width), -1 * int(hm_y * height)))


# Size, in inches, of the output images.
IMAGE_SIZE = (12, 8)
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.70)

with detection_graph.as_default():
    with tf.Session(graph=detection_graph, config=tf.ConfigProto(gpu_options=gpu_options)) as sess:
        stolen = False
        while True:
            # screen = cv2.resize(grab_screen(region=(0,40,1280,745)), (WIDTH,HEIGHT))
            screen = cv2.resize(grab_screen(region=(0, 40, 1280, 745)), (800, 450))
            image_np = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            # Actual detection.
            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8)

            vehicle_dict = {}

            for i, b in enumerate(boxes[0]):
                #                 car                    bus                  truck
                if classes[0][i] == 3 or classes[0][i] == 6 or classes[0][i] == 8:
                    if scores[0][i] >= 0.5:
                        mid_x = (boxes[0][i][1] + boxes[0][i][3]) / 2
                        mid_y = (boxes[0][i][0] + boxes[0][i][2]) / 2
                        apx_distance = round(((1 - (boxes[0][i][3] - boxes[0][i][1])) ** 4), 3)
                        cv2.putText(image_np, '{}'.format(apx_distance), (int(mid_x * 800), int(mid_y * 450)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                        '''
                        if apx_distance <=0.5:
                          if mid_x > 0.3 and mid_x < 0.7:
                            cv2.putText(image_np, 'WARNING!!!', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 3)
                        '''

                        vehicle_dict[apx_distance] = [mid_x, mid_y, scores[0][i]]

            if len(vehicle_dict) > 0:
                closest = sorted(vehicle_dict.keys())[0]
                vehicle_choice = vehicle_dict[closest]
                print('CHOICE:', vehicle_choice)
                if not stolen:
                    determine_movement(mid_x=vehicle_choice[0], mid_y=vehicle_choice[1], width=1280, height=705)
                    if closest < 0.1:
                        keys.directKey("w", keys.key_release)
                        keys.directKey("f")
                        time.sleep(0.05)
                        keys.directKey("f", keys.key_release)
                        stolen = True
                    else:
                        keys.directKey("w")

            cv2.imshow('window', image_np)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break