from src.data_generator import generate_data
from src.data_processor import process_data
import os

def main():
    """Runs the end-to-end data pipeline."""
    # Create directories if they don't exist
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    print("--- Starting Data Generation ---")
    generate_data()
    print("--- Data Generation Complete ---\n")

    print("--- Starting Data Processing ---")
    process_data()
    print("--- Data Processing Complete ---")

if __name__ == "__main__":
    main()