# Room Occupancy Data Pipeline

This project is an end-to-end data engineering pipeline that simulates processing sensor data to monitor room occupancy and control electrical appliances accordingly.

## Project Overview

The pipeline performs the following steps:
1.  **Data Ingestion**: Generates sample time-series data from room sensors that detect entries and exits.
2.  **Data Processing**: Calculates the real-time occupancy of the room based on sensor events.
3.  **Appliance Control Logic**: Determines whether appliances should be ON or OFF based on the room's occupancy.
4.  **Data Storage**: Stores the processed data with appliance status in a CSV file.

## Project Structure
```
room-occupancy-pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── data_generator.py
│   └── data_processor.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## How to Run the Project

### Prerequisites
*   Python 3.8+
*   pip

### Setup and Execution

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/<your-username>/room-occupancy-pipeline.git
    cd room-occupancy-pipeline
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the main pipeline script:**
    ```bash
    python main.py
    ```

This will execute the entire pipeline:
*   `data/raw/sensor_data.csv` will be created.
*   `data/processed/appliance_status.csv` will be generated with the final output.

## Output Data

The processed data in `data/processed/appliance_status.csv` will have the following columns:

*   **timestamp**: The time of the event.
*   **sensor_id**: The ID of the sensor that recorded the event.
*   **event_type**: `enter` or `exit`.
*   **person_count**: The number of people in the room after the event.
*   **appliance_status**: `ON` if `person_count` > 0, otherwise `OFF`.