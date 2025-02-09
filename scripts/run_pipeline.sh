#!/bin/bash

echo "Running training pipeline..."
python3 src/model.py

echo "Starting Flask app..."
python3 src/app.py