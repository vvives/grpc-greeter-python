"""
Copyright (c) 2021 Víctor Vives - All rights reserved.

Licensed under the MIT License. 
See LICENSE file in the project root for full license information.
"""

import sys

sys.path.insert(0, './protos')

import asyncio
import logging

import grpc
import greeter_pb2
import greeter_pb2_grpc

class Greeter(greeter_pb2_grpc.GreeterServicer):
    """The greeter service class.
    """

    async def SayHello(
        self, request: greeter_pb2.HelloRequest,
        context: grpc.aio.ServicerContext) -> greeter_pb2.HelloReply:
        """Procedure that greets a user.
        """

        logging.info('Request received from %s!' % request.name)

        return greeter_pb2.HelloReply(message='Hello, %s!' % request.name)


async def serve() -> None:
    """Procedure that serves the server.
    """
    server = grpc.aio.server()
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    listen_addr = '[::]:5000'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
