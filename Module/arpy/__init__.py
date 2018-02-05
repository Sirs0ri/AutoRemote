# Todo: loading process
#   -> Load Plugin (AutoRemote.__init__())
#   -> Start Plugin (AutoRemote.__start__())
# 		-> Run Server (MyServer(RequestHandler, port).Start())
# 		-> Update gDrive permissions (GoogleDrive(...).Authorize()
#
# Todo: registration process
#   -> RegisterEventGHost.__call__()
# 		-> RequestSendRegistration(...).Send()
#
# Todo: send messages
#   -> text
#   -> ??
#
# Todo: Manage Devices

# standard library imports
import logging
import socket

# related third party imports
import requests

# application specific imports

__version__ = "0.1.0a1"

class ARServer:

    def __init__(self, port=1818, server_name="ArPy", file_folder="", username="", password=""):
        # load server
        self.running = False
        self.devices = []
        self.port = port
        self.name = server_name
        self.file_folder = file_folder
        self.username = username
        self.password = password
        self.logger = logging.getLogger("{}.server_{}".format(__name__, server_name))
        # get private and public IP
        self.public_ip = self._get_public_ip()
        self.local_ip = self._get_local_ip()

    def _get_public_ip(self):
        try:
            response = requests.get("https://httpbin.org/ip", timeout=1)
            if response.status_code == 200:
                result = response.json()
                if "origin" in result:
                    self.logger.debug("My public IP is %s", result["origin"])
                    return result["origin"]
                else:
                    self.logger.error("Faulty data:\n%s", result)
            else:
                self.logger.error("Wrong response code: %s",
                                  response.status_code)
        except (requests.exceptions.ConnectionError,
                requests.exceptions.SSLError,
                requests.exceptions.Timeout) as e:
            self.logger.error("Couldn't get my public IP: %s", e)

    def _get_local_ip(self):
        local_ip = ""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("google.com", 80))
            local_ip = s.getsockname()[0]
            self.logger.debug("My local IP is %s", local_ip)
        except socket.error as e:
            self.logger.error("Couldn't get my local IP: %s", e)
        finally:
            s.close()
            return local_ip

    def start(self):
        # Start server
        # register on devices
        return

    def add_device(self):
        return

    def _save_devices(self):
        return

    def _load_devices(self):
        return


class ARDevice:

    def __init__(self):
        # set up address, password, name?
        return

    def register(self):
        return

    def send_message(self):
        return

    def send_notification(self):
        return


def _set_up_logging():
    global LOGGER
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    nice_formatter = logging.Formatter(u"%(asctime)-8s,%(msecs)-3d %(levelname)-8s %(name)-12s\t%(message)s", "%X")
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(nice_formatter)
    root.addHandler(console_handler)



def set_up_server():
    LOGGER.debug("hello")


_set_up_logging()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
LOGGER.debug("Logging set up successfully.")

# if __name__ == "__main__":
#     _set_up_logging()
#     server = ARServer()