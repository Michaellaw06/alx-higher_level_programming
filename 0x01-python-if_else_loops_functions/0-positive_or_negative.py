```python
#!/usr/bin/python3
import random

def generate_number():
    return random.randint(-10, 10)

def check_number(number):
    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")

if __name__ == "__main__":
    num = generate_number()
    check_number(num)
```
