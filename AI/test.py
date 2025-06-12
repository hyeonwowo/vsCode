# 예: PyTorch를 이용한 이미지 분류기 (고양이 vs 강아지)

import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

# 1. 데이터 전처리
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])
dataset = ImageFolder("data/", transform=transform)
loader = DataLoader(dataset, batch_size=32)

# 2. 모델 정의
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, 3), nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.fc = nn.Linear(16 * 31 * 31, 2)

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

model = CNN()

# 3. 학습
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    for img, label in loader:
        output = model(img)
        loss = criterion(output, label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
