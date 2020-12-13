import eel

# Setup
eel.init("web")

# Functions
@eel.expose
def helloWorld():
    print("Hello world!")

# Start
eel.start("index.html", mode="chrome", clock=False, size=(800, 480), port=2804)

# Run Once


# Main Loop
while True:
    eel.sleep(2)