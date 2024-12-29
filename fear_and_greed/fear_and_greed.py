import requests
from datetime import datetime, timedelta
from typing import List, Dict, Union, Optional
from statistics import mean, median

class FearAndGreedIndex:
    """A simple wrapper for the Alternative.me Crypto Fear & Greed Index API."""
    
    BASE_URL = "https://api.alternative.me/fng/"
    
    def __init__(self):
        self.session = requests.Session()

    def get_current_value(self) -> int:
        """Get the current Fear & Greed Index value (0-100)."""
        data = self._make_request(limit=1)
        return int(data['data'][0]['value'])
    
    def get_current_classification(self) -> str:
        """Get the current Fear & Greed Index classification 
        (Extreme Fear, Fear, Neutral, Greed, or Extreme Greed)."""
        data = self._make_request(limit=1)
        return data['data'][0]['value_classification']
    
    def get_current_data(self) -> Dict:
        """Get complete current Fear & Greed Index data including value, 
        classification and timestamp."""
        data = self._make_request(limit=1)
        return data['data'][0]
    
    def get_value_for_date(self, date: datetime) -> int:
        """Get the Fear & Greed Index value for a specific date."""
        data = self.get_historical_data(date, date)
        if not data:
            raise ValueError(f"No data available for date: {date.date()}")
        return int(data[0]['value'])
    
    def get_historical_data(self, start_date: datetime, end_date: Optional[datetime] = None) -> List[Dict]:
        """Get Fear & Greed Index data between two dates."""
        if not end_date:
            end_date = datetime.now()
            
        days = (end_date - start_date).days + 1
        data = self._make_request(limit=days)
        
        return [
            entry for entry in data['data']
            if start_date <= datetime.fromtimestamp(int(entry['timestamp'])) <= end_date
        ]
    
    def get_last_n_days(self, days: int) -> List[Dict]:
        """Get Fear & Greed Index data for the last n days."""
        data = self._make_request(limit=days)
        return data['data']

    def calculate_average(self, days: int) -> float:
        """Calculate the average Fear & Greed Index value over the last n days."""
        historical_data = self.get_last_n_days(days)
        values = [int(entry['value']) for entry in historical_data]
        return mean(values)
    
    def calculate_median(self, days: int) -> float:
        """Calculate the median Fear & Greed Index value over the last n days."""
        historical_data = self.get_last_n_days(days)
        values = [int(entry['value']) for entry in historical_data]
        return median(values)

    def _make_request(self, **params) -> Dict:
        """Make a request to the Fear & Greed Index API."""
        try:
            response = self.session.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data['metadata']['error']:
                raise ValueError(f"API Error: {data['metadata']['error']}")
                
            return data
            
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to the Fear & Greed Index API: {str(e)}") 