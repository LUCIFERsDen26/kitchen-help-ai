# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.


import torch
import torch.nn as nn
import random
import numpy as np

from torchvision.models import resnet50, resnet101, resnet152
from torchvision.models import ResNet50_Weights, ResNet101_Weights, ResNet152_Weights

class EncoderCNN(nn.Module):
    def __init__(self, embed_size, dropout=0.5, image_model='resnet101', pretrained=True):
        """Load the pretrained ResNet and replace top fc layer."""
        super(EncoderCNN, self).__init__()

        # Dynamically map the model name to weights
        weights_map = {
            'resnet50': ResNet50_Weights.DEFAULT,
            'resnet101': ResNet101_Weights.DEFAULT,
            'resnet152': ResNet152_Weights.DEFAULT,
        }

        # Get the appropriate weights
        weights = weights_map[image_model] if pretrained else None

        # Dynamically get the ResNet model
        model_map = {
            'resnet50': resnet50,
            'resnet101': resnet101,
            'resnet152': resnet152,
        }
        resnet = model_map[image_model](weights=weights)  # Updated argument
        
        # Keep all layers except the last two
        modules = list(resnet.children())[:-2]  # delete the last fc layer
        self.resnet = nn.Sequential(*modules)

        # Replace the last FC layer
        self.linear = nn.Sequential(
            nn.Conv2d(resnet.fc.in_features, embed_size, kernel_size=1, padding=0),
            nn.Dropout2d(dropout)
        )


    def forward(self, images, keep_cnn_gradients=False):
        """Extract feature vectors from input images."""

        if keep_cnn_gradients:
            raw_conv_feats = self.resnet(images)
        else:
            with torch.no_grad():
                raw_conv_feats = self.resnet(images)
        features = self.linear(raw_conv_feats)
        features = features.view(features.size(0), features.size(1), -1)

        return features


class EncoderLabels(nn.Module):
    def __init__(self, embed_size, num_classes, dropout=0.5, embed_weights=None, scale_grad=False):

        super(EncoderLabels, self).__init__()
        embeddinglayer = nn.Embedding(num_classes, embed_size, padding_idx=num_classes-1, scale_grad_by_freq=scale_grad)
        if embed_weights is not None:
            embeddinglayer.weight.data.copy_(embed_weights)
        self.pad_value = num_classes - 1
        self.linear = embeddinglayer
        self.dropout = dropout
        self.embed_size = embed_size

    def forward(self, x, onehot_flag=False):

        if onehot_flag:
            embeddings = torch.matmul(x, self.linear.weight)
        else:
            embeddings = self.linear(x)

        embeddings = nn.functional.dropout(embeddings, p=self.dropout, training=self.training)
        embeddings = embeddings.permute(0, 2, 1).contiguous()

        return embeddings
