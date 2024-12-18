import pytest
from datetime import datetime
from src.services.transaction_monitor import TransactionMonitor  # Ispravljeni import

def test_basic_transaction_analysis():
    monitor = TransactionMonitor()
    
    # Test empty transactions
    empty_analysis = monitor.analyze_transactions()
    assert empty_analysis['totalBuy'] == 0
    assert empty_analysis['totalSell'] == 0
    assert empty_analysis['profit'] == 0

    # Test single buy transaction
    buy_transaction = {
        'id': '1',
        'amount': 1000,
        'date': datetime.now(),
        'type': 'buy',
        'symbol': 'AAPL',
        'price': 100,
        'quantity': 10
    }
    monitor.add_transaction(buy_transaction)
    
    buy_analysis = monitor.analyze_transactions()
    assert buy_analysis['totalBuy'] == 1000
    assert buy_analysis['totalSell'] == 0
    assert buy_analysis['profit'] == -1000
    assert 'predictedNextPrice' in buy_analysis

def test_model_predictions():
    monitor = TransactionMonitor()
    
    # Add multiple transactions to test prediction
    transactions = [
        {
            'id': '1',
            'amount': 1000,
            'date': datetime.now(),
            'type': 'buy',
            'symbol': 'AAPL',
            'price': 100,
            'quantity': 10
        },
        {
            'id': '2',
            'amount': 1200,
            'date': datetime.now(),
            'type': 'sell',
            'symbol': 'AAPL',
            'price': 120,
            'quantity': 10
        }
    ]
    
    for transaction in transactions:
        monitor.add_transaction(transaction)
    
    analysis = monitor.analyze_transactions()
    
    # Test prediction is within reasonable bounds
    assert isinstance(analysis['predictedNextPrice'], float)
    assert 0 <= analysis['predictedNextPrice'] <= 1000  # Assuming reasonable price range

if __name__ == "__main__":
    test_basic_transaction_analysis()
    test_model_predictions()
    print("All tests passed!")
