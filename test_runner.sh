#!/bin/bash
echo "Running Python tests..."
python -m pytest tests/test_transaction_monitor.py -v

echo -e "\nRunning TypeScript tests..."
npm test
