#!/usr/bin/env python3
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from project import main

if __name__ == '__main__':
    port = 8080
    server = make_server('0.0.0.0', port, main())
    print('will now serve on port ', port)
    server.serve_forever()
