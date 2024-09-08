import time
from datetime import datetime

class SimpleAgent:
    def __init__(self):
        self.running = True

    def sense(self):
        """현재 시간을 감지하는 메서드"""
        current_time = datetime.now()
        return current_time

    def act(self, current_time):
        """현재 시간에 따라 다른 행동을 취하는 메서드"""
        if current_time.hour < 12:
            print(f"Good morning! It's {current_time.strftime('%H:%M:%S')}.")
        else:
            print(f"Good afternoon! It's {current_time.strftime('%H:%M:%S')}.")

    def run(self):
        """에이전트를 지속적으로 동작하게 하는 메서드"""
        while self.running:
            current_time = self.sense()
            self.act(current_time)
            time.sleep(5)  # 5초마다 동작

# 에이전트 실행
if __name__ == "__main__":
    agent = SimpleAgent()
    agent.run()
