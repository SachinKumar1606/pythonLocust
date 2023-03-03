from locust import SequentialTaskSet, constant, task, HttpUser

class MyHttpCat(SequentialTaskSet):

    @task
    def getStatus(self):
        self.client.get("/200")
        print("Get Status of 200")

    @task
    def getRandom(self):
        self.client.get("/500")
        print("Get Status of 500")

class MyLoadTest1(HttpUser):

    host = "https://http.cat"
    tasks = [MyHttpCat]
    wait_time = constant(1)

