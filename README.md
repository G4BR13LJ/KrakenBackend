# Bitcoin Trading Web App

A web application for visualizing Bitcoin trading data using a Django backend and a React frontend. This application retrieves OHLC (Open, High, Low, Close) data from the Kraken API and displays it using lightweight charts.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Retrieve real-time OHLC data from the Kraken API
- Display data in interactive candlestick charts using Lightweight Charts
- Simple user interface with functionalities to buy/sell Bitcoin
- Responsive design with Tailwind CSS

## Technologies

- **Frontend:** React, Tailwind CSS, Lightweight Charts
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default)
- **API:** Kraken API

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- [Node.js](https://nodejs.org/) (v14 or higher)
- [Python](https://www.python.org/downloads/) (v3.12.6 recommended)
- [pip](https://pip.pypa.io/en/stable/) (comes with Python)
- [npm](https://www.npmjs.com/) (comes with Node.js)

### Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/bitcoin-trading-web-app.git
   cd bitcoin-trading-web-app

2. cd backend  # Navigate to the Django backend folder
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment (use `venv\Scripts\activate` on Windows)
pip install -r requirements.txt  # Install required Python packages
3. python manage.py migrate
4. python manage.py runserver
5. cd frontend  # Navigate to the React frontend folder
npm install  # Install required JavaScript packages
npm start  # Start the React development server
6. Open your browser and go to http://localhost:3000 for the React app and http://localhost:8000 for the Django backend.
