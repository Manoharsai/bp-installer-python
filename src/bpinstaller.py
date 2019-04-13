import subprocess
import json

test_schematic = """
{
    "connections": [
        {
            "server" : "SQLExpress",
            "database" : "Production",
            "username" : "",
            "password: : "",
            "connection" : "",
            "create" : "True"
        }
    ]
}
"""


class SchematicInterface:

    @staticmethod
    def decode_schematic(schematic):
        return json.loads(schematic)


class BluePrismInterface:

    bpInstallDir = "C:\\Program Files\\Blue Prism Limited\\Blue Prism Automate"
    automate = bpInstallDir + "\\Automate.exe"
    automateC = bpInstallDir + "\\AutomateC.exe"

    @classmethod
    def set_current_connection(cls, connection_name):
        a = [cls.automate, "/dbconname", connection_name]
        print(a)

    @classmethod
    def create_db_connection(cls, database_server_name, database_name, username="", password="", connection_name="", create=False):
        a = [cls.automate, "/setdbserver", database_server_name, "/setdbname", database_name]

        if len(username) != 0 and len(password) != 0:
            a += ["/setdbusername", username, "/setdbpassword", password]
        elif len(username) != 0:
            raise Exception("A Username was not supplied during Database Connection creation.")
        elif len(password) != 0:
            raise Exception("A Password was not supplied during Database Connection creation.")

        if len(connection_name) > 0:
            a += ["/dbconname", connection_name]

        subprocess.call(a)

    @classmethod
    def create_bp_connection(cls, host, port, connection_name="", connection_mode=""):
        a = [cls.automate, "/setbpserver", host, port]

        if len(connection_name) > 0:
            a += ["/dbconname", connection_name]

        if len(connection_mode) > 0:
            if connection_mode.isdigit():
                if int(connection_mode) < 0 or int(connection_mode) > 5:
                    raise Exception("The connection mode must be between 0 and 5.")
            else:
                raise Exception("The Connection Mode supplied must be an integer.")

            a += ["/connectionmode", connection_mode]

        subprocess.call(a)

    @classmethod
    def open(cls):
        subprocess.call([cls.automate])

    @classmethod
    def setup(cls, bp_install_dir):
        cls.bpInstallDir = bp_install_dir
        cls.automate = bp_install_dir + "\\Automate.exe"
        cls.automateC = bp_install_dir + "\\AutomateC.exe"

BluePrismInterface().set_current_connection("test")