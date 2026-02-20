import typer
from typing import Optional
from binance_client import BinanceFuturesClient

app = typer.Typer()

@app.command()
def main(
    symbol: str = typer.Option(..., "--symbol"),
    side: str = typer.Option(..., "--side"),
    order_type: str = typer.Option(..., "--order-type"),
    quantity: float = typer.Option(..., "--quantity"),
    price: Optional[float] = typer.Option(None, "--price")
):
    # Use your actual Testnet API keys here
    client = BinanceFuturesClient("dP6HCAXQukrET6Of0PRVaJQ2C77xE9XIKEQVj5ptBWF78hoRAiOTiPI3bOqGO6Gh", "06Y6Hn1PW4ywnPnmHX2LfZoQKTKje2v7sBW1YVP3zugHOhzieRxA5oAqE0XqxQ29")
    
    try:
        print(f"🚀 Sending {order_type} {side} order for {symbol}...")
        res = client.place_order(symbol, side, order_type, quantity, price)
        
        print("\n✅ ORDER SUCCESSFUL")
        print(f"Order ID:     {res.get('orderId')}")
        print(f"Status:       {res.get('status')}")
        print(f"Symbol:       {res.get('symbol')}")
        print(f"Side:         {res.get('side')}")
        print(f"Type:         {res.get('type')}")
        
        # For Market orders, executedQty is what you want to see
        print(f"Qty Ordered:  {res.get('origQty')}")
        
        # If the order filled instantly, these might still be 0 in the initial response
        # but you can check them like this:
        avg_price = res.get('avgPrice') if float(res.get('avgPrice', 0)) > 0 else "Market Price"
        print(f"Avg Price:    {avg_price}")
        print("-" * 30)
        
    except Exception as e:
        print(f"❌ Order Failed: {e}")
              
if __name__ == "__main__":
    app()