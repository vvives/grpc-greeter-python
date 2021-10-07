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

async def run() -> None:
    """Procedure that runs the client.
    """

    async with grpc.aio.insecure_channel('localhost:5000') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(greeter_pb2.HelloRequest(name=sys.argv[1]))
    print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
