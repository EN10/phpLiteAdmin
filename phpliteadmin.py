#!/usr/local/bin/python3

import argparse
import os
import re
import subprocess
import sys
import shutil
import termcolor
import tempfile


DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8082
PHP_FILE = f'/opt/cs50/phpliteadmin/share/index.php'
PHP_THEME = f'/opt/cs50/phpliteadmin/share/phpliteadmin.css'
EXECUTABLE = '/usr/bin/php'


def main():

    args = parse_args(sys.argv[1:])

    if not os.path.isfile(args.path):
        sys.exit("Database not found, exiting...")

    # Preparing files
    tempDir = tempfile.mkdtemp()
    shutil.copy(PHP_FILE, tempDir)
    shutil.copy(PHP_THEME, tempDir)

    # Update database path and name in phpliteadmin
    with open(f'{tempDir}/{os.path.basename(PHP_FILE)}', 'r+') as file:
        content = file.read()
        content = re.sub('ENV_DATABASE_PATH', os.path.abspath(args.path), content)
        content = re.sub('ENV_DATABASE_NAME', os.path.basename(args.path), content)
        file.seek(0)
        file.write(content)
        file.truncate()

    # Construct php command
    command = [EXECUTABLE]
    command.extend(['-S', f'{DEFAULT_HOST}:{DEFAULT_PORT}', '-t', tempDir])
    os.system(f'fuser -k {DEFAULT_PORT}/tcp') # Kill any process listing on the specified port
    display_codespace_url(DEFAULT_PORT)

    # Start php server
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path'
    )
    return parser.parse_args(args)


def display_codespace_url(port):
    codespace_name = os.getenv('CODESPACE_NAME')
    if (codespace_name is not None):
        local_address = f'https://{codespace_name}-{port}.preview.app.github.dev/'
        msg = f"\nphpLiteAdmin running on {local_address}\n"
        print(termcolor.colored(msg, 'green'))


if __name__ == '__main__':
    main()
