from locust import HttpUser, constant, task


class MyResReq(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(2)

    @task
    def getUser(self):
        res = self.client.get("/api/users?page=2")
        assert res.status_code is 200
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def postUser(self):
        res = self.client.post("/api/users", data='''
        {name: "morpheus", job: "leader"}
        ''')
        print(res.text)
        assert res.status_code is 201
        print(res.status_code)
        print(res.headers)
