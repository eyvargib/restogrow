


class Member:

    def __init__(self,percentage):
        self.percentage_share=percentage
        self.spent=0
        self.common_spent=0
        self.debit_pending=self.spent-self.common_spent



class splitwise:

    def __init__(self,group):
        self.total_member=0
        self.group=group
        self.dict_person=dict()
        print(f"Group : {group} is created")
        
    
    def add_member(self,person):
        print("Enter percentage share of user  like (55)")
        for i in range(self.total_member,self.total_member+person):

            p=int(input(f"Enter percentage share of user {i+1}:"))
            self.dict_person[i+1]=Member(p)

        self.total_member +=person

    def distribute(self):
        u=int(input("Enter user id to spent money :"))
        if u in self.dict_person.keys():
            amount=int(input("Amount of money you spent :"))
            self.dict_person[u].spent +=amount
            distribution=(amount/len(self.dict_person))
            for i in range(len(self.dict_person)):
                self.dict_person[i+1].common_spent +=distribution

    def details_printer(self):
        print("\n\n\n")
        for i in range(len(self.dict_person)):
            print(f"\t\tPerson {i+1}\n")
            print(f"Amount You spent {self.dict_person[i+1].spent}")
            print(f"Amount You in common {self.dict_person[i+1].common_spent}")
            print(f"Amount You have to pay {self.dict_person[i+1].debit_pending}")

        print("\n\n")
        







if __name__ == "__main__":
    print("\n\n")
    print("\t\t\tWelcome to splitwise\n\n")
    print("1.Create Group ")
    print("2.Exit ")
    o=int(input("Enter Your Options(1,2): "))
    if(o == 1):
        n=input("Enter your Group Name : ")
        p=int(input("Enter no of person in Group : "))
        gp1=splitwise(n)
        gp1.add_member(p)
        while  1:
            i=int(input("Enter 1 to spent money \nEnter 2 : To print details of money \n"))
            if i==1:
                gp1.distribute()
            elif i==2 :
                gp1.details_printer()
            else:
                break




        
    
