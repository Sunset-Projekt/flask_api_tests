import unittest
import requests
from app import app, Task, db

class TestAPI(unittest.TestCase):
    def test_get_task(self):
        # Ожидаемые возврат в теле ответа
        expected_return = {
            "created_on": "Tue, 21 Mar 2023 08:18:21 GMT",
            "description": "она самая! даже измененная",
            "done": False,
            "id": 2,
            "title": "вторая заметка"
        }

                # Отправка запроса по получению всех элементов
        response = requests.get("http://localhost:5000/api//tasks/2")
        # Проверяем соответствие
        self.assertEqual(response.json(),expected_return)

    # def test_post_task(self):
    #     with app.app_context():
    #         title = "Прогуляться"
    #         description = "Найти приятное место"
    #         expected_return = {
    #             'id': Task.query.all()[-1].id + 1,
    #             'title': title,
    #             'description': description,
    #             'done': False
    #         }
    #         response = requests.post("http://localhost:5000/todo/api/v1.0/tasks", {"title": title, "description": description})
    #         self.assertEqual(response.json(),expected_return)
if __name__ == '__main__':
    unittest.main()