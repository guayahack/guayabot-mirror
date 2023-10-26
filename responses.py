import random
import quotes

def split_string_with_quotes(input_string):
    parts = []  # Initialize an empty list to store the segments
    inside_quotes = False  # Track if we are currently inside double quotes
    current_part = ''  # Initialize the current part as an empty string

    for char in input_string:
        if char == ' ' and not inside_quotes:
            if current_part:  # If the current part is not empty, add it to the list
                parts.append(current_part)
            current_part = ''  # Reset the current part
        else:
            current_part += char
            if char == '"':
                inside_quotes = not inside_quotes  # Toggle the inside_quotes flag

    if current_part:
        parts.append(current_part)  # Append the last part after the loop

    return parts

def handle_response(message) -> str:
    p_message = message.lower()

    parts = split_string_with_quotes(p_message)
    command = parts[0]

    if command == '!quote':
        quotes_list = quotes.read_yaml_quotes("quotes.yaml")
        return quotes.format_quote(random.choice(quotes_list))

    if command == '!addquote':
        #for now please provide author quote only
        #command should be !addquote author "quote"
        quote_list = []
        quote_list.extend([parts[1], parts[2]])
        quotes.add_quote(quote_list, "quotes.yaml")
        return "quote successfully added"