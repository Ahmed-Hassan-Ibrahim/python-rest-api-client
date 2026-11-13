
# Python REST API Client

A Python application that retrieves current weather
information using the WeatherAPI REST API.

## Features

- Sends HTTP GET requests using Requests.
- Parses JSON API responses.
- Uses a Python dataclass to store weather information.
- Loads API credentials from a .env file.
- Handles HTTP and connection errors.

## Requirements

- Python 3.10+
- WeatherAPI API key

## Installation

Clone the repository:

    git clone https://github.com/YOUR_USERNAME/python-rest-api-client.git

Navigate to the project directory:

    cd python-rest-api-client

Create a virtual environment:

    python -m venv venv

Activate it on Windows:

    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

## Configuration

Create a .env file in the project root:

    WEATHER_API_KEY=your_api_key_here

Replace the placeholder with your actual API key.

## Execution

Run:

    python main.py

Enter the desired city when prompted.

## Security

Never commit your .env file or expose your API key.
