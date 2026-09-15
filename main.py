import requests

# Step 1 & 2: Tell the computer where to go and knock on the door
response = requests.get("http://www.google.com")

# Step 3 & 4: Your exact logic!
if response.status_code == 200:
    print("It's on!")
else:
    print("It's off!")