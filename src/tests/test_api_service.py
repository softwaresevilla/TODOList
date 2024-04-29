import unittest
from unittest.mock import MagicMock
from src.models.todo import Todo
from src.Services.ApiService import ApiService

class TestApiService(unittest.TestCase):
    def test_fetch_todo_data_success(self):
        requests_mock = MagicMock()
        requests_mock.get.return_value.json.return_value = [
            {"id": 1, "title": "Todo 1", "completed": False},
            {"id": 2, "title": "Todo 2", "completed": True}
        ]
        api_service = ApiService(requests_mock)
        result = api_service.fetch_todo_data()
        self.assertEqual(len(result), 2)

    def test_fetch_todo_data_error(self):
        requests_mock = MagicMock()
        requests_mock.get.side_effect = Exception("Test error")
        api_service = ApiService(requests_mock)
        with self.assertRaises(Exception):
            api_service.fetch_todo_data()

    def test_write_todo_data_to_file_success(self):
        todo = Todo(id=1, userId=1, title="Test Todo", completed=False)
        api_service = ApiService()
        with unittest.mock.patch("builtins.open", unittest.mock.mock_open()) as mock_file:
            api_service.write_todo_data_to_file(todo)
            mock_file.assert_called_once_with("./storage/2024_04_29_1.csv", "w", newline="", encoding="utf-8")

    def test_write_todo_data_to_file_unexpected_error(self):
        todo = Todo(id=1, userId=1, title="Test Todo", completed=False)
        
        api_service = ApiService()
        
        with unittest.mock.patch("builtins.open", side_effect=Exception("Test error")):
            with self.assertRaises(Exception):
                api_service.write_todo_data_to_file(todo)
