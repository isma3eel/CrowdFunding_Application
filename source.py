import os


def application_register():
    """Users signup for the crowd funding application with the data of fullName,
     Email, Password, Mobile Number"""

    file_name = "User Data.txt"
    email = ""
    name = ""
    mobile = ""
    user_data = []
    password = "abc"
    confirm_password = "cba"

    while not name:
        name = input("Please Enter your full Name: ")

    while not email:
        email = input("Please Enter your Email: ")
        try:
            if string_search(file_name, email, True):
                print("Email Already Taken")
                email = ""
        except FileNotFoundError:
            pass

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
    data inside a text file | Modify directory pass to work"""

    file_obj = open(filename, 'a')
    file_obj.write("\n")
    for i in user_data:
        file_obj.write(i)
        file_obj.write("-  -")


def application_login():
    """Takes login info(email, password) from user and puts it in a list for it to be compared
    with the pre-saved file | if no accounts were registered before it will end the executions """

    file_name = "User Data.txt"
    login_data = []
    email = ""
    password = ""
    while not email:
        email = input("Please Enter your Email: ")
        try:
            if not string_search(file_name, email, True):
                print("Email is not found")
                return False, 0
        except FileNotFoundError:
            print("No registers found ! Register account then try again")
            return False, 0
    while not password:
        password = input("Enter Password: ")
    login_data.append(email)
    login_data.append(password)
    if file_check(login_data):
        return True, email


def file_check(login_data):
    """the user attempt login data[email, password] is compared with data inside the pre-saved
     file. if true attempt it will login and if failed it will stop"""

    file_name = "User Data.txt"
    file_obj = open(file_name, "r")
    line = string_search(file_name, login_data[0], False)
    print(line)
    data_split = line.split("-  -")
    user_info = [data_split[2], data_split[3]]

    if user_info == login_data:
        file_obj.close()
        return True
    else:
        print("Wrong email or password !")
        # application login attempt t - 3
        file_obj.close()
        return False


def user_entry(email):
    """After Successful login user is asked for more options inside the app """

    print("Login Successfully\n.........................\n")
    print("What do you like to do?")
    choice = int(input("1-Create a new project        2-View and edit already existed projects\n"))
    if choice == 1:
        project_creation(email)
    elif choice == 2:
        project_edit(email)
    else:
        print("Wrong Choice !")


def project_creation(email):
    """Saving project data inside (Project Data.txt) file"""

    project_data = []

    project_data.append(email)
    project_data.append(input("Please enter project title: "))
    project_data.append(input("Please enter details about the project: "))
    project_data.append(input("What is the target you're aiming to reach (EGP)? "))
    project_data.append(input("Start date: "))
    project_data.append(input("End date: "))

    file_save("Project Data.txt", project_data)


def project_edit(email):

    choice = int(input("1-View All Projects\n2-Edit Projects\n3-Delete Projects\n4-Search for a project using s specific keyword\n"))
    if choice == 1:
        view = view_all_projects(email)[0]
        for i in range(len(view)):
            print(view[i][1])
    if choice == 2:
        pass
    if choice == 3:
        delete_project(email)
    if choice == 4:
        pass


def view_all_projects(email):
    """Used to search for the projects submitted by a specific user using the email address
    as a parameter. it returns the list of lists of things done by user and also line numbers"""

    i = 0
    line_number = []
    lines = []
    with open("Project Data.txt", "r") as read_obj:
        for line in read_obj:
            if email in line:
                splits = line.split("-  -")
                lines.append(splits)
                line_number.append(i)
            i += 1

    return lines,line_number



def delete_project(email):
    line_number = view_all_projects(email)[1]
    with open("Project Data.txt", "r") as read_obj:
        for line in read_obj:
            print(line)



def string_search(file_name, search_str, chk):
    """Search for a specific string inside a file
    chk=True for application_login function to chk if email exist in database - return True/False
    chk=false for file_check function to compare login data with user data - return line number"""

    with open(file_name, "r") as read_obj:
        for line in read_obj:
            if search_str in line:
                if chk:
                    return True
                return line



def main():
    os.chdir("C:\\Users\Isma3el\PycharmProjects\iti_crowdFunding\saves")
    print("Welcome to CrowdFunding application\n")
    done = False
    print("What do you like to do?")
    while not done:
        choice = input("1-Register   2-Login\n")
        if choice == "1":
            application_register()
            done = True
        elif choice == "2":
            # return True and email from successful login
            lo_return = application_login()
            if lo_return[0]:
                user_entry(lo_return[1])
            else:
                done = True
            done = True
        elif choice == "3":
            print("Testing")
            # line = string_search("Project Data.txt", "zzidan@outlook.com", False)
            # splits = line.split("-  -")
            # print(splits)
            # view_all_projects("zzidan@outlook.com")
            delete_project("zzidan@outlook.com")
            done = True
        else:
            print("Wrong choice")


if __name__ == '__main__':
    main()
