import tensorflow as tf



print("You are using TensorFlow version", tf.__version__)
if len(tf.config.list_physical_devices('GPU')) > 0:
    print("You have a GPU enabled.")
else:
    print("Enable a GPU before running this notebook.")
