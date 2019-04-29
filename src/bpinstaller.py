import os
import json


class Schematic:

    @classmethod
    def get(cls, path):

        f = open(path)
        contents = f.read()
        f.close()

        if os.path.splitext(path) == ".json":
            return json.loads(contents)
        elif os.path.splitext(path) == ".xml":
            return
        raise Exception("Unknown file type.")


class BluePrismCommands:

    _install_directory = "C:\\Program Files\\Blue Prism Limited\\Blue Prism Automate"
    _delimiter = "||"
    _commands = [
        (
            "-CreateDBConnection",
            [
                ("--InstallDirectory", True),
                ("--Server", True),
                ("--Database", True),
                ("--Connection", False),
                ("--Username", False),
                ("--Password", False)

            ],
            [
                "{{--InstallDirectory}}\\Automate.exe",
                "/setdbserver {{--Server}}",
                "/setdbname {{--Database}}",
                "/dbconname {{--Connection}}",
                "/setdbusername {{--Username}}",
                "/setdbpassword {{--Password}}"
            ]
        ),
        (
            "-CreateBPConnection",
            [
                ("--InstallDirectory", True),
                ("--Host", True),
                ("--Port", True),
                ("--Connection", False),
                ("--Mode", False)
            ],
            [
                "{{--InstallDirectory}}\\Automate.exe",
                "/setbpserver {{--Host}} {{--Port}}",
                "/dbconname {{--Connection}}",
                "/connectionmode {{--Mode}}"
            ]
        ),
        (
            "-LaunchBP",
            [
                ("--InstallDirectory", True)
            ],
            [
                "{{--InstallDirectory}}\\Automate.exe"
            ]
        ),
        (
            "-CreateDB",
            [
                ("--InstallDirectory", True),
                ("--Connection", False)
            ],
            [
                "{{--InstallDirectory}}\\AutomateC.exe",
                "/createdb",
                "/dbconname {{--Connection}}"
            ]

        )
    ]

    def __init__(self, install_dir=""):

        if install_dir != "":
            self._install_directory = install_dir

    def command(self, command, arguments):

        comm = self._get_command(command)
        args = self._add_install_directory_key(arguments)
        arr = self._replace_arguments_in_command(comm[2], args)
        if self._missing_mandatory_arguments(arr, comm[1]):
            raise Exception("Missing mandatory argument.")
        return self._remove_placeholder_arguments(arr)

    def _get_command(self, comm):

        for c in self._commands:
            if c[0] == comm:
                return c

        raise Exception("Unable to locate command.")

    def _add_install_directory_key(self, args):

        for a in args:
            if a[0] == "--InstallDirectory":
                return args

        return [("--InstallDirectory", self._install_directory)] + args

    def _replace_arguments_in_command(self, arr, args):

        string = self._delimiter.join(arr)

        for a in args:
            string = string.replace("{{"+a[0]+"}}", a[1])

        return string.split(self._delimiter)

    @staticmethod
    def _missing_mandatory_arguments(arr, args):

        mandatory = []

        for a in args:
            if a[1]:
                mandatory += [a[0]]

        for m in mandatory:
            if m in "||".join(arr):
                return True

        return False

    @staticmethod
    def _remove_placeholder_arguments(arr):

        command = []

        for i in range(len(arr)):
            if not (("{{" in arr[i]) and ("}}" in arr[i])):
                command += [arr[i]]

        return command
