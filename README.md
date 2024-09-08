# TARS AI Project

## Overview
TARS AI is a project developed by the SHPE Club from LACC-MESA. It provides a Flask API for controlling a robot and a React application for user interaction.

## Project Structure
```
tars-ai/
├── api/                  # Flask API backend
│   ├── core/             # Core functionalities
│   ├── logs/             # Log files
│   ├── requirements.txt  # Python dependencies
│   ├── .flaskenv         # Environment variables for Flask
│   └── main.py           # Main entry point for the API
├── tars-app/             # React frontend
│   ├── src/              # Source files for React
│   ├── public/           # Public assets
│   ├── package.json      # Node.js dependencies
│   └── vite.config.ts    # Vite configuration
└── README.md             # Project documentation
```

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/tars-ai.git
cd tars-ai
```

### 2. Set Up the Backend (API)

#### a. Create a Virtual Environment
```bash
cd api
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### b. Copy the Example Environment File
```bash
cp .example.env .env
```
Edit the `.env` file to add your `OPENAI_API_KEY`.

#### c. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Set Up the Frontend (App)

#### a. Navigate to the Frontend Directory
```bash
cd ../tars-app
```

#### b. Install Node.js Dependencies
```bash
yarn
```

## Running the Project

### 1. Start the Backend
```bash
cd api
python main.py
```

### 2. Start the Frontend
```bash
cd ../tars-app
yarn dev
```

## Usage
- Access the API at `http://localhost:8080`.
- Access the frontend application at `http://localhost:3000`.

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.
```
