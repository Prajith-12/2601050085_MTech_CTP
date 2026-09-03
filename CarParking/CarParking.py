import datetime
import math

TOTAL_SLOTS = 100
RATE_PER_HOUR = 20

parking_slots = {i: None for i in range(1, TOTAL_SLOTS + 1)}
active_vehicles = {}
available_slots = set(range(1, TOTAL_SLOTS + 1))

def display_availability():
    print(f"Available slots: {len(available_slots)} / {TOTAL_SLOTS}")
    if available_slots:
        sorted_slots = sorted(list(available_slots))
        print("Slot numbers:", sorted_slots[:10], "..." if len(sorted_slots) > 10 else "")
    else:
        print("Parking area is FULL.")

def allocate_slot(vehicle_number):
    if not available_slots:
        print("Sorry, parking area is full.")
        return None
    
    if vehicle_number in active_vehicles:
        print(f"Vehicle {vehicle_number} is already parked in slot {active_vehicles[vehicle_number]}.")
        return None

    slot = min(available_slots)
    available_slots.remove(slot)
    
    parking_slots[slot] = {
        "vehicle_number": vehicle_number,
        "entry_time": datetime.datetime.now()
    }
    active_vehicles[vehicle_number] = slot
    
    print(f"Vehicle {vehicle_number} assigned to slot {slot}.")
    return slot

def release_slot(vehicle_number):
    if vehicle_number not in active_vehicles:
        print(f"Vehicle {vehicle_number} not found in parking.")
        return None

    slot = active_vehicles.pop(vehicle_number)
    entry_time = parking_slots[slot]["entry_time"]
    exit_time = datetime.datetime.now()
    
    duration = exit_time - entry_time
    hours = max(1, math.ceil(duration.total_seconds() / 3600))
    fee = hours * RATE_PER_HOUR

    print(f"Vehicle {vehicle_number} left slot {slot}.")
    print(f"Duration: {hours} hour(s) | Fee: {fee} currency units")

    parking_slots[slot] = None
    available_slots.add(slot)
    
    return fee

def main():
    while True:
        print("\n--- Parking Management System ---")
        print("1. Display Availability")
        print("2. Vehicle Entry")
        print("3. Vehicle Exit")
        print("4. Exit Program")
        choice = input("Enter choice: ")

        if choice == "1":
            display_availability()
        elif choice == "2":
            vnum = input("Enter vehicle number: ").strip()
            if vnum:
                allocate_slot(vnum)
            else:
                print("Invalid vehicle number.")
        elif choice == "3":
            vnum = input("Enter vehicle number: ").strip()
            if vnum:
                release_slot(vnum)
            else:
                print("Invalid vehicle number.")
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
