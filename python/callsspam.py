import time

import phonenumbers
from phonenumbers import NumberParseException

# Set your caller number (ideally E.164 with +countrycode).
CALLER_NUMBER = "+919953175450"
DEFAULT_REGION = "IND"  # Used when numbers omit the +countrycode.


def parse_number(raw_number, default_region):
    try:
        parsed = phonenumbers.parse(raw_number, default_region)
    except NumberParseException as exc:
        print(f"Invalid phone number '{raw_number}': {exc}")
        return None

    if not phonenumbers.is_valid_number(parsed):
        print(f"Invalid phone number '{raw_number}': failed validation.")
        return None

    region = phonenumbers.region_code_for_number(parsed) or "Unknown"
    country_code = parsed.country_code
    intl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
    return {
        "raw": raw_number,
        "region": region,
        "country_code": country_code,
        "intl": intl,
        "e164": e164,
    }


# Simulate making repeated calls (no real calls are made)
def simulate_calls(caller_number, target_number, times, default_region=DEFAULT_REGION):
    if times <= 0:
        print("Number of calls must be positive.")
        return

    caller = parse_number(caller_number, default_region)
    target = parse_number(target_number, default_region)
    if not caller or not target:
        return

    print(
        f"Using caller {caller['intl']} (country +{caller['country_code']}, region {caller['region']})"
    )
    print(
        f"Target {target['intl']} (country +{target['country_code']}, region {target['region']})"
    )

    for i in range(1, times + 1):
        print(f"Simulated call {i} from {caller['e164']} to {target['e164']}...")
        time.sleep(1)  # Delay to mimic call duration


if __name__ == "__main__":
    if not CALLER_NUMBER:
        print("Set CALLER_NUMBER to your outbound number (e.g., +15555550123).")
    else:
        try:
            target = input("Enter target phone number: ").strip()
            count = int(input("Enter number of simulated calls: "))
            simulate_calls(CALLER_NUMBER, target, count)
        except ValueError:
            print("Invalid input. Please enter a number for calls.")
