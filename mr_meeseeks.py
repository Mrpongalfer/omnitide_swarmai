import sys
import time

def mr_meeseeks_task(task):
    print(f"👀 I'm Mr. Meeseeks! Doing the task: {task}")
    time.sleep(2)
    print(f"✅ Task completed: {task}")
    print("💀 Poof! Mr. Meeseeks has self-destructed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Please provide a task for Mr. Meeseeks.")
    else:
        mr_meeseeks_task(" ".join(sys.argv[1:]))
