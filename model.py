# -*- coding: utf-8 -*-


from modelsummary import summary
import torch.nn.functional as F
import torch.nn as nn
import torch

'''
Model Details:

Two Convolutional Layers:
      - Using ReLU activation
      - Batch Normalisation
      - Uniform Xavier Weigths
      - Max Pooling

One Fully Connected Layer:
      - Using ReLU activation

One Fully Connected Layer:
      - Output Layer

'''


class CNN(nn.Module):
	def __init__(self):
		super(CNN, self).__init__()

		self.cnn1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=5, stride=1, padding=2)
		self.relu1 = nn.ReLU()
		self.norm1 = nn.BatchNorm2d(32)
		nn.init.xavier_uniform_(self.cnn1.weight)

		self.maxpool1 = nn.MaxPool2d(kernel_size=2)

		self.cnn2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=2)
		self.relu2 = nn.ReLU()
		self.norm2 = nn.BatchNorm2d(64)
		nn.init.xavier_uniform_(self.cnn2.weight)

		self.maxpool2 = nn.MaxPool2d(kernel_size=2)

		self.fc1 = nn.Linear(4096, 4096)
		self.fcrelu = nn.ReLU()

		self.fc2 = nn.Linear(4096, 10)

	def forward(self, x):
		out = self.cnn1(x)
		out = self.relu1(out)
		out = self.norm1(out)

		out = self.maxpool1(out)

		out = self.cnn2(out)
		out = self.relu2(out)
		out = self.norm2(out)

		out = self.maxpool2(out)

		out = out.view(out.size(0), -1)

		out = self.fc1(out)
		out = self.fcrelu(out)

		logits = self.fc2(out)
		probas = F.softmax(logits, dim=1)
		return logits, probas

# if __name__ == '__main__':
#
# 	# Device
# 	device = torch.device("cuda:3" if torch.cuda.is_available() else "cpu")
# 	model = CNN()
# 	model.to(device)
# 	summary(model, torch.ones(128, 1, 28, 28), batch_size=128, show_input=False)