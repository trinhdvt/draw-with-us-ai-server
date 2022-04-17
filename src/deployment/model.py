import torch.nn as nn
import torchvision


class DrawClassifier(nn.Module):
    def __init__(self, num_classes: int):
        super().__init__()

        self.net = torchvision.models.mobilenet_v2(pretrained=True)
        self.net.classifier = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(1280, num_classes)
        )

    def forward(self, x):
        return self.net(x)
