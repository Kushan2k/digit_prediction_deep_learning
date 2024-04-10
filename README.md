# Digit Classification Model Using Deep Learning

This repository contains code for training and evaluating a deep learning model to classify handwritten digits using the MNIST dataset.

## Overview

The goal of this project is to build a convolutional neural network (CNN) that can accurately classify images of handwritten digits (0-9) from the MNIST dataset. The model will be implemented using Python and TensorFlow/Keras.

## Dataset

We are using the MNIST dataset, which is a widely used dataset for handwritten digit classification. It consists of 60,000 training images and 10,000 test images, each of size 28x28 pixels.

## Model Architecture

The CNN architecture used for this task is as follows:

- Input layer (28x28 pixels)
- Convolutional layer with 32 filters
- ReLU activation
- Max pooling layer
- Convolutional layer with 64 filters
- ReLU activation
- Max pooling layer
- Flatten layer
- Dense (fully connected) layer with 128 units
- ReLU activation
- Dropout layer (for regularization)
- Output layer with 10 units (corresponding to digits 0-9) and softmax activation

## Requirements

To run the code in this repository, you will need:

- Python 3.x
- TensorFlow 2.x
- Keras
- NumPy
- Matplotlib

You can install these dependencies using pip:

```bash
pip install tensorflow numpy matplotlib
```
