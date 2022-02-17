import socket


def decode_rtp_packet(packet_bytes):  # 解包单个RTP报文
    packet_vars = {}
    byte1 = packet_bytes[0:2]
    byte1 = int(byte1, 16)
    byte1 = format(byte1, 'b')
    packet_vars['version'] = int(byte1[0:2], 2)
    packet_vars['padding'] = int(byte1[2:3])
    packet_vars['extension'] = int(byte1[3:4])
    packet_vars['csi_count'] = int(byte1[4:8], 2)
    byte2 = packet_bytes[2:4]
    byte2 = int(byte2, 16)
    byte2 = format(byte2, 'b').zfill(8)
    packet_vars['marker'] = int(byte2[0:1])
    packet_vars['payload_type'] = int(byte2[1:8], 2)
    packet_vars['sequence_number'] = int(str(packet_bytes[4:8]), 16)
    packet_vars['timestamp'] = int(str(packet_bytes[8:16]), 16)
    packet_vars['ssrc'] = int(str(packet_bytes[16:24]), 16)
    packet_vars['payload'] = str(packet_bytes[24:])
    return packet_vars


if __name__ == "__main__":
    tcp_client = socket.socket()
    tcp_client.connect(('127.0.0.1', 62610))
    while True:
        buffer = tcp_client.recv(1500)
        if buffer:
            print(buffer)
        else:
            tcp_client.close()
            break
