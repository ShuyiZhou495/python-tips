# padding of string

a = 15
f"{a:04}" # '0015' <== 0 padding
f"{a:4}" # '  15' <== space padding

# precision of float number

a = 1.1111324354432634
f"{a:.5f}" #'1.11113' <== give 5 digits after the point
f"{a:.5g}" #'1.1111' <== give 5 significant digits

# lowercase and uppercase

a = "hello kitty"
a.upper() # 'HELLO KITTY'
a.islower() # True
a.isupper() # False
a.capitalize() # 'Hello kitty' <== change first letter to uppercase and rest to lowercase

b = "Hello Kitty"
b.lower() # 'hello kitty'
b.islower() # False
b.isupper() # False
b.capitalize() # 'Hello kitty' <== Only first letter is uppercase

"15".isnumeric() # True
"15.15".isnumeric() # False <== only number

"15az".isalnum() # True <== alphabet and number


