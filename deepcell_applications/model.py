import os
import tensorflow as tf
from deepcell.applications import Mesmer


def loading_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model
