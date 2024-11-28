# ask the user for file type (either integer, image, text, xxx)
def get_filetype():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or exit code
        if response == "xxx" or response == "i":
            return response

        # check for integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for text
        elif response in ["text", 'txt', 't']:
            return "text"

        # check for image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # print an error as output for invalid responses
        else:
            print("Sorry, please choose integer, text or image")
            print("")

# Main routine goes here
while True:
    file_type = get_filetype()

    # if user chose 'i', check for image / integer
    if file_type == 'i':

        want_image = input("Press <enter> for integer or any key for image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"
    print(f"Your choice is {file_type}")
    print("")

    if file_type == "xxx":
        print("Thank you for using the Bits Calculator")
        break