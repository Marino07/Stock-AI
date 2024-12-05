import torch

print("Starting PyTorch test script...")

# Check for CUDA availability
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0, 4.0]).to(device)
print(f"Original tensor: {tensor}")

# Perform a simple operation (e.g., addition)
result = tensor + 10
print(f"Tensor after addition: {result}")

print("PyTorch test script completed.")