import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
import config

def test_credentials():
    print(f"Testing with API KEY: {config.BINANCE_API_KEY[:5]}...{config.BINANCE_API_KEY[-5:]}")
    print(f"Testing with SECRET KEY: {config.BINANCE_SECRET_KEY[:5]}...{config.BINANCE_SECRET_KEY[-5:]}")
    
    # Try with tld='us' as in the code
    print("\n--- Trying with tld='us' ---")
    client_us = Client(config.BINANCE_API_KEY, config.BINANCE_SECRET_KEY, tld='us')
    try:
        account = client_us.get_account()
        print("Success with tld='us'!")
    except BinanceAPIException as e:
        print(f"BinanceAPIException (us): {e}")
    except Exception as e:
        print(f"Exception (us): {e}")

    # Try with tld=None (default, binance.com)
    print("\n--- Trying with tld=None (binance.com) ---")
    client_com = Client(config.BINANCE_API_KEY, config.BINANCE_SECRET_KEY)
    try:
        account = client_com.get_account()
        print("Success with binance.com!")
    except BinanceAPIException as e:
        print(f"BinanceAPIException (com): {e}")
    except Exception as e:
        print(f"Exception (com): {e}")

if __name__ == "__main__":
    test_credentials()
