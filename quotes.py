from yaml import safe_load, dump

def read_yaml_quotes(yaml_file:str) -> list:
    """
    Reads a YAML file containing quotes and authors, and returns a list of quote-author pairs.

    Args:
        yaml_file (str): The path to the YAML file containing quotes and authors.

    Returns:
        quote_list (list): A list of lists, where each inner list contains an author's name and their associated quote.

    This function reads a YAML file and extracts quote-author pairs from the 'quotes' section
    of the YAML content. It returns the data in the form of a list, where each inner list
    contains two elements: the author's name and their corresponding quote.
    """
    quote_list = []
    with open(yaml_file, 'r') as file:
        data = safe_load(file)
        
        quotes = data.get("quotes", {})
        
        for author, quote in quotes.items():
            quote_list.append([author, quote])
    
    return quote_list

def add_quote(quote_list:list, yaml_file:str) -> None:
    """
    Appends a new quote and author to an existing YAML file in a specific format.

    Args:
        quote_list (list): A list containing two elements: the author's name and the quote text.
        yaml_file (str): The path to the YAML file to which the quote should be appended.

    This function appends a new quote and its author to the specified YAML file. It reads the existing
    YAML content, extracts the 'quotes' section, and adds the new quote to the 'quotes' dictionary.
    The YAML file is updated with the new quote, following a specific format.
    """
    
    author, quote = quote_list
    with open(yaml_file, 'r') as file:
        data = safe_load(file)

    quotes = data.get("quotes", {})

    quotes[author] = quote
    data["quotes"] = quotes

    with open(yaml_file, 'w') as file:
        dump(data, file, default_flow_style=False, allow_unicode=True)

def format_quote(quote_list:list) -> str:
    """
    Formats a quote and its author's name with an aesthetically pleasing font style.

    Args:
        quote_list (list): A dictionary where the author's name is the key, and the
            associated value is the quote text.

    Returns:
        formatted_quote (str): A formatted representation of the quote with the author, suitable for display.

    This function takes a dictionary containing the author's name as the key and their
    associated quote text as the value. It combines them into a well-designed
    representation, making it visually appealing for presentation or display purposes.

    Example:
    \>>> quotes = ["John Lennon", "Life is what happens when you're busy making other plans."}]

    "Life is what happens when you're busy making other plans."
    - John Lennon
    """

    return f'`"{quote_list[1]}"\n - {quote_list[0]}`'

if __name__ == "__main__":
    #testing shit
    import random
    add_quote(["mcveight", "dafsdgasd"], "quotes.yaml")
    quotes = read_yaml_quotes("quotes.yaml")

    print(format_quote(quotes[4]))

