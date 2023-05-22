# Dog Breed Classifier Capstone Project

## Project Overview

Welcome to my Dog Breed Classifier using Convolutional Neural Networks (CNN) capstone project in the Data Scientist Nanodegree! In this project, I have built a pipeline that is used in a web app to process real-world, user-supplied images. The web app can identify the breed of a dog given an image of a dog and also identify the resembling dog breed when supplied with an image of a human.

## Problem Statement

For my project, I needed to write an algorithm that accepts a file path to an image and performs the following tasks:

1. Determine whether the image contains a human, dog, or neither.
2. If a dog is detected in the image, return the predicted breed.
3. If a human is detected in the image, return the resembling dog breed.
4. If neither a dog nor a human is detected in the image, provide an output that indicates an error.

## Strategy for Solving the Problem

To solve this problem, I followed the following steps:

1. Built Humans and Dog detectors from the image.
2. Created a CNN to Classify Dog Breeds from scratch.
3. Used a CNN to Classify Dog Breeds using Transfer Learning with ResNet-50.
4. Created a CNN to Classify Dog Breeds using Transfer Learning with a selected pre-trained model.
5. Chose the best CNN model for classification based on test accuracy.
6. Developed an algorithm to detect the dog breed or resembling dog breed or return an error.
7. Tested the algorithm.

## Analysis

### Data Exploration

#### Dog Images

- Total dog categories: 133
- Total dog images: 8,351
- Training dog images: 6,680
- Validation dog images: 835
- Test dog images: 836

#### Human Images

- Total human images: 13,233

### Human Detector Performance

I used OpenCV's implementation of Haar feature-based cascade classifiers to detect human faces in images. The performance is as follows:

- 100.0% of the first 100 images in human_files have a detected human face.
- 11.0% of the first 100 images in dog_files have a detected human face.

### Dog Detector Performance

I used a pre-trained ResNet-50 model to detect dogs in images. The performance is as follows:

- 0.0% of the images in human_files_short have a detected dog.
- 100.0% of the images in dog_files_short have a detected dog.

### Model Performance

- CNN from scratch: Test accuracy of 14%.
- CNN to Classify Dog Breeds using ResNet-50 (using transfer learning): Test accuracy of 81%.
