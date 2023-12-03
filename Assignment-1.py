def reverse_string(s):
    reversed_str =""
    for i in range(len(s) -1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def main():
    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")
if __name__ == "__main__":
    main()

