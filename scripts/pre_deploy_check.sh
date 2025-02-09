#!/bin/bash

# Check app size
APP_SIZE=$(du -sh . | cut -f1)
echo "App size: $APP_SIZE"

# Check if Docker image exists
if docker images | grep -q "student_performance_app"; then
    echo "Docker image exists."
else
    echo "Docker image does not exist. Build it using 'docker build -t student_performance_app .'"
fi