import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from requests.exceptions import RequestException
from fear_and_greed import FearAndGreedIndex

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise Exception(f"HTTP Status: {self.status_code}")

class TestFearAndGreedIndex(unittest.TestCase):
    def setUp(self):
        self.fng = FearAndGreedIndex()
        self.mock_current_data = {
            "name": "Fear and Greed Index",
            "data": [{
                "value": "25",
                "value_classification": "Extreme Fear",
                "timestamp": "1648744800",
                "time_until_update": "86400"
            }],
            "metadata": {"error": None}
        }
        
        self.mock_historical_data = {
            "name": "Fear and Greed Index",
            "data": [
                {"value": "25", "value_classification": "Extreme Fear", "timestamp": "1648744800"},
                {"value": "30", "value_classification": "Fear", "timestamp": "1648658400"},
                {"value": "35", "value_classification": "Fear", "timestamp": "1648572000"},
                {"value": "40", "value_classification": "Fear", "timestamp": "1648485600"},
                {"value": "45", "value_classification": "Fear", "timestamp": "1648399200"},
                {"value": "50", "value_classification": "Neutral", "timestamp": "1648312800"},
                {"value": "55", "value_classification": "Greed", "timestamp": "1648226400"}
            ],
            "metadata": {"error": None}
        }

    @patch('requests.Session.get')
    def test_get_current_value(self, mock_get):
        """Test that current value is an integer between 0 and 100."""
        mock_get.return_value = MockResponse(self.mock_current_data)
        
        value = self.fng.get_current_value()
        self.assertEqual(value, 25)
        self.assertIsInstance(value, int)

    @patch('requests.Session.get')
    def test_get_current_classification(self, mock_get):
        """Test that classification is one of the expected values."""
        mock_get.return_value = MockResponse(self.mock_current_data)
        
        classification = self.fng.get_current_classification()
        self.assertEqual(classification, "Extreme Fear")

    @patch('requests.Session.get')
    def test_get_historical_data(self, mock_get):
        """Test historical data retrieval."""
        mock_get.return_value = MockResponse(self.mock_historical_data)
        
        start_date = datetime.fromtimestamp(1648226400)  # First day in mock data
        end_date = datetime.fromtimestamp(1648744800)    # Last day in mock data
        
        data = self.fng.get_historical_data(start_date, end_date)
        self.assertEqual(len(data), 7)
        self.assertEqual(data[0]['value'], "25")
        self.assertEqual(data[-1]['value'], "55")

    @patch('requests.Session.get')
    def test_calculate_average(self, mock_get):
        """Test average calculation."""
        mock_get.return_value = MockResponse(self.mock_historical_data)
        
        avg = self.fng.calculate_average(7)
        self.assertEqual(avg, 40.0)  # (25 + 30 + 35 + 40 + 45 + 50 + 55) / 7

    @patch('requests.Session.get')
    def test_calculate_median(self, mock_get):
        """Test median calculation."""
        mock_get.return_value = MockResponse(self.mock_historical_data)
        
        median = self.fng.calculate_median(7)
        self.assertEqual(median, 40.0)  # Middle value of sorted array

    @patch('requests.Session.get')
    def test_api_error(self, mock_get):
        """Test API error handling."""
        error_response = {
            "metadata": {"error": "API Error"}
        }
        mock_get.return_value = MockResponse(error_response)
        
        with self.assertRaises(ValueError):
            self.fng.get_current_value()

    @patch('requests.Session.get')
    def test_connection_error(self, mock_get):
        """Test connection error handling."""
        mock_get.side_effect = RequestException("Connection failed")
        
        with self.assertRaises(ConnectionError):
            self.fng.get_current_value()

if __name__ == '__main__':
    unittest.main() 