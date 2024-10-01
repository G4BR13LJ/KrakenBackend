import krakenex
import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, HttpResponse

#--------------------------------------------------------------
def home(request):
    return HttpResponse("Hello world")


#--------------------------------------------------------------
@require_http_methods(["GET"])
def get_ohlc_data(request):
    api = krakenex.API()
    pair = 'XBTUSD'

    # Get the 'interval' parameter from the request, default to 60 if not provided
    interval = request.GET.get('interval', 60)  # Defaults to 60
    since = 0  # Get the most recent candles

    try:
        # Fetch data from Kraken API
        candles = api.query_public('OHLC', {'pair': pair, 'interval': interval, 'since': since})

        # Check if 'result' exists in the response
        if 'result' not in candles:
            logging.error(f"Unexpected response from Kraken API: {candles}")
            return JsonResponse({'error': 'Error fetching data from Kraken'}, status=500)

        # Check if the pair key exists
        if 'XXBTZUSD' not in candles['result']:
            logging.error(f"Pair data not found in Kraken response: {candles['result']}")
            return JsonResponse({'error': 'Invalid pair data'}, status=500)

        # Process and format the OHLC data
        ohlc_data = [
            {
                'time': int(candle[0]),
                'open': float(candle[1]),
                'high': float(candle[2]),
                'low': float(candle[3]),
                'close': float(candle[4])
            }
            for candle in candles['result']['XXBTZUSD']
        ]

        print(ohlc_data)
        return JsonResponse(ohlc_data, safe=False)

    except Exception as e:
        logging.exception(f"Error occurred while fetching OHLC data: {str(e)}")
        return JsonResponse({'error': 'Internal server error'}, status=500)
