class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input= input("""welcome to chatbook !! how would you like to proceed?" 
                            1. press 1 to signup
                            2. press 2 to signin
                            3. press 3 to write a post
                            4. press 4 to message a friend
                            5. press any other key to exit""")
        
        if user_input == "1":
           self.signup()
        elif user_input == "2":
            self.signin()
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email=input("enter your email id")
        pwd =input("setup your passward")
        self.username=email
        self.password=pwd
        print("you have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("no user found please signup first")
        else:
            uname=input("enter your user name here ")
            pwd=input("enter your passward here")
            if self.username==uname and self.password==pwd:
                print("you have logged in successfully")
                self.loggedin=True
            else:
                print("invalid credentials")
        print("\n")
        self.menu()



obj = chatbook()