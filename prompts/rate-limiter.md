Detection: When the Vnstock API hits a rate limit, it raises a SystemExit exception with "rate limit" in the message
Response: The code catches this specific exception and:

Waits for 40 seconds (time.sleep(40))
Prints a throttling message
Retries the same request (continue loops back to the API call)


Fallback Strategy: If other exceptions occur (not rate limits), it tries the fallback data source (TCBS if VCI fails)
Additional Politeness: There's also a general 1-second delay between all API calls:
pythontime.sleep(1)  # <= polite pause per call
