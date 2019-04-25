import subprocess


class BluePrismInterface:

    bp_install_dir = "C:\\Program Files\\Blue Prism Limited\\Blue Prism Automate"

    @classmethod
    def create_db_server_connection(cls, database_server_name, database_name, username="", password="", connection_name=""):
        a = [cls.automate(), "/setdbserver", database_server_name, "/setdbname", database_name]

        if len(connection_name) > 0:
            a += ["/dbconname", connection_name]

        if len(username) > 0 or len(password) > 0:
            if (len(username) > 0) != (len(password) > 0):
                raise Exception("A username AND password must be supplied if an SQL database connection is to be used.")
            a += ["/setdbusername", username, "/setdbpassword", password]

        subprocess.call(a)

    @classmethod
    def create_db(cls, password="", connection_name=""):
        a = [cls.automate_c(), "/createdb", password]

        if len(connection_name) > 0:
            a += ["/dbconname", connection_name]

        subprocess.call(a)

    @classmethod
    def create_bp_server_connection(cls, host, port, connection_name="", connection_mode=""):
        a = [cls.automate(), "/setbpserver", host, port]

        if len(connection_name) > 0:
            a += ["/dbconname", connection_name]

        if len(connection_mode) > 0:
            if connection_mode.isdigit() or (int(connection_mode) < 0 or int(connection_mode) > 5):
                raise Exception("The Connection Mode must be between 0 and 5.")
            elif not connection_mode.isdigit():
                raise Exception("The Connection Mode supplied must be an integer.")

            a += ["/connectionmode", connection_mode]

        subprocess.call(a)

    @classmethod
    def set_bp_install_dir(cls, install_dir):
        cls.bp_install_dir = install_dir

    @classmethod
    def automate(cls, run=False):
        path = cls.bp_install_dir + "\\Automate.exe"

        if run:
            subprocess.call([path])

        return path

    @classmethod
    def automate_c(cls, run=False):
        path = cls.bp_install_dir + "\\AutomateC.exe"

        if run:
            subprocess.call([path])

        return path


BluePrismInterface.automate(True)
