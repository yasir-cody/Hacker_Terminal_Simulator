print("\n<--- HACKER TERMINAL READY --->")


while True:
    given_command = input("\nCommand: ")

    if given_command == "scan":
        print("Simulated scan started...")
    elif given_command == "status":
        print("System status: Online")
    elif given_command == "exit":
        print("Terminal session closed.")
        break
    else:
        print("Unknown command.")
