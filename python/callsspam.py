import time

# Simulate making repeated calls (no real calls are made)
def simulate_calls(contact_name, times):
    if times <= 0:
        print("Number of calls must be positive.")
        return
    
    for i in range(1, times + 1):
        print(f"Simulated call {i} to {contact_name}...")
        time.sleep(1)  # Delay to mimic call duration

# Example usage
try:
    name = input("Enter contact name: ").strip()
    count = int(input("Enter number of simulated calls: "))
    simulate_calls(name, count)
except ValueError:
    print("Invalid input. Please enter a number for calls.")
