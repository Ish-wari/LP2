# =========================================
# CUSTOMER SUPPORT CHATBOT
# Algorithms Used:
# 1. Selection Sort
# 2. Job Scheduling
# =========================================


# ---------- INTRO ----------

def intro():

    print("\n========================================")
    print("      WELCOME TO HELPBOT 🤖")
    print("========================================")

    print("\nI am a Customer Support Chatbot.")
    print("I help customer care managers to:")
    print("• Manage customer complaints")
    print("• Sort urgent complaints first")
    print("• Schedule support tasks efficiently")

    print("\nAvailable Commands:")
    print("1 -> Show Complaints")
    print("2 -> Sort Complaints")
    print("3 -> Schedule Support Tasks")
    print("4 -> Exit")


# ---------- SELECTION SORT ----------

def selection_sort(complaints):

    n = len(complaints)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            # Compare priorities
            if complaints[j][1] < complaints[min_index][1]:
                min_index = j

        # Swap
        complaints[i], complaints[min_index] = complaints[min_index], complaints[i]

    return complaints


# ---------- JOB SCHEDULING ----------

def job_scheduling(tasks):

    # Sort according to profit (high to low)
    tasks.sort(key=lambda x: x[2], reverse=True)

    max_deadline = 0

    # Find maximum deadline
    for task in tasks:

        if task[1] > max_deadline:
            max_deadline = task[1]

    slots = [False] * max_deadline
    result = [""] * max_deadline

    total_profit = 0

    # Schedule tasks
    for task in tasks:

        task_name = task[0]
        deadline = task[1]
        profit = task[2]

        for i in range(deadline - 1, -1, -1):

            if slots[i] == False:

                slots[i] = True
                result[i] = task_name
                total_profit += profit
                break

    print("\n🤖 HelpBot:")
    print("Support Tasks Scheduled Successfully!\n")

    print("Scheduled Tasks:")

    for task in result:

        if task != "":
            print("•", task)

    print("\nTotal Service Profit:", total_profit)



# ---------- CHATBOT ----------

def chatbot():

    # complaint name, priority
    complaints = [
        ("Payment Failed", 3),
        ("Account Hacked", 1),
        ("Refund Pending", 2),
        ("Late Delivery", 4)
    ]

    # task name, deadline, profit
    tasks = [
        ("Handle Premium Customer", 2, 100),
        ("Solve Payment Issue", 1, 80),
        ("Process Refund", 2, 60),
        ("Delivery Support", 1, 70)
    ]

    intro()

    while True:

        print("\n----------------------------------------")

        choice = input("\nYou: ")

        # SHOW COMPLAINTS
        if choice == "1":

            print("\n🤖 HelpBot:")
            print("Here are current customer complaints:\n")

            for complaint in complaints:

                print("Complaint:", complaint[0],
                      "| Priority:", complaint[1])

            print("\nSmaller priority number = More urgent complaint")


        # SORT COMPLAINTS
        elif choice == "2":

            print("\n🤖 HelpBot:")
            print("Sorting complaints using Selection Sort...\n")

            sorted_complaints = selection_sort(complaints)

            print("Complaints After Sorting:\n")

            for complaint in sorted_complaints:

                print("Complaint:", complaint[0],
                      "| Priority:", complaint[1])

            print("\nMost urgent complaints are now at the top.")


        # SCHEDULE TASKS
        elif choice == "3":

            print("\n🤖 HelpBot:")
            print("Scheduling customer support tasks...\n")

            job_scheduling(tasks)


        # EXIT
        elif choice == "4":

            print("\n🤖 HelpBot:")
            print("Thank you! Customer support tasks completed.")
            break


        # INVALID INPUT
        else:

            print("\n🤖 HelpBot:")
            print("Sorry, I did not understand that command.")



# ---------- MAIN ----------

chatbot()