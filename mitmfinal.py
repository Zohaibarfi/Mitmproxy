from mitmproxy import http
from mitmproxy import ctx

class LogServerConnections:
    def __init__(self):
        self.connections = set()
        self.output_file = "/Users/macos/zohaib/1.txt"  # Specify the output file path here

        # Open the file in write mode to clear previous contents
        with open(self.output_file, "w") as f:
            f.write("")

    def response(self, flow: http.HTTPFlow) -> None:
        # Log successful server connection details
        self.log_connection(flow, "success", "")

    def error(self, flow: http.HTTPFlow) -> None:
        # Log failed server connection details
        error_message = self.get_error_reason(flow)
        self.log_connection(flow, "failure", error_message)

    def serverconnect(self, conn):
        # Capture server connect events
        if conn.error:
            error_message = conn.error.msg
            self.log_connection_event(conn, "failure", error_message)
        else:
            self.log_connection_event(conn, "success", "")

    def serverdisconnect(self, conn):
        # Capture server disconnect events
        if conn.error:
            error_message = conn.error.msg
            self.log_connection_event(conn, "failure", error_message)

    def get_error_reason(self, flow: http.HTTPFlow) -> str:
        if flow.error:
            return flow.error.msg
        if flow.response and flow.response.status_code >= 400:
            return f"HTTP {flow.response.status_code} {flow.response.reason}"
        return "Unknown error"

    def log_connection(self, flow: http.HTTPFlow, status: str, reason: str) -> None:
        server_conn = flow.server_conn
        domain = server_conn.address[0] if server_conn.address else "unknown"
        ip = server_conn.ip_address[0] if server_conn.ip_address else "unknown"
        url = flow.request.url
        connection_info = (domain, ip, url, status, reason)

        # Log unique connections based on domain, IP, and URL
        if connection_info not in self.connections:
            self.connections.add(connection_info)
            log_entry = f"Domain: {domain}, IP: {ip}, URL: {url}, Status: {status}, Reason: {reason}\n"
            ctx.log.info(log_entry)

            # Append the log entry to the output file
            with open(self.output_file, "a") as f:
                f.write(log_entry)

    def log_connection_event(self, conn, status: str, reason: str) -> None:
        domain = conn.address[0] if conn.address else "unknown"
        ip = conn.ip_address[0] if conn.ip_address else "unknown"
        url = conn.metadata.get("url", "unknown")
        connection_info = (domain, ip, url, status, reason)

        # Log unique connections based on domain, IP, and URL
        if connection_info not in self.connections:
            self.connections.add(connection_info)
            log_entry = f"Domain: {domain}, IP: {ip}, URL: {url}, Status: {status}, Reason: {reason}\n"
            ctx.log.info(log_entry)

            # Append the log entry to the output file
            with open(self.output_file, "a") as f:
                f.write(log_entry)

addons = [
    LogServerConnections()
]
