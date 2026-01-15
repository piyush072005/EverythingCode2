import os
import time

import phonenumbers
from phonenumbers import NumberParseException
from twilio.base.exceptions import TwilioException
from twilio.rest import Client

# Configure your Twilio caller number (must be a Twilio number or a verified outbound caller ID).
CALLER_NUMBER = "+1 225 307 3216"
# Two-letter country code used when numbers omit a +countrycode (e.g., "IN" for India, "US" for United States).
DEFAULT_REGION = "US"

# Set Twilio credentials via environment variables.
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "AC9245b1796ff699ac97709540ac3413ce")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "51a980f2135fafac16ce1da23128b6fd")


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


def get_twilio_client():
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
        print("Set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables.")
        return None
    return Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def place_calls(caller_number, target_number, times, default_region=DEFAULT_REGION):
    if times <= 0:
        print("Number of calls must be positive.")
        return

    caller = parse_number(caller_number, default_region)
    target = parse_number(target_number, default_region)
    if not caller or not target:
        return

    client = get_twilio_client()
    if not client:
        return

    print(
        f"Using caller {caller['intl']} (country +{caller['country_code']}, region {caller['region']})"
    )
    print(
        f"Target {target['intl']} (country +{target['country_code']}, region {target['region']})"
    )

    for i in range(1, times + 1):
        try:
            call = client.calls.create(
                to=target["e164"],
                from_=caller["e164"],
                url="http://demo.twilio.com/docs/voice.xml",  # Simple Twilio-hosted demo TwiML.
            )
            print(f"Call {i}/{times} initiated, SID: {call.sid}")
        except TwilioException as exc:
            print(f"Failed to place call {i}: {exc}")
            return
        time.sleep(1)  # Throttle a bit between calls.


if __name__ == "__main__":
    if not CALLER_NUMBER:
        print("Set CALLER_NUMBER to your Twilio 'From' number (e.g., +15555550123).")
    else:
        try:
            target = input("Enter target phone number: ").strip()
            count = int(input("Enter number of simulated calls: "))
            place_calls(CALLER_NUMBER, target, count)
        except ValueError:
            print("Invalid input. Please enter a number for calls.")