import tensorflow as tf
import sys

init_model = tf.keras.models.load_model("model.h5")
print("converting to .keras")
init_model.save('modelK.keras')
sys.exit(1)