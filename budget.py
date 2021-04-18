#App database

budget_dictionary = [{
    "category": "food",
    "amount": 0,
}, {
    "category": "cloths",
    "amount": 0,
}, {
    "category": "entertainment",
    "amount": 0,
}]


# Budget class with categories
class budget:

    def __init__(self):
        pass

    def deposit(self):
        print('**** Welcome ****')
        print("Select Budget Options")
        print("1. food")
        print("2. cloth")
        print("3. entertainment")
        print("4. exit")
        selected_budget = int(input("select budget \n "))

        if selected_budget == 1:
            print("Food Balance is: ", budget_dictionary[0]["amount"])
            depo_act = int(input("deposit to food balance? 1(yes), 2(no) \n "))
            if depo_act == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budget_dictionary[0]["amount"] + deposit
                budgetDict[0]["amount"] = budgetDict[0]["amount"] + deposit
                print("Balance: ", budgetDict[0]["amount"])
                withd_act = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n "))
                if withd_act == 2:
                    self.withdrawfromBudget()

                elif withd_act == 1:
                    self.transfer()

                elif withd_act == 3:
                    exit()
                else:
                    return("Goodbye")

            else:
                return("invalid Selection\n PLEASE SELECT A VALID OPTION")
                self.deposit()




        elif selected_budget == 2:
            print("Cloth Balance: ", budget_dictionary[1]["amount"])
            depo_act = int(input("deposit to cloth balance? 1(yes), 2(no) \n"))
            if depo_act == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budget_dictionary[1]["amount"] + deposit
                budgetDict[1]["amount"] = budget_dictionary[1]["amount"] + deposit
                print("Balance: ", budget_dictionary[1]["amount"])
                withd_act = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if withd_act == 2:
                    self.withdrawfromBudget()

                elif withd_act == 1:
                    self.transfer()

                elif withd_act == 3:
                    exit()
                else:
                    print("Have a Nice Day")


            else:
                print("invalid Selection\n PLEASE SELECT A VALID OPTION")
                self.deposit()



        elif selected_budget == 3:
            print("Cloth Balance: ", budget_dictionary[2]["amount"])
            depo_act = int(input("deposit to cloth balance? 1(yes), 2(no) \n"))
            if depo_act == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[2]["amount"] + deposit
                budgetDict[2]["amount"] = budget_dictionary[1]["amount"] + deposit
                print("Balance: ", budget_dictionary[2]["amount"])
                withd_act = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if withd_act == 2:
                    self.withdrawfromBudget()

                elif withd_act == 1:
                    self.transfer()

                elif withd_act == 3:
                    exit()
                else:
                    return("goodbye")


            else:
                print("invalid Selection\n PLEASE SELECT A VALID OPTION")
                self.deposit()

        elif selected_budget == 4:
            return("goodbye!!!")
            exit()


        else:
            print("goodbye")

    def withdraw_from_budget(self):
        print(budget_dictionary)
        print("withdraw Options")
        print("1. Food")
        print("2. cloth")
        print("3. entertainment")
        print("4. exit")
        selected_budget_option = int(input("select withdraw Options \n"))

        if selected_budget_option == 1:
            print("Food Balance: ", budget_dictionary[0]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budget_dictionary[0]["amount"]:
                print("insuficent Funds")
                withd_act = int(input("would you like to return home 1(yes), 2(no)"))
                if withd_act == 1:
                    self.deposit()
                else:
                    print("goodbye")
                    exit()

            else:
                withdraw1 = budgetDict[0]["amount"] - withdraw
                budgetDict[0]["amount"] = budgetDict[0]["amount"] - withdraw
                print("Withdrawal Sucessful")
                print("Food Balance: ", budget_dictionary[0]["amount"])
                withd_act = int(input("would you like to return home 1(yes), 2(no)"))
                if withd_act == 1:
                    self.deposit()
                else:
                    print("goodbye")
                    exit()

        elif selected_budget_option == 2:
            print("CLOTH BALANCE: ", budget_dictionary[1]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[1]["amount"]:
                print("insuficent Funds")
                withd_act = int(input("would you like to return home 1(yes), 2(no)"))
                if withd_act == 1:
                    self.deposit()
                else:
                    print("have a nice day")
                    exit()

            else:
                withdraw1 = budgetDict[1]["amount"] - withdraw
                budgetDict[1]["amount"] = budget_dictionary[1]["amount"] - withdraw
                print("Withdrawal Sucessful")
                print("Cloth Balance: ", budget_dictionary[1]["amount"])
                withd_act = int(input("would you like to return home 1(yes), 2(no)"))
                if withd_act == 1:
                    self.deposit()
                else:
                    print("goodbye")
                    exit()

        elif selected_budget_option == 3:
            print("Entertainment Balance: ", budget_dictionary[2]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budget_dictionary[2]["amount"]:
                print("insuficent Funds")
                withd_act = int(input("would you like to return home 1(yes), 2(no)"))
                if withd_act == 1:
                    self.deposit()
                else:
                    print("goodbye")
                    exit()

            else:
                withdraw1 = budget_dictionary[2]["amount"] - withdraw
                budget_dictionary[2]["amount"] = budget_dictionary[2]["amount"] - withdraw
                print("Withdrawal Sucessful")
                print("Entertainment Balance: ", budget_dictionary[2]["amount"])
                withd_act = int(input("would you like to return home 1(yes), 2(no)"))
                if withd_act == 1:
                    self.deposit()
                else:
                    print("goodbye")
                    exit()

        elif selected_budget_option == 4:
            print("goodbye!!!")
            exit()

        else:
            print("invalid Selection\n PLEASE SELECT A VALID OPTION")
            self.deposit()

    def transfer(self):
        print(budget_dictionary)
        print("Transfer Options")
        print("1.From  Food")
        print("2.From cloth")
        print("3.From entertainment")
        print("4. exit")
        select_tf_option = int(input("select destination\n"))

        if select_tf_option == 1:
            print("Food Balance: ", budget_dictionary[0]["amount"])
            tf = int(input("1.(Transfer to Cloth), 2.(Transfer to Entertainment)\n"))
            if tf == 1:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budget_dictionary[0]["amount"]:
                    tfamount1 = budget_dictionary[0]["amount"] - tfamount
                    tfamount2 = budget_dictionary[1]["amount"] + tfamount
                    budget_dictionary[0]["amount"] = budget_dictionary[0]["amount"] - tfamount
                    budget_dictionary[1]["amount"] = budget_dictionary[1]["amount"] + tfamount
                    tfamount2 = budget_dictionary[1]["amount"] + tfamount
                    print("tf SUCESSFUL!!!")
                    print("Food Balance: ", budget_dictionary[0]["amount"])
                    print("Cloth Balance: ", budget_dictionary[1]["amount"])
                    tf_act = int(input("new transfer again? 1(ye) 2(no)\n"))
                    if tf_act == 1:
                        self.transfer()
                    else:
                        print("goodbye!!")
                        exit()
                else:
                    print("insufficent funds")
                    print("Food Balance: ", budget_dictionary[0]["amount"])
                    self.deposit()

            elif tf == 2:
                tfamount = int(input("Enter Amount\n "))
                if tfamount <= budget_dictionary[0]["amount"]:
                    tfamount1 = budget_dictionary[0]["amount"] - tfamount
                    tfamount2 = budget_dictionary[2]["amount"] + tfamount
                    budget_dictionary[0]["amount"] = budget_dictionary[0]["amount"] - tfamount
                    budget_dictionary[2]["amount"] = budget_dictionary[2]["amount"] + tfamount
                    tfamount2 = budget_dictionary[1]["amount"] + tfamount
                    print("tf SUCESSFUL!!!")
                    print("Food Balance: ", budget_dictionary[0]["amount"])
                    print("Entertainment Balance: ", budget_dictionary[2]["amount"])
                    tf_act = int(input("Transfer again? 1(ye) 2(no)\n"))
                    if tf_act == 1:
                        self.transfer()
                    else:
                        print("goodbye!!")
                        exit()

                else:
                    print("insufficent funds")
                    print("Food Blanace: ", budget_dictionary[0]["amount"])
                    self.deposit()

        elif select_tf_option == 2:
            print("Cloth Balance: ", budget_dictionary[1]["amount"])
            tf = int(input("1.(tf to Entertainment), 2.(tf to Food)\n "))
            if tf == 1:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budget_dictionary[1]["amount"]:
                    tfamount1 = budget_dictionary[1]["amount"] - tfamount
                    tfamount2 = budget_dictionary[2]["amount"] + tfamount
                    budget_dictionary[1]["amount"] = budget_dictionary[1]["amount"] - tfamount
                    budget_dictionary[2]["amount"] = budget_dictionary[2]["amount"] + tfamount
                    tfamount2 = budget_dictionary[1]["amount"] + tfamount
                    print("tf SUCESSFUL!!!")
                    print("Cloth Balance: ", budget_dictionary[1]["amount"])
                    print("Entertainment Balance: ", budget_dictionary[2]["amount"])
                    tf_act = int(input("Transfer again? 1(ye) 2(no)\n"))
                    if tf_act == 1:
                        self.transfer()

                    else:
                        print("goodbye!!")
                        exit()
                else:
                    print("insufficent funds")
                    print("Food Balance: ", budget_dictionary[0]["amount"])
                    self.deposit()

            elif tf == 2:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budget_dictionary[1]["amount"]:
                    tfamount1 = budget_dictionary[1]["amount"] - tfamount
                    tfamount2 = budget_dictionary[0]["amount"] + tfamount
                    budget_dictionary[1]["amount"] = budget_dictionary[1]["amount"] - tfamount
                    budget_dictionary[0]["amount"] = budget_dictionary[0]["amount"] + tfamount
                    tfamount2 = budget_dictionary[0]["amount"] + tfamount
                    print("tf SUCESSFUL!!!")
                    print("Cloth Balance: ", budget_dictionary[1]["amount"])
                    print("Food Balance: ", budget_dictionary[0]["amount"])
                    tf_act = int(input("Transfer again? 1(ye) 2(no)\n "))
                    if tf_act == 1:
                        self.transfer()
                    else:
                        print("goodbye!!")
                        exit()

                else:
                    print("insufficent funds")
                    print("Cloth Balnace: ", budget_dictionary[1]["amount"])
                    self.deposit()

        elif select_tf_option == 3:
            print("ENTERTAINMENT BALANCE: ", budget_dictionary[2]["amount"])
            tf = int(input("1.(TF to cloth), 2.(TF to Food)\n"))
            if tf == 1:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budget_dictionary[2]["amount"]:
                    tfamount1 = budget_dictionary[2]["amount"] - tfamount
                    tfamount2 = budget_dictionary[1]["amount"] + tfamount
                    budget_dictionary[2]["amount"] = budget_dictionary[2]["amount"] - tfamount
                    budget_dictionary[1]["amount"] = budget_dictionary[1]["amount"] + tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    print("tf SUCESSFUL!!!")
                    print("Entertainment Balance: ", budget_dictionary[2]["amount"])
                    print("Cloth Balance: ", budget_dictionary[1]["amount"])
                    tf_act = int(input("Transfer again? 1(ye) 2(no)\n"))
                    if tf_act == 1:
                        self.transfer()
                    else:
                        print("goodbye!!")
                        exit()

                else:
                    print("insufficent funds")
                    print("Food Balance: ", budget_dictionary[0]["amount"])
                    self.deposit()

            elif tf == 2:
                tfamount = int(input("Enter Amount\n "))
                if tfamount <= budget_dictionary[2]["amount"]:
                    tfamount1 = budget_dictionary[2]["amount"] - tfamount
                    tfamount2 = budget_dictionary[0]["amount"] + tfamount
                    budget_dictionary[2]["amount"] = budget_dictionary[2]["amount"] - tfamount
                    budget_dictionary[0]["amount"] = budget_dictionary[0]["amount"] + tfamount
                    tfamount2 = budget_dictionary[0]["amount"] + tfamount
                    print("tf SUCESSFUL!!!")
                    print("Entertainment Balance: ", budget_dictionary[2]["amount"])
                    print("Food Balance: ", budget_dictionary[0]["amount"])
                    tf_act = int(input("Transfer again? 1(ye) 2(no)\n"))
                    if tf_act == 1:
                        self.transfer()
                    else:
                        print("goodbye!!")
                        exit()

                else:
                    print("insufficent funds")
                    print("Cloth Blanace: ", budget_dictionary[1]["amount"])
                    self.deposit()

        elif select_tf_option == 4:
            return("goodbye!!!")
            exit()

        else:
            print("goodbye!!!")


transaction = budget()
transaction.deposit()