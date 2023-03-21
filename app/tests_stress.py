from locust import HttpUser, TaskSet, task


class UserBehavior(HttpUser):
    ids =1
    @task
    def on_start(self):
        self.client.get("/")


    @task
    def posts(self):
        self.client.get("/todo/api/v1.0/tasks")

    @task
    def to_do(self):
        data = {
           'title': 'Сходить в химчистку',
           'description': 'Забрать плащ',
        }
        self.client.post("/todo/api/v1.0/tasks", json=data)

    # @task
    #
    # @task
    # def posts(self, ids=ids):
    #     self.client.delete(f"/todo/api/v1.0/tasks/{ids}")


class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000