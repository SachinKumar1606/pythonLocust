import time

from locust import User, task, between, constant, constant_pacing

class MyUser(User):

    wait_time = constant_pacing(3)

    @task
    def launch(self):
        time.sleep(5)
        print("This will inject 1 sec delay")
