# -*- coding: utf-8 -*-
# @Time  : 2021/7/24 10:14
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : RPCServer.py
import logging
import os
import traceback
from asyncio import get_event_loop
from concurrent import futures
from typing import Optional

import grpc

from tzrpc.decorator.rpc import servicers
from tzrpc.exceptions.exceptions import TZRPCException
from tzrpc.proto.py.Server_pb2_grpc import add_toObjectServicer_to_server
from tzrpc.server.base import tzrpcBase
from tzrpc.utils.constant import MAX_MESSAGE_LENGTH, MAX_METADATA_SIZE
from tzrpc.utils.logger import get_logger

logger = get_logger(to_std=True, stdout_level="INFO", save_log_file=False)


class TZRPC_Server(tzrpcBase):
    def __init__(self, name, debug=False):
        if debug:
            get_logger(
                to_std=True,
                stdout_level="DEBUG" if debug else "INFO",
                save_log_file=False,
            ).setLevel(logging.DEBUG)

        super().__init__(name)

    @property
    def loop(self):
        """
        Synonymous with asyncio.get_event_loop().
        .. note::
            Only supported when using the `app.run` method.
        """
        if not self.is_running:
            raise TZRPCException(
                "Loop can only be retrieved after the app has started "
                "running. Not supported with `create_server` function"
            )
        return get_event_loop()

    def run(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        debug: bool = False,
        workers: int = 1,
        loop: None = None,
    ) -> None:
        """
        Run the HTTP Server and listen until keyboard interrupt or term
        signal. On termination, drain connections before closing.
        :param host: Address to host on
        :type host: str
        :param port: Port to host on
        :type port: int
        :param debug: Enables debug output (slows server)
        :type debug: bool
        :param workers: Number of processes received before it is respected
        :type workers: int
        :return: Nothing
        """
        if loop is not None:
            raise TypeError(
                "loop is not a valid argument. To use an existing loop, "
                "change to create_server().\nSee more: "
                "https://sanic.readthedocs.io/en/latest/sanic/deploying.html"
                "#asynchronous-support"
            )

        host, port = host or "127.0.0.1", port or 8000
        get_logger(
            to_std=True, stdout_level="DEBUG" if debug else "INFO", save_log_file=False
        )
        try:
            self.is_running = True
            self.is_stopping = False
            if workers > 1 and os.name != "posix":
                logger.warn(
                    f"Multiprocessing is currently not supported on {os.name},"
                    " using workers=1 instead"
                )
                workers = 1
            if workers == 1:
                logger.info(f"Tzrpc Server now listening {host}:{port}.")
                server = grpc.server(
                    futures.ThreadPoolExecutor(),
                    options=[
                        ("grpc.max_send_message_length", MAX_MESSAGE_LENGTH),
                        ("grpc.max_receive_message_length", MAX_MESSAGE_LENGTH),
                        ("grpc.max_metadata_size", MAX_METADATA_SIZE),
                    ],
                )
                for servicer in servicers:
                    add_toObjectServicer_to_server(
                        servicer, server, servicer.task.__name__
                    )

                server.add_insecure_port(f"{host}:{port}")
                server.start()
                logger.info("Tzrpc Server started.")
                server.wait_for_termination()
            else:
                # TODO
                raise ValueError(
                    "it so sorry for mutil-process is not available, please set work = 1"
                )
        except BaseException as base_exc:
            logger.info(base_exc)
            traceback.print_exc()
        finally:
            self.is_running = False
        logger.info("Server Stopped")

    def stop(self):
        """
        This kills the tzrpc
        """
        if not self.is_stopping:
            self.is_stopping = True
            get_event_loop().stop()
