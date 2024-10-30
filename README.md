# Property Valuation API

This project provides a machine learning model and API for property valuation based on property features. The API takes property data as input and returns a valuation prediction. The application is containerized using Docker and can be run locally.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Installation and Setup](#installation-and-setup)
4. [Running the API](#running-the-api)
5. [Making Predictions](#making-predictions)
6. [Logging](#logging)
7. [Assumptions](#assumptions)

## Project Overview

This API provides property valuation predictions based on the provided property data. It uses a trained machine learning model and is accessible via a FastAPI server, which allows for secure and scalable deployment. The API currently accepts property features as input and returns a single prediction.

## Project Structure

The directory structure is as follows:
```
property-valuation-project/ 
├── data/ 
│ ├── train.csv
│ └── test.csv
├── logs/ 
├── model/
│ └── model_pipeline.pkl
├── src/ 
│ ├── init.py
│ ├── app.py 
│ ├── train.py 
│ ├── inference.py 
│ ├── data_loader.py 
│ ├── preprocessing.py 
│ ├── run_pipeline.py 
│ └── model_config.py 
├── Dockerfile 
├── requirements.txt 
├── README.md 
└── .env
```

## Installation and Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/property-valuation-project.git
    cd property-valuation-project
    ```

2. **Install Dependencies**
- Create a virtual environment (the example is using miniconda).
    ```bash
    conda create --name "<NAME_OF_YOUR_ENV>" python=3.10
    ```
- Install Python packages.
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**
- Create a `.env` file in the root directory and add the API key (replace `your_api_key` with your actual API key):

    ```bash
    API_KEY=your_api_key
    ```

4. **Running the pipeline**
- To run the pipeline that tranforms the data and trains the model:
    
    ```bash
    python src/run_pipeline.py
    ```

## Running the API

1. **Start the FastAPI Server**
   ```bash
   uvicorn src.app:app --reload
   ```

2. **Testing the Health Check Endpoint**
- Open your browser or use curl:
    ```bash
    curl http://127.0.0.1:8000/ 
    ```
- You should see:

    {"message": "Property valuation API is running"}

## Making Predictions

Once the API is running, you can make predictions with the ```/predict``` endpoint.

#### Example Prediction Request:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'X-API-Key: your_api_key' \
  -d '{
        "type": "casa" ,
        "sector": "vitacura" ,
        "net_usable_area": 152.0 ,
        "net_area": 257.0 ,
        "n_rooms": 3.0 ,
        "n_bathroom": 3.0 ,
        "latitude": -33.3794 ,
        "longitude": -70.5447
    }'
```
## Running with Docker
To run the API in a Docker container, follow these steps:

1. Build the Docker Image

- In the root directory of the project, build the Docker image:

```bash
docker build -t property-valuation-api .
```

2. Run the Docker Container

- Start the container with the following command, replacing ```/path/to/.env``` with the actual path to your ```.env``` file:

```bash
docker run -d -p 8000:8000 --env-file /path/to/.env property-valuation-api
```
- This will run the API at ```http://127.0.0.1:8000.```

3. Testing the API in Docker

- Access the health check endpoint:
```bash
curl http://127.0.0.1:8000/
```

- Make predictions using the same instructions as in the [Making Predictions](#making-predictions) section.

## Logging
API calls are logged in the file api_logs.log. Logs capture:

- Request paths and methods
- Response statuses
- Unauthorized access attempts
- Prediction requests and results

This logging ensures transparency and helps monitor API usage and errors.

## Assumptions

- Assumes input features match the model’s requirements.