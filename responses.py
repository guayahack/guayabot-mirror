import random
import quotes
import re


def filter(message: str) -> list:
    """
    Parses a message to extract a 'addquote' command along with the quote and its author.

    This function uses a regular expression to identify messages that follow the
    pattern of the 'addquote' command, extracting the quote and author. The expected
    pattern is '!addquote "quote" - author'. If the message matches, it returns a list
    containing the command, author, and quote. Otherwise, it returns the original message
    and an empty string.

    Parameters:
        message (str): The text message to be parsed.

    Returns:
        list: A list with the parsed command, author, and quote if the message matches
              the expected pattern. Returns the original message and an empty string if not.

    Example:
        Input: '!addquote "This is a quote" - Author'
        Output: ['addquote', 'Author', 'This is a quote']

        Input: 'Hello world'
        Output: ['Hello world', '']
    """

    # Regular expression pattern to match the addquote command.
    pattern = r'!addquote "(.*?)" - (\w+)'

    # Attempt to match the pattern in the message.
    match = re.match(pattern, message)
    if match:
        # If matched, extract the quote and author.
        quote, author = match.groups()
        return ["addquote", author, quote]
    else:
        # If no match, return the original message and an empty string.
        return [message, ""]


def handle_response(message) -> str:
    p_message = message.lower()

    parts = filter(p_message)
    command = parts[0]

    if command == "!quote":
        quotes_list = quotes.read_yaml_quotes("quotes.yaml")
        return quotes.format_quote(random.choice(quotes_list))

    if command == "addquote":
        quote_list = []
        quote_list.extend([parts[1], parts[2]])
        quotes.add_quote(quote_list, "quotes.yaml")
        return "quote successfully added"
