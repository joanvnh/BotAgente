def application(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    method = environ.get("REQUEST_METHOD", "GET")
    
    if path == "/":
        response = "Bot active"
    elif path == "/api/webhook":
        response = "Webhook endpoint"
    elif path == "/api/send_message":
        response = "Send message endpoint"
    else:
        response = "Not found"
    
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [response.encode()]