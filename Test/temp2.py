# import re
#
#
# def validate_user(username, minlen):
#     if minlen < 1:
#         raise ValueError("minlen must be at least 1")
#
#     # Usernames can't be shorter than minlen
#     if len(username) < minlen:
#         return False
#     # Usernames can only use letters, numbers, dots and underscores
#     if not re.match('^[a-z][a-z0-9._]*$', username):
#         return False
#     # Usernames can't begin with a number
#     if username[0].isnumeric():
#         return False
#     return True
#
#
# print(validate_user("blue.kale", 3))  # True
# print(validate_user(".blue.kale", 3))  # False
# print(validate_user("red_quinoa", 4))  # True
# print(validate_user("_red_quinoa", 4))  # False
arr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]



arr[-5] = "Holiday"



for i in range(len(arr)):

    print(arr[i])


print(3 ** 5.0 + 3 * 2)