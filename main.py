import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import os
import sys
import logging

from timer_utils import (
    set_record_time,
    calculate_relative_time,
    format_time
)

record_time = set_record_time()
beep_time = None
movement_time = None
finish_time = None
reaction_time = None
elapsed_time = None
race_duration = None



def main():
    print("AI Swim Analyzer Initialized.")
    # Set the record time
    record_time = set_record_time()
    
    # Example: Simulate timing a short process
    record_time = set_record_time()
    time.sleep(1.2)  # simulate waiting
    beep_time = record_time + 5.2  # example: beep detected 5.2s into video
    movement_time = record_time + 5.8  # example: movement detected
    finish_time = record_time + 50.7   # example: finish detected

    # Convert to race-relative times
    reaction = calculate_relative_time(movement_time, beep_time)
    race_duration = calculate_relative_time(finish_time, beep_time)

    # Display results
    print(f"Reaction Time: {format_time(reaction)}")
    print(f"Race Duration: {format_time(race_duration)}")
    print(f"Start Time: {format_time(record_time)}")
    print(f"Beep Time: {format_time(beep_time)}")
    print(f"Movement Time: {format_time(movement_time)}")
    print(f"Finish Time: {format_time(finish_time)}")


if __name__ == "__main__":
    main()
