import funcs_for_diffy_hellman_key_exchange as f
import socket
socket = f.connect_to_server_socket()
f.send_msg_with_diffy_hellman_key_exchange(
    socket, 'msg from client.\nhello world.')
