import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import Mock, patch


class PredictionTests(unittest.TestCase):
    def setUp(self):
        path = Path(__file__).resolve().parents[1] / 'app.py'
        spec = importlib.util.spec_from_file_location('rain_test_app', path)
        self.module = importlib.util.module_from_spec(spec)
        self.model = Mock()
        self.model.predict.return_value = [0]
        with patch.object(Path, 'open', return_value=io.BytesIO()), patch('pickle.load', return_value=self.model):
            spec.loader.exec_module(self.module)
        self.client = self.module.app.test_client()

    def test_browser_date_and_two_dimensional_prediction(self):
        data = {field: '1' for field in self.module.FEATURE_FIELDS}
        data['date'] = '2026-10-08'
        with patch.object(self.module, 'render_template', return_value='sunny'):
            response = self.client.post('/predict', data=data)
        self.assertEqual(response.status_code, 200)
        matrix = self.model.predict.call_args.args[0]
        self.assertEqual(len(matrix), 1)
        self.assertEqual(len(matrix[0]), 23)
        self.assertEqual(matrix[0][-2:], [10.0, 8.0])

    def test_get_and_invalid_input(self):
        with patch.object(self.module, 'render_template', return_value='form'):
            self.assertEqual(self.client.get('/predict').status_code, 200)
        self.assertEqual(self.client.post('/predict', data={'date': 'invalid'}).status_code, 400)
        self.model.predict.assert_not_called()

if __name__ == '__main__':
    unittest.main()
