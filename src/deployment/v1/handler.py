from ts.torch_handler.image_classifier import ImageClassifier
from torchvision import transforms as T


class DrawClassifier(ImageClassifier):
    IN_SIZE = (128, 128)
    topk = 3
    image_processing = T.Compose([
        T.Resize(IN_SIZE),
        T.Grayscale(num_output_channels=3),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
