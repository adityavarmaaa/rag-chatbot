# utils/mcp.py
def create_message(sender, receiver, msg_type, payload, trace_id):
    return {
        "sender": sender,
        "receiver": receiver,
        "type": msg_type,
        "trace_id": trace_id,
        "payload": payload
    }
