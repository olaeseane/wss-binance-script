from websocket import create_connection
import json


# Copy the web brower header and input as a dictionary
headers = json.dumps({
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'Upgrade',
    'Host': 'stream.binance.com',
    'Origin': 'https://www.binance.com',
    'Pragma': 'no-cache',
    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
    'Sec-WebSocket-Key': 'phdrS1DuiaBXmqEKyk4eYg==',
    'Sec-WebSocket-Version': '13',
    'Upgrade': 'websocket',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
})


# Launch the connection to the server.
ws = create_connection(
    'wss://stream.binance.com/stream', headers=headers)

# Perform the handshake.
ws.send(json.dumps({'method': 'SUBSCRIBE', 'params': [
        '!miniTicker@arr@3000ms', 'btcusdt@aggTrade', 'btcusdt@depth', 'btcusdt@kline_1d'], 'id': 3}))

# Printing all the result
while True:
    try:
        result = ws.recv()
        print(result)
    except Exception as e:
        print(e)
        break
