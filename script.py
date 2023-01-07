import requests
import time


########## FILL THESE PARAMETERS IN ##########

# Channel link
# LOOKS SOMETHING LIKE THIS:
# https://discord.com/api/vNUMBER/SOME_NUMBERS/messages
channel = r"LINK TO THE CHANNEL"

# Message to send
payload = {
    'content': "MESSAGE TO SEND"
}

# Authorization
headers = {
    'authorization': "AUTHORIZATION KEY"
}

timeout = 30 # Timeout length in seconds

########## FILL THESE PARAMETERS IN ##########



def send_message() -> None:
    # Send message
    requests.post(url=channel, data=payload, headers=headers)


def main() -> int:
    print("Discord does not allow self-bots, by using this software, you are aware of possible account termination.")
    print("See https://support.discord.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots- for support on self-bots.")

    try:
        while True:
            # Send message and wait [timeout] seconds
            send_message()
            time.sleep(timeout)

        return 0

    except Exception as e:
        print("Error: ", e)
        return 1

if __name__ == "__main__":
    exit(main())
