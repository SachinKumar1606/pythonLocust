from locust import TaskSet, constant, task, HttpUser

class MyHttpCat(TaskSet):

    @task
    def getStatus(self):
        self.client.get("/200")
        print("Get Status of 200")
        self.interrupt(reschedule=False)


class AnotherMyHttpCat(TaskSet):
    @task
    def getRandom(self):
        self.client.get("/500")
        print("Get Status of 500")
        self.interrupt(reschedule=False)

class MyLoadTest2(HttpUser):
    host = "https://http.cat"
    tasks = [MyHttpCat, AnotherMyHttpCat]
    wait_time = constant(1)

