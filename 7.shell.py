import subprocess


def exec_command(command):
    try:
        result = subprocess.run(command.split())
    except Exception as e:
        print(f"Command is not found: {command} with error {e}")


def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        elif command == "help":
            print("Shell written in Python")
        else:
            exec_command(command)


main()

