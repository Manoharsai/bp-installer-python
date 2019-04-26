import subprocess


class BluePrismCommands:

    _directory = "C:\\Program Files\\"

    _standard_bp_install_folder = "Blue Prism Limited\\Blue Prism Automate"

    _automate_exe = "\\Automate.exe"
    _automate_c_exe = "\\AutomateC.exe"

    _automate = ""
    _automate_c = ""

    _arguments = [
        (
            "-CreateDBConnection",
            ("--Server", "--Database", "--Connection", "--Username", "--Password"),
            (True, True, False, False, False),
            "{{AUTOMATE}} /setdbserver {{--Server}} /setdbname {{--Database}} /dbconname {{--Connection}} //setdbusername {{--Username}} /setdbpassword {{--Password}}"
        ),
        (
            "-CreateBPConnection",
            ("--Host", "--Port", "--Connection", "--Mode"),
            (True, True, False, False),
            "{{AUTOMATE}} /setbpserver {{-HOST}} {{--PORT}} /dbconname {{--Connection}} /connectionmode {{--Mode}}"
        ),
        (
            "-LaunchBP",
            (),
            (),
            "{{AUTOMATE}}"
        ),
        (
            "-CreateDB",
            ("--Connection"),
            (False),
            "{{AUTOMATE_C}} /createdb"
        )
    ]

    def __init__(self, install_dir=""):

        id = self._directory + self._standard_bp_install_folder

        if install_dir != "":
            id = install_dir

        self._automate = id + self._automate_exe
        self._automate_c = id + self._automate_c_exe

