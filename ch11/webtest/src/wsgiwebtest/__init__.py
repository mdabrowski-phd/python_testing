class Application:
    def __call__(self, environ, start_response):
        start_response(
            '200 OK', 
            [('Content-type', 'test/plain; charset=utf-8')]
        )
        return ["Hello World!".encode("utf-8")]
