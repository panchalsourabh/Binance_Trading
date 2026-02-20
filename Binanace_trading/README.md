# Binance Futures Testnet Trading Bot

## Overview

This project is a simplified Python trading bot that simulates placing MARKET and LIMIT orders on Binance Futures Testnet.

The bot is built with a clean and reusable structure, includes logging, and accepts user input via command line.

## Features

- Supports BUY and SELL orders
- Supports MARKET and LIMIT order types
- Command Line Interface (CLI) using argparse
- Logs order requests and responses to a log file
- Error handling and structured code design

## Project Structure

binance_client.py – Handles order placement logic

cli_app.py – Handles CLI input and executes orders

binance_orders.log – Stores log of order requests and responses

requirements.txt – Project dependencies

README.md – Project documentation

## Requirements

Python 3.14.2 installed

## How to Run

Open Command Prompt in the project folder.

### Example: MARKET Order

python cli_app.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.002

### Example: LIMIT Order

python cli_app.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.002 --price 95000

## Output

 Sending MARKET BUY order for BTCUSDT...

✅ ORDER SUCCESSFUL
Order ID:    ********
Status:       NEW
Symbol:       BTCUSDT
Side:         BUY
Type:         MARKET
Qty Ordered:  0.002
Avg Price:    Market Price
------------------------------

## Log File

All order activity is saved in:

binance_orders.log

This includes:

- Order request details
- Order response details
- Errors if any

## Assumptions

This project simulates Binance Futures Testnet order responses for demonstration and testing purposes.

## Author

Sourabh Panchal.