# UAV Tracking System with Kalman Filter & Obstacle Detection

A real-time UAV tracking and obstacle detection system using a **C8051 microcontroller**, GPS, ultrasonic sensing, and a **Kalman Filter** for improved position estimation.

## Overview

The system is designed to track UAV position using GPS data while reducing measurement noise using a Kalman Filter.

An ultrasonic sensor is used for real-time obstacle detection and proximity monitoring. A Python-based visualization system displays the UAV trajectory and processed position data.

## Key Features

- Real-time GPS-based UAV position tracking
- GPS noise reduction using Kalman Filter
- Ultrasonic-based obstacle detection
- Real-time proximity monitoring
- C8051 microcontroller-based sensor processing
- Python-based UAV trajectory visualization
- Separation of raw and filtered position data

## System Architecture

```text
              ┌──────────────┐
              │     GPS      │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │    C8051     │
              │ Microcontroller│
              └──────┬───────┘
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   ┌──────────────┐      ┌──────────────┐
   │ Kalman Filter│      │  Ultrasonic  │
   │              │      │    Sensor    │
   └──────┬───────┘      └──────┬───────┘
          │                     │
          ▼                     ▼
   Filtered Position      Obstacle Distance
          │                     │
          └──────────┬──────────┘
                     │
                     ▼
              ┌──────────────┐
              │    Python    │
              │ Visualization│
              └──────────────┘
