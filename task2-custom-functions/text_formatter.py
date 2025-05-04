def format_text(text: str, prefix: str = "", suffix: str = "", capitalize: bool = False, max_length: int = None) -> str:
    if not isinstance(text, str):
        raise TypeError("The 'text' parameter must be a string.")
    if not isinstance(prefix, str):
        raise TypeError("The 'prefix' parameter must be a string.")
    if not isinstance(suffix, str):
        raise TypeError("The 'suffix' parameter must be a string.")
    if not isinstance(capitalize, bool):
        raise TypeError("The 'capitalize' parameter must be a boolean.")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' parameter must be an integer.")
        if max_length < 0:
            raise ValueError("The 'max_length' parameter must be greater than or equal to 0.")

    if capitalize:
        text = text.capitalize()

    formatted_text = f"{prefix}{text}{suffix}"

    if max_length is not None and len(formatted_text) > max_length:
        formatted_text = formatted_text[:max_length]

    return formatted_text


if __name__ == "__main__":
    try:
        print(format_text("hello world", prefix=">>> ", suffix=" <<<", capitalize=True))
        print(format_text("hello world", max_length=10))
        print(format_text("hello world", prefix=">> ", suffix=" <<", capitalize=False, max_length=15))
    except Exception as e:
        print(f"Error: {e}")
