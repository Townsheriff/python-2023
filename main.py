

try:
  raise Exception("Hello Exception")
except Exception as err:
  print(f'Handled Error message="{err}"')


try:
  100 / 0
except Exception as err:
  print(f'Handling division by 0 message="{err}"')


class MyException(Exception):
  def __init__(self, message, error_code):
    super().__init__(message)

    self.message = message
    self.error_code = error_code
    

try:
  raise MyException("my message", 123)
except MyException as err:
  print(f'My exception message="{err.message}" error_code={err.error_code}')