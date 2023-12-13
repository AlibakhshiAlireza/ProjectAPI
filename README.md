# Clinic Reservation System

## Overview
This Flask application serves as a backend for a clinic reservation system. It allows users to view available appointment slots for different clinics and make reservations by updating the slot count.

## Features
- **View Available Slots**: Users can view the current number of available slots for each clinic.
- **Reserve Slots**: Users can reserve slots, which updates the available slot count in the system.

## Installation

### Prerequisites
- Python 3
- Flask

### Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/AlibakhshiAlireza/ProjectAPI
   cd ProjectAPI

### Usage
- **Viewing Available Slots
- **Endpoint: GET /slots
- **Function: Returns a JSON object with available slots for each clinic.
---
- **Reserving Slots
- **Endpoint: POST /reserve
- **Function: Updates the available slot count for a specified clinic.
- **Data Format: JSON with id (clinic ID) and reserved (number of slots to reserve).
- **Usage Example: Send a POST request to http://127.0.0.1:5000/reserve with a JSON body like {"id": "1", "reserved": 1}
