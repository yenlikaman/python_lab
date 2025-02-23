import re

def match_a_followed_by_b(string):
    return bool(re.fullmatch(r'a*b*', string))

def match_a_followed_by_two_three_b(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

def find_sequences_with_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

def find_uppercase_followed_by_lowercase(string):
    return re.findall(r'[A-Z][a-z]+', string)

def match_a_followed_by_anything_ending_b(string):
    return bool(re.fullmatch(r'a.*b', string))

def replace_spaces_commas_dots(string):
    return re.sub(r'[ ,.]', ':', string)

def snake_to_camel(string):
    return ''.join(word.title() if i != 0 else word for i, word in enumerate(string.split('_')))

def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

def insert_spaces_at_capitals(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

def camel_to_snake(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

# Example usage:
print(match_a_followed_by_b("abbb"))
print(match_a_followed_by_two_three_b("abb"))
print(find_sequences_with_underscore("this_is_a_test example"))
print(find_uppercase_followed_by_lowercase("HelloWorld Test"))
print(match_a_followed_by_anything_ending_b("axxxb"))
print(replace_spaces_commas_dots("Hello, world. This is a test"))
print(snake_to_camel("hello_world_example"))
print(split_at_uppercase("HelloWorldTest"))
print(insert_spaces_at_capitals("HelloWorldTest"))
print(camel_to_snake("HelloWorldTest"))
