import pandas as pd

def process_data(input_path="data/raw/sensor_data.csv", output_path="data/processed/appliance_status.csv"):
    """
    Reads raw sensor data, calculates room occupancy, determines appliance status,
    and saves the processed data.
    """
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"Error: The file at {input_path} was not found.")
        return

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by="timestamp")

    # Calculate the cumulative person count
    df['person_count'] = df['event_value'].cumsum()

    # Ensure person count does not go below zero
    df['person_count'] = df['person_count'].clip(lower=0)

    # Determine the status of the appliances
    df['appliance_status'] = df['person_count'].apply(lambda x: 'ON' if x > 0 else 'OFF')
    
    # Select final columns for the output
    processed_df = df[['timestamp', 'sensor_id', 'event_type', 'person_count', 'appliance_status']]

    processed_df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    process_data()