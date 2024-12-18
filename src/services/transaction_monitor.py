import torch
import numpy as np
from ..models.transaction_model import TransactionPredictor

class TransactionMonitor:
    def __init__(self):
        self.transactions = []
        self.model = TransactionPredictor()
        self.price_history = []
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        
    def prepare_data(self, transaction):
        try:
            # Track price history for better normalization
            self.price_history.append(transaction['price'])
            mean_price = np.mean(self.price_history)
            std_price = np.std(self.price_history) or 1.0
            
            return torch.tensor([
                (float(transaction['price']) - mean_price) / std_price,
                float(transaction['quantity']) / 100,
                1.0 if transaction['type'] == 'buy' else 0.0,
                float(transaction['amount']) / 10000,
                float(transaction['date'].timestamp()) % 86400 / 86400
            ], dtype=torch.float32)
        except Exception as e:
            print(f"Error preparing data: {e}")
            return None
        
    def analyze_transactions(self):
        if not self.transactions:
            return {"totalBuy": 0, "totalSell": 0, "profit": 0}
            
        total_buy = sum(t['price'] * t['quantity'] 
                       for t in self.transactions if t['type'] == 'buy')
        total_sell = sum(t['price'] * t['quantity'] 
                        for t in self.transactions if t['type'] == 'sell')
                        
        # PyTorch prediction for next price
        latest_transaction = self.transactions[-1]
        input_tensor = self.prepare_data(latest_transaction)
        if input_tensor is None:
            return {"totalBuy": total_buy, "totalSell": total_sell, "profit": total_sell - total_buy, "predictedNextPrice": None}
        with torch.no_grad():
            prediction = self.model(input_tensor)
            
        return {
            "totalBuy": total_buy,
            "totalSell": total_sell,
            "profit": total_sell - total_buy,
            "predictedNextPrice": prediction.item()
        }
