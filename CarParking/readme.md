# Parking Management System

## Description

This project contains a Python script that implements a simple **Parking Management System**. It manages **100 parking slots**, assigns available slots to vehicles, and calculates parking fees when vehicles leave.

## Algorithm

The core logic of the system follows this step-by-step algorithm:

1. **Start**
2. **Display Availability slots:** Check and show the current number of available slots.
3. **Read vehicle number:** Capture the required details (number plate) for the vehicle.
4. **Check whether parking is available:** Check if there is at least one empty slot out of the 100.
5. **Assign or Reject:**
   * **If slot available:** Assign a slot to the vehicle and record the entry time.
   * **Else:** Display a message stating that the parking is full.
6. **When vehicle exits:**
   * Find the vehicle in the records.
   * Calculate the parking duration (using entry and exit times).
   * Calculate the parking fee.
   * Update availability (free up the parking slot).


## Input and Output

### Input
Enter choice: 2

Enter vehicle number: ap22idhnr

### Output
Vehicle ap22idhnr assigned to slot 1.

When the vehicle exits:

Vehicle ap22idhnr left slot 1.

Duration: 1 hour(s) | Fee: 20 currency units
