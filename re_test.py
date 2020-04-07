import re

group_string = "test tost tast toast test12 over test abc  testtt tst . ... w tttest  test over taost toost taast toooaaast " \
            "Mr Smith Mr. Smith Mrrr Smithggg"

re.findall("test", group_string)
group_pattern = r"M(r|s|rs)+\.* [A-Z][a-zA-Z]*"
print(re.match(group_pattern, group_string))  # does for the entire string
print(re.fullmatch(group_pattern, group_string))

test_string = 'the capital of Azerbaijan is Baku'
print(re.match(r'^the', test_string))

pattern = r'[A-Z]\w+'
re.split(r'\s', 'hello how are you')
re.findall(pattern, test_string)

re.sub(pattern, 'Mexico', test_string)

re.search(pattern, test_string)


# compiling regular expressions
rex = re.compile(pattern)
rex.search(test_string)