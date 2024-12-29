from fear_and_greed import FearAndGreedIndex
from datetime import datetime, timedelta

def should_buy_bitcoin():
    """Simple trading strategy based on extreme fear levels."""
    fng = FearAndGreedIndex()
    fear_level = fng.get_current_value()
    
    # Example strategy: Buy when fear is high (value < 30)
    if fear_level < 30:
        return True
    return False

def analyze_market_sentiment():
    """Analyze market sentiment using multiple indicators."""
    fng = FearAndGreedIndex()
    
    # Get last 14 days of data and calculate average
    two_weeks = fng.get_last_n_days(14)
    avg_sentiment = sum(int(day['value']) for day in two_weeks) / len(two_weeks)
    return avg_sentiment

def generate_market_report():
    """Generate a comprehensive market sentiment report."""
    fng = FearAndGreedIndex()
    
    # Get current data
    current = fng.get_current_data()
    
    # Get data from last month
    month_ago = datetime.now() - timedelta(days=30)
    monthly_trend = fng.get_historical_data(month_ago)
    
    report = {
        "current_sentiment": current['value_classification'],
        "current_value": current['value'],
        "monthly_datapoints": len(monthly_trend),
        "monthly_average": fng.calculate_average(30),
        "monthly_median": fng.calculate_median(30)
    }
    
    return report

if __name__ == "__main__":
    # Example usage
    if should_buy_bitcoin():
        print("Market shows extreme fear - consider buying!")
    
    avg_sentiment = analyze_market_sentiment()
    print(f"14-day average sentiment: {avg_sentiment:.1f}")
    
    report = generate_market_report()
    print(f"\nMarket Report:")
    print(f"Current Sentiment: {report['current_sentiment']}")
    print(f"Current Value: {report['current_value']}")
    print(f"30-day Average: {report['monthly_average']:.1f}")
    print(f"30-day Median: {report['monthly_median']:.1f}") 