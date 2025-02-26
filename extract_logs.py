import os
import sys

def get_logs(log_file, date, size=1024 * 1024):
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, f"logs_{date}.txt")

    try:
        with open(log_file, "r", buffering=size) as file, open(output_path, "w") as output:
            for line in file:
                if line.startswith(date):
                    output.write(line)

        print(f"Logs saved in: {output_path}")

    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]
    log_file = "test_logs.log"
    
    get_logs(log_file, date)
