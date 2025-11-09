def shutdown(response):
    if response.lower() == "yes":
        print("Shutting down...")
    elif response.lower() == "no":
        print("Abort shutdown.")
    else:
        print("Sorry.")

# Example usage
user_input = input("Do you want to shut down? (Yes/No): ")
shutdown(user_input)
