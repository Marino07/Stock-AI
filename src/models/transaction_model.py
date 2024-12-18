import torch
import torch.nn as nn
import numpy as np

class TransactionPredictor(nn.Module):
    def __init__(self, input_size=5):
        super(TransactionPredictor, self).__init__()
        # Device configuration
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Layers
        self.layer1 = nn.Linear(input_size, 32)
        self.layer2 = nn.Linear(32, 16)
        self.layer3 = nn.Linear(16, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        
        # Initialize weights
        self._init_weights()
        
        # Move model to device
        self.to(self.device)
        
    def _init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_normal_(m.weight)
                nn.init.constant_(m.bias, 0)
    
    def forward(self, x):
        x = x.to(self.device)
        # Normalize input
        x = (x - x.mean()) / (x.std() + 1e-8)
        
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.sigmoid(self.layer3(x))
        # Scale output to reasonable price range (0-1000)
        return x * 1000
