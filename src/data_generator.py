import pandas as pd
import numpy as np
import datetime

def generate_data(output_path="data/raw/sensor_data.csv"):
    """Generates sample sensor data and saves it to a CSV file."""
    num_records = 200
    start_date = datetime.datetime(2023, 10, 26, 8, 0, 0)

    data = {
        "timestamp": [start_date + datetime.timedelta(minutes=15 * i) for i in range(num_records)],
        "sensor_id": np.random.choice(['sensor_A', 'sensor_B'], size=num_records),
        "event_type": np.random.choice(['enter', 'exit'], size=num_records, p=[0.6, 0.4])
    }

    df = pd.DataFrame(data)

    # Assign +1 for 'enter' and -1 for 'exit'
    df['event_value'] = df['event_type'].apply(lambda x: 1 if x == 'enter' else -1)

    # Ensure the first event is an entry
    df.loc[0, 'event_type'] = 'enter'
    df.loc[0, 'event_value'] = 1

    df.to_csv(output_path, index=False)
    print(f"Sample data generated and saved to {output_path}")

if __name__ == "__main__":
    generate_data()