"""Parse a 12-hour time string and print it in 24-hour format.

This file is named `datetime.py`, which would shadow the standard
library module `datetime` if we tried to import it. To avoid that
problem we use the `time` module (part of the standard library) to
parse the string and format the output as `HH:MM:SS`.
"""

import time

current_time = '5:55 PM'

def to_24h(time_str: str) -> str:
	"""Convert a 12-hour time string like '5:55 PM' to '17:55:00'."""
	t = time.strptime(time_str, "%I:%M %p")
	return time.strftime("%H:%M:%S", t)


if __name__ == "__main__":
	print(to_24h(current_time))