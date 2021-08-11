# -*- coding: utf-8 -*-
# @Time  : 2021/7/24 10:14
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : RPCServer.py
import os
from asyncio import get_event_loop
from typing import Optional

from tzrpc.base import tzrpcBase
from tzrpc.exceptions.exceptions import TZRPCException


class TZRPC(tzrpcBase):
    def __init__(self, name):
        super().__init__(name=name)

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
            unix: Optional[str] = None,
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
                serve_single(server_settings)
            else:
                serve_multiple(server_settings, workers)
        except BaseException:
            error_logger.exception(
                "Experienced exception while trying to serve"
            )
            raise
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