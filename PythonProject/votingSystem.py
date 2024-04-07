import time

nominee1 = input("Enter the name of the first nominee: ")
nominee2 = input("Enter the name of the second nominee: ")

voterId = [1, 2, 3, 4]

num_vote1 = 0
num_vote2 = 0

def votingFunction():
    global num_vote1, num_vote2

    while True:
        if voterId == []:
            print("Voting completed")

            print("Counting the votes...")
            
            i= 0
            while(i!= 5):
                
                print(".", end = "")
                time.sleep(1)
                i= i+1
            
            
            if num_vote1 > num_vote2:
                print(f"\n{nominee1} won this election with {num_vote1 - num_vote2} votes\n")
            elif num_vote2 > num_vote1:
                print(f"\n{nominee2} won this election with {num_vote2 - num_vote1} votes\n")
            else:
                print(f"\nBoth candidates got {num_vote1} votes respectively\n")
            break

        voter = int(input("Enter your voter id: "))

        if voter in voterId:
            print("Verified !!")

            print("-----------------------------------------")
            print("For giving the vote press your selection. \n")
            print("Press 1 for ", nominee1, "and Press 2 for ", nominee2)
            print("-----------------------------------------")

            vote = int(input("Select your precious vote: "))
            if vote == 1:
                num_vote1 += 1
                print("Your vote has been submitted to ", nominee1)
                voterId.remove(voter)
            elif vote == 2:
                num_vote2 += 1
                print("Your vote has been submitted to ", nominee2)
                voterId.remove(voter)
            else:
                print("Invalid selection !!! \n Press your selection again")

        else:
            print("Are you trying to vote again...?\n")


while True:
    user = input("Do you want to conduct the election again? (Press Y for yes and N for no): ")
    if user.lower() == 'y':
        votingFunction()
    elif user.lower() == 'n':
        print("Thanks for your precious time.")
        break
