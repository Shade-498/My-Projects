import time

def stopwatch():
  start_time = time.time() # Get the start time
  print("Stopwatch started. Press Ctrl+C to stop.")

  try:
    while True:
      current_time = time.time() # Get the current time
      elapsed_time = current_time - start_time # Calculate elapsed time
      print(f"Elapsed time: {elapsed_time:.2f} seconds")
      time.sleep(1) # Update every second
  except KeyboardInterrupt: # Stop the stopwatch when Ctrl+C is pressed
    print("\nStopwatch stopped.")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
  stopwatch()
