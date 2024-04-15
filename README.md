# Digit Classification Model Using Deep Learning

This repository contains code for training and evaluating a deep learning model to classify handwritten digits using the MNIST dataset.

## Overview

The goal of this project is to build a convolutional neural network (CNN) that can accurately classify images of handwritten digits (0-9) from the MNIST dataset. The model will be implemented using Python and TensorFlow/Keras.

also created simple GUI interface using tkinter,ttkbootstrap and opencv for image handiling which lets you pic an image containing number and the model predicts the number

<br>this is a simple example aim to show the realworld use case of an artificial neural network(ANN)</br>

## Dataset

We are using the MNIST dataset, which is a widely used dataset for handwritten digit classification. It consists of 60,000 training images and 10,000 test images, each of size 28x28 pixels.

## Model Architecture

The CNN architecture used for this task is as follows:

- Input layer (28x28 pixels)
- ReLU activation
- Dense (fully connected) layer with 10 units
- ReLU activation
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
pip install tensorflow numpy matplotlib opencv-python ttkbootstrap
```
