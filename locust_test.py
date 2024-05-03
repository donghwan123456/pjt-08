from locust import HttpUser, task, TaskSet, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)
    @task
    def find_similar_age_rows(self):
        response = self.client.get("test/find-similar-age-rows/")  # Django 엔드포인트 경로
        if response.status_code == 200:
            print("Response:", response.text)
        else:
            print("Error:", response.status_code)

#     def on_start(self):
#         print('test start')

#     @task
#     def normal_sort(self):
#         self.client.get("test/normal_sort/")

#     @task
#     def priority_queue(self):
#         self.client.get("test/priority_queue/")

#     @task
#     def bubble_sort(self):
#         self.client.get("test/bubble_sort/")

# class WebsiteTasks(TaskSet):
#     @task
#     def read_csv(self):
#         response = self.client.get("/read-csv/")
#         print(response.text)

#     @task
#     def bubble_sort(self):
#         response = self.client.get("/bubble-sort/")
#         print(response.text)

#     @task
#     def normal_sort(self):
#         response = self.client.get("/normal-sort/")
#         print(response.text)

#     @task
#     def priority_queue(self):
#         response = self.client.get("/priority-queue/")
#         print(response.text)

#     @task
#     def replace_empty_with_null(self):
#         response = self.client.get("/replace-empty-with-null/")
#         print(response.text)

    # @task
    # def find_similar_age_rows(self):
    #     response = self.client.get("/find-similar-age-rows/")
    #     print(response.text)

# class WebsiteUser(HttpUser):
#     wait_time = between(5, 9)
#     tasks = [WebsiteTasks]