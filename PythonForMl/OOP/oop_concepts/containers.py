from collections import namedtuple

user_tuple = ('Alice', 'admin',
'alice@email.com')
print(user_tuple[2]) # What is index 2? Hard to

# Namedtuple: Self-documenting dot notation
User = namedtuple('User', ['name', 'role',
'email'])
user_nt = User('Alice', 'admin',
'alice@email.com')
print(user_nt.email) # Clear and readable
