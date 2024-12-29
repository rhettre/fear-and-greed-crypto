from fear_and_greed import FearAndGreedIndex

def lambda_handler(event, context):
    """AWS Lambda function to get current market sentiment."""
    fng = FearAndGreedIndex()
    
    current_value = fng.get_current_value()
    current_sentiment = fng.get_current_classification()
    
    return {
        'statusCode': 200,
        'body': {
            'value': current_value,
            'sentiment': current_sentiment,
            'should_buy': current_value < 30  # Example trading signal
        }
    } 