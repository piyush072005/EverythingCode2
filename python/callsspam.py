import time

# Simulate making repeated calls (no real calls are made)
def simulate_calls(phone_number, times):
    if not phone_number:
        print("Phone number is required.")
        return
    if not phone_number.isdigit():
        print("Phone number should contain digits only.")
        return
    if times <= 0:
        print("Number of calls must be positive.")
        return

    for i in range(1, times + 1):
        print(f"Simulated call {i} to {phone_number}...")
        time.sleep(1)  # Delay to mimic call duration


if __name__ == "__main__":
    try:
        phone = input("Enter phone number: ").strip()
        count = int(input("Enter number of simulated calls: "))
        simulate_calls(phone, count)
    except ValueError:
        print("Invalid input. Please enter a number for calls.")
