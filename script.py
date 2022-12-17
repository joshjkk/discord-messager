import requests
import time


# Work channel
work_channel = r"CHANNEL LINK"

# Message to send
payload = {
    'content': "!work"
}

# Authorizations
headers = {
    'authorization': "AUTHORIZATION KEY"
}

# Timeout length in seconds
TIMEOUT = 30


def work() -> None:
    # Send message
    requests.post(url=work_channel, data=payload, headers=headers)



def main() -> int:
    try:
        while True:
            work()
            # Wait for timeout
            time.sleep(TIMEOUT)

        return 0

    except Exception as e:
        print("Error: ", e)
        return 1

if __name__ == "__main__":
    exit(main())
