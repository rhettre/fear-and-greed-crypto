# Crypto Fear and Greed Index API

A simple Python wrapper for the Alternative.me Crypto Fear and Greed Index API. Get Bitcoin market sentiment data easily with intuitive methods.

## Installation

```bash
pip install fear-and-greed-crypto
```

## Quick Start

```python
from fear_and_greed import FearAndGreedIndex

# Initialize the client
fng = FearAndGreedIndex()

# Get current index value (0-100)
value = fng.get_current_value()
print(f"Current Fear & Greed Index: {value}")

# Get current classification
sentiment = fng.get_current_classification()
print(f"Market sentiment: {sentiment}")  # e.g., "Extreme Fear", "Neutral", "Greed"

# Get complete current data
today = fng.get_current_data()

# Get historical data
from datetime import datetime, timedelta

# Last 7 days
week_data = fng.get_last_n_days(7)

# Data between specific dates
start_date = datetime.now() - timedelta(days=30)
monthly_data = fng.get_historical_data(start_date)

# Calculate averages and medians
week_avg = fng.calculate_average(7)
month_median = fng.calculate_median(30)
```

## Available Methods

### Basic Methods
- `get_current_value()` - Get current fear and greed index (0-100)
- `get_current_classification()` - Get current market sentiment classification
- `get_current_data()` - Get complete current data including value, classification, and timestamp

### Historical Data
- `get_last_n_days(days: int)` - Get data for the last n days
- `get_historical_data(start_date: datetime, end_date: Optional[datetime] = None)` - Get data between dates

### Analysis Methods
- `calculate_average(days: int)` - Calculate average index value over specified days
- `calculate_median(days: int)` - Calculate median index value over specified days

## Example Trading Strategy

```python
def should_buy_bitcoin():
    fng = FearAndGreedIndex()
    fear_level = fng.get_current_value()
    
    # Buy when fear is high (value < 30)
    return fear_level < 30

# Example usage
if should_buy_bitcoin():
    print("Market shows extreme fear - consider buying!")
```

See more examples in the `examples` directory.

## Data Attribution

Data provided by [Alternative.me](https://alternative.me/crypto/fear-and-greed-index/). When using this data, please properly acknowledge the source and prominently reference it accordingly.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Author

Rhett Reisman

Email: rhett@rhett.blog

GitHub: https://github.com/rhettre/fear-and-greed-crypto

## Disclaimer

This project is not affiliated with, maintained, or endorsed by Alternative.me. Use this software at your own risk. Trading cryptocurrencies carries a risk of financial loss. The developers of this software are not responsible for any financial losses or damages incurred while using this software. Nothing in this software should be seen as an inducement to trade with a particular strategy or as financial advice.
