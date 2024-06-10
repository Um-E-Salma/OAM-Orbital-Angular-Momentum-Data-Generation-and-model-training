
# OAM Dataset and Model Training

## Overview

This repository contains code for creating an Orbital Angular Momentum (OAM) dataset with a noise level of 0.1. Additionally, it includes model training using various deep learning architectures such as DenseNet, AlexNet, MobileNet, ResNet, ResNeXt, WideResNet, ShuffleNet, and SqueezeNet.

## Dataset Generation

The OAM dataset was created in 10 modes with a noise level of 0.1. Each dataset entry consists of images with distinct modes, providing a diverse set of 1000 image samples.
## Model Training

The following deep learning models were trained an evaluate on the accuracy and loss on the OAM dataset:

* DenseNet
* AlexNet
* MobileNet
* ResNet
* ResNeXt
* WideResNet
* ShuffleNet
* SqueezeNet
## Model Comparison

TensorFlow models, including DenseNet, ResNet, ResNeXt, WideResNet, and AlexNet, were evaluated based on their accuracy, F1 score, precision, and recall. A comprehensive comparison was conducted to determine the performance of each model.
## Model Chaining

The trained models were utilized in a model chaining approach to enhance overall prediction performance. This strategy leverages the strengths of individual models to achieve improved results in classification tasks. As work progresses, I will update this section to reflect any improvements in accuracy resulting from the model chaining technique.