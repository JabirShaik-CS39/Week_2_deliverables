## Sequential Workflow
def read_document():
    return "Artificial Intelligence is transforming industries."

def summarize(text):
    return text[:40] + "..."

def translate(text):
    return "Traducción: " + text

doc = read_document()
summary = summarize(doc)
translated = translate(summary)

print(translated)


## Conditional Workflow
message = "I need refund"

if "refund" in message:
    print("Route to Support Team")
else:
    print("Route to Sales Team")


## Parallel Workflow
import threading
import time

def task1():
    time.sleep(2)
    print("Task 1 Completed")

def task2():
    time.sleep(2)
    print("Task 2 Completed")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()