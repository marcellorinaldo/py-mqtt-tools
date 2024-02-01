from termcolor import colored

INPUT_FORMAT = "{name} [default = {default_value}]: "

def get_or_default_str(parameter_name, default):
    user_input = input(INPUT_FORMAT.format(name=parameter_name, default_value=default))
    if user_input == "":
        return default
    return user_input

def get_or_default_int(parameter_name, default):
    user_input = input(INPUT_FORMAT.format(name=parameter_name, default_value=default))
    if user_input == "":
        return int(default)
    return int(user_input)

def get_or_default_bool(parameter_name, default):
    user_input = input(INPUT_FORMAT.format(name=parameter_name, default_value=default))
    if user_input == "":
        return bool(default)
    return bool(user_input)

def print_connection_parameters(host, port, client_id):
    str_to_print = "Connecting to {host}:{port} with client ID {client}".format(host=host, port=port, client=client_id)
    print("\n")
    print(colored(str_to_print, color="light_blue"))
    print("\n")

def print_connection_successful(host, port, result_code):
    print("\n")
    print("Connected to", end=" ")
    print(colored(host + ":" + str(port), color="green"), end=" ")
    print("with result code", end=" ")
    print(colored(str(result_code), color="green"), end=" ")
    print("\n")

def print_message(topic, payload):
    print("Message arrived on topic", end=": '")
    print(colored(topic, color="light_green"), end="'.\n")
    print(colored(payload, color = "light_blue"), end="\n\n")