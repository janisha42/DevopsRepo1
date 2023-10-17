import psutil
import time

# Predefined threshold for CPU usage (in percentage)
threshold = 80

print("Monitoring CPU usage...")

try:
    while True:
        # Get current CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Check if CPU usage exceeds the threshold
        if cpu_usage > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
        else:
            print(f"CPU usage: {cpu_usage}%", end='\r')  # Use '\r' to overwrite the same line
        
        # Sleep for 1 second before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped. Exiting...")
except Exception as e:
    print(f"An error occurred: {e}")
