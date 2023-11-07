import random
import quotes
import re

def filter(message:str) -> list:
    """
    Filters a message to extract a command, author, and a quote.

    Args:
        message (str): The input message to be filtered.

    Returns:
        parts (list): A list containing the extracted information.
              - If the message matches the expected pattern:
                [command (str), author (str), quote (str)]
              - If the message does not match the pattern:
                [message (str), " " (str)]
    
    The function uses a regular expression pattern to parse the input message and extracts
    a command, an optional author, and a quoted text. If the pattern is not matched,
    it returns the original message with an empty string as the author.

    Example:
    >>> filter('!addquote John "This is a quote."')
    ['addquote', 'John', 'This is a quote.']

    >>> filter('Hello, world!')
    ['Hello, world!', ' ']
    """    
    # Define the regex pattern
    pattern = r'!(addquote|showquote)(?: (\w+))? "(.*?)"'

    match = re.match(pattern, message)
    if match:
        command, author, quote = match.groups()
        return command, author, quote
    else:
        return message, " "

def handle_response(message) -> str:
    p_message = message.lower()

    parts = filter(p_message)
    command = parts[0]

    if command == '!quote':
        quotes_list = quotes.read_yaml_quotes("quotes.yaml")
        return quotes.format_quote(random.choice(quotes_list))

    if command == 'addquote':
        quote_list = []
        quote_list.extend([parts[1], parts[2]])
        quotes.add_quote(quote_list, "quotes.yaml")
        return "quote successfully added"