import subprocess
import sys

def test_script_output(capfd):
    # Run the script file under a new process using the same python interpreter
    subprocess.run([sys.executable, '../script.py'])
    # Capture the process output
    captured = capfd.readouterr()
    # Assert that the output is correct
    assert captured.out == "Hello, World\r\n"
