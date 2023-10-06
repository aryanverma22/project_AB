from Books.Input.Model.model import Input
from flask import request

def convert_input(func):
    def wrapper():
        # Process the input
        data = func()
        return [Input(**data), data]

    return wrapper()
# @convert_input
def take_input():
    data = request.json
    print(data)
    # inp = Input(**data)
    return data

# @convert_input
def take_input_get():
    data = request.args
    # inp = Input(**data)
    return data


#


def my_decorator(func):
    def wrapper():
        # Process the input
        data = func()
        return [Input(**data), data]

    return wrapper()

# # @my_decorator
# def trial():
#     x = {
#         "topic": "New update roll out",
#         "user_id": "4",
#         "content": {
#             "Glad": "Impressive features",
#             "Mad": "Increased the workload a lot",
#             "Sad": "Still some bugs unresolved"
#         }
#     }
#     return x
# trial= my_decorator(trial)
# b=trial
# print((b[0]))
#
#     #     # Call the original function with the processed input
#     #
#     #
#     #     # Process the output
#     #     # processed_output = process_output(result)
#     #
#     #     # Return the processed output
#     #     return result
#     #
#     # return wrapper
