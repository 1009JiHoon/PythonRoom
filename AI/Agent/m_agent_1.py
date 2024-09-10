import time
from datetime import datetime

class MyAgent:
    def __init__(self):
        self.running = True

    def sense(self):
        current_time = datetime.now()
        return current_time
    
    def act(self, current_time):
        if current_time.hour < 12:
            print(f"Good Morning it's {current_time.strftime('%H:%M:%S')}.")
        else:
            print(f"Good Afternoon! it's {current_time.strftime('%H:%M:%S')}.")

    def run(self):
        while self.running:
            current_time = self.sense()
            self.act(current_time)
            time.sleep(4)

if __name__ == "__main__":
    agent = MyAgent()
    agent.run()