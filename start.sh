#!/bin/bash

# AI Movie Studio - Quick Start Guide

echo "🎬 AI Movie Studio - Tamil Edition - Quick Start"
echo "=================================================="
echo ""

# Step 1: Install dependencies
echo "Step 1: Installing Python dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Step 2: Copy environment file
echo "Step 2: Setting up environment..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file (edit it with your settings)"
else
    echo "✓ .env file already exists"
fi
echo ""

# Step 3: Create necessary directories
echo "Step 3: Creating directories..."
mkdir -p videos
mkdir -p scripts
mkdir -p generated_movies
mkdir -p .temp
echo "✓ Directories created"
echo ""

# Step 4: Start the Flask app
echo "Step 4: Starting AI Movie Studio server..."
echo "📍 Server will run on http://localhost:5000"
echo ""
python app.py
