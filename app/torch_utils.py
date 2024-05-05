import io
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

# Hyper-parameters 
input_size = 784 # 28x28
hidden_size = 500 
num_classes = 10

# Fully connected neural network with one hidden layer
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.input_size = input_size
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size, num_classes)  
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        # no activation and no softmax at the end
        return out

model = NeuralNet(input_size, hidden_size, num_classes)
PATH = "app/mymodule.pt"
model.load_state_dict(torch.load(PATH))
model.eval()


#image to tensor
def transform_image(filename):
    transform = transforms.Compose([transforms.Grayscale(num_output_channels=1),
                                    transforms.Resize((28,28)),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.1307,),(0.3081,))])
    print("*"*50)
    image = Image.open(filename)
    return transform(image).unsqueeze(0)

# predict
def get_prediction(image_tensor):
    images = image_tensor.reshape(-1,28*28)
    outputs = model(images)
    _,predicted = torch.max(outputs.data,1)
    return predicted