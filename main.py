import matplotlib
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nlp

def show_history(h):
    epochs_trained = len(h.history['loss'])


