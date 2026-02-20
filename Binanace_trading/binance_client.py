import logging
from binance.um_futures import UMFutures

# Standard logging configuration to force file creation
logging.basicConfig(
    filename='binance_orders.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)
logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self, key, secret):
        self.client = UMFutures(
            key=key, 
            secret=secret, 
            base_url="https://testnet.binancefuture.com"
        )

    def place_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity,
        }
        
        if order_type.upper() == 'LIMIT':
            params['price'] = price
            params['timeInForce'] = 'GTC'

        try:
            logger.info(f"Sending Request: {params}")
            # Execute the order
            response = self.client.new_order(**params)
            logger.info(f"Received Response: {response}")
            return response
        except Exception as e:
            logger.error(f"API Error: {str(e)}")
            raise e