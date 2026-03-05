import random
import requests

def generate_random_number(min: int = 1, max: int = 100) -> int:
    return random.randint(min, max)

def generate_random_number_from_api() -> int:
    response = requests.get("https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new")
    if response.status_code == 200:
        return int(response.text.strip())
    else:
        raise Exception("Failed to fetch random number from API")

def generate_random_string(length : int) -> str:
    """
    Generate a random string of the specified length.

    Args:
        length (int): The length of the string to generate.

    Returns:
        str: A random string of the specified length.

    Example:
        >>> generate_random_string(5)
        'abcde'
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # Tuple comprehension is nice.
    return ''.join(random.choice(letters) for _ in range(length))


if __name__ == "__main__":
    # print(generate_random_number())
    print(generate_random_number_from_api())
    # print(generate_random_string(10))
