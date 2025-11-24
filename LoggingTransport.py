import httpx
import json

class LoggingTransport(httpx.BaseTransport):
    def __init__(self, transport):
        self._transport = transport

    def handle_request(self, request):
        print("===================== OUTGOING REQUEST =====================")
        print("URL:", request.url)
        print("Method:", request.method)
        print("Headers:", dict(request.headers))

        if request.content:
            try:
                print("Body (JSON parsed):")
                print(json.dumps(json.loads(request.content), indent=2))
                print("Body (raw):")
                print(request.content)
            except Exception:
                print("Body (raw):")
                print(request.content)

        print("============================================================")
        
        return self._transport.handle_request(request)
