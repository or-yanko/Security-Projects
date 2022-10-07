import funcs_for_diffy_hellman_key_exchange as f
socket, address = f.socket_after_connection_listen_as_a_server(
    f.get_my_ip_address())
print(f.recive_msg_with_diffy_hellman_key_exchange_and_hash_confirmation(socket))
