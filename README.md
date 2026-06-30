# Lunar Ice Detection & Mission Planning

## Overview

This project aims to assist future lunar exploration by identifying potential water ice deposits in the Moon's south polar region using Chandrayaan-2 data.

Instead of relying on a single dataset, the system combines terrain analysis, radar observations, infrared data, and artificial intelligence to estimate where subsurface ice is most likely to exist. It also helps plan safe rover routes for future exploration missions.

## The Problem

Water ice is expected to exist inside Permanently Shadowed Regions (PSRs), where sunlight never reaches the surface. These regions are extremely cold, making them ideal locations for preserving ice. However, locating these areas accurately and confirming the presence of ice remains a major challenge.

## Our Approach

The system follows a multi-stage pipeline:

1. Analyze high-resolution Digital Terrain Models (DTMs) from Chandrayaan-2.
2. Detect craters, slopes, and terrain depressions.
3. Simulate sunlight using terrain geometry to identify Permanently Shadowed Regions (PSRs).
4. Combine radar (DFSAR) and infrared (IIRS) observations to estimate ice probability.
5. Train a Reinforcement Learning agent to generate safe and efficient rover paths.
6. Produce an interactive 3D visualization with ice probability maps and mission planning tools.

## Features

- Digital Terrain Model (DTM) analysis
- Crater detection
- Terrain slope and curvature analysis
- Solar illumination simulation
- Permanently Shadowed Region (PSR) detection
- DFSAR radar integration
- IIRS spectral analysis
- Ice probability mapping
- Reinforcement Learning based rover path planning
- Interactive 3D lunar visualization

## Technology Stack

### Frontend
- React
- Three.js
- TypeScript
- Tailwind CSS

### Backend
- Python
- FastAPI
- Node.js

### Data Processing
- Rasterio
- GDAL
- NumPy
- SciPy
- OpenCV
- GeoPandas

### AI & Machine Learning
- PyTorch
- Stable-Baselines3
- Scikit-learn

## Workflow

```text
Chandrayaan-2 Data
        │
        ▼
Terrain Analysis
        │
        ▼
Crater Detection
        │
        ▼
Shadow Simulation
        │
        ▼
PSR Detection
        │
        ▼
Radar + Infrared Data Fusion
        │
        ▼
Ice Probability Mapping
        │
        ▼
Reinforcement Learning
        │
        ▼
Safe Rover Path Planning
```

## Expected Outcome

The final system will provide:

- Potential ice-rich locations
- Permanently Shadowed Region maps
- Safe landing and exploration zones
- Optimized rover traversal paths
- Interactive 3D visualization for mission planning

## Vision

Our goal is to build a reusable lunar exploration platform rather than a solution for a single challenge. The same framework can support future scientific studies, landing site evaluation, rover navigation, and resource exploration for upcoming lunar missions.
