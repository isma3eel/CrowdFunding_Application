import os


def application_register():
    """Users signup for the crowd funding application with the data of fullName,
     Email, Password, Mobile Number"""

    email = ""
    name = ""
    mobile = ""
    # data = [50][6]
    user_data = []
    password = "abc"
    confirm_password = "cba"

    while not name:
        name = input("Please Enter your full Name: ")

    while not email:
        email = input("Please Enter your Email: ")
        if string_search(email, True):
            print("Email Already Taken")
            email = ""

    while password != confirm_password:
        password = input("Enter Password: ")
        while not password:
            password = input("Enter Password: ")
        confirm_password = input("Confirm Password: ")
        while not confirm_password:
            confirm_password = input("Confirm Password: ")
    print("Password Confirmed..")

    while not mobile:
        mobile = input("please enter your mobile phone: ")

    print("...............................................")
    print("Thanks for registering")

    first_name = name.split(" ")[0]
    last_name = name.split(" ")[-1]

    user_data.append(first_name)
    user_data.append(last_name)
    user_data.append(email)
    user_data.append(password)
    user_data.append(mobile)

    file_save("User Data.txt", user_data)


def file_save(filename, user_data):
    """Data from registering is sent to this function as a first step to save
    data inside a text file"""

    os.chdir("C:\\Users\Isma3el\PycharmProjects\iti_crowdFunding\saves")
    print(os.getcwd())
    file_obj = open(filename, 'a')
    file_obj.write("\n")
    for i in user_data:
        file_obj.write(i)
        file_obj.write(" ")


def application_login():
    """Takes login info(email, password) from user and puts it in a list for it to be compared
    with the pre-saved file"""

    login_data = []
    email = ""
    password = ""
    while not email:
        email = input("Please Enter you Email: ")
        if not string_search(email, True):
            print("Email is not found")
            email = ""
    while not password:
        password = input("Enter Password: ")
    login_data.append(email)
    login_data.append(password)
    file_check(login_data)


def file_check(login_data):
    """After the user attempt to login the data from user is compared with data
    inside the pre-saved file if true attempt it will login and if failed it will stop"""

    file_obj = open("User Data.txt", "r")
    file_data = file_obj.read()
    line = string_search(login_data[0], False)
    print(line)
    data_split = line.split(" ")
    user_info = [data_split[2], data_split[3]]
    # print(login_data)
    # print(user_info)
    if user_info == login_data:
        print("HOOOLAAAAA!!!!")
        file_obj.close()
    else:
        print("Wrong !")
        # application login attempt t - 3
        file_obj.close()


def project_creation():
    pass


def string_search(search_str, chk):
    """Search for a specific string inside a text
    chk=True for application_login function to chk if email exist in database
    chk=false for file_check function to compare login data with user data"""

    with open("User Data.txt", "r") as read_obj:
        for line in read_obj:
            if search_str in line:
                # print(line)
                if chk:
                    return True
                return line



def main():
    os.chdir("C:\\Users\Isma3el\PycharmProjects\iti_crowdFunding\saves")
    fileObj = open("User Data.txt", "r")
    print("Welcome to CrowdFunding application\n")
    done = False
    print("What do you like to do?")
    while not done:
        choice = input("1-Register   2-Login\n")
        if choice == "1":
            application_register()
            done = True
        elif choice == "2":
            application_login()
            done = True
        elif choice == "3":
            print("Testing")
            file_obj = open("User Data.txt", 'r')
            xx = file_obj.read()
            splits = xx.split(" ")
            print(splits)
        else:
            print("Wrong choice")


if __name__ == '__main__':
    main()

