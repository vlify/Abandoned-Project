from socketIO_client import SocketIO

from conf import hosts, port

client = SocketIO(hosts, port=port, wait_for_connection=True)
