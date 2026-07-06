#wap a program just like kbc
print("WELCOME TO KBC!")
q1 = "What is the capital of India?"
print("Q1:", q1)
o1 = "A. New Delhi"
o2 = "B. Mumbai"
o3 = "C. Kolkata"
o4 = "D. Chennai"
print(o1, o2, o3 , o4)
print("Enter your answer (A/B/C/D):")
ans1 = str(input())
if(ans1 == "A" or ans1 == "a"):
    print("Correct!, You won 10Lakhs!!!!")
    print("Do you want to continue?🙈")
    print("YES OR NO")
    out = str(input())
    if(out == "YES" or out == "yes"):
        q2 = "What is the capital of America?"
        print("Q2:", q2)
        o1 = "A. New York"
        o2 = "B. Washington D.C."
        o3 = "C. Boston"
        o4 = "D. Miami"
        print(o1, o2, o3 , o4)
        print("Enter your answer (A/B/C/D):")
        ans2 = str(input())
        if(ans2 == "B" or ans2 == "b"):
            print("Correct!✅, You won 50Lakhs!!!!")
            print("Do you want to continue?😏")
            print("YES OR NO")
            out = str(input())
            if(out == "YES" or out == "yes"):
                q3 = "What is the capital of UK?"
                print("Q3:", q3)
                o1 = "A. London"
                o2 = "B. Manchester"
                o3 = "C. Birmingham"
                o4 = "D. Liverpool"
                print(o1, o2, o3 , o4)
                print("Enter your answer (A/B/C/D):")
                ans3 = str(input())
                if(ans3 == "A" or ans3 == "a"):
                    print("Correct!✅, You won 1Crore!!!!")
                    print("Do you want to continue?👽")
                    print("YES OR NO")
                    out = str(input())
                    if(out == "YES" or out == "yes"):
                        q4 = "What is the capital of Canada?"
                        print("Q4:", q4)
                        o1 = "A. Toronto"
                        o2 = "B. Ottawa"
                        o3 = "C. Vancouver"
                        o4 = "D. Montreal"
                        print(o1, o2, o3 , o4)
                        print("Enter your answer (A/B/C/D):")
                        ans4 = str(input())
                        if(ans4 == "B" or ans4 == "b"):
                            print("Correct!✅, You won 5Crores!!!!")
                            print("Do you want to continue?🤯")
                            print("YES OR NO")
                            out = str(input())
                            if(out == "YES" or out == "yes"):
                                q5 = "Who is the captain of the RCB?"
                                print("Q5:", q5)
                                o1 = "A. virat kohli"
                                o2 = "B. rohit sharma"
                                o3 = "C. ms dhoni"
                                o4 = "D. kl rahul"
                                print(o1, o2, o3 , o4)
                                print("Enter your answer (A/B/C/D):")
                                ans5 = str(input())
                                if(ans5 == "A" or ans5 == "a"):
                                    print("Congratulations!!!!🤑🤑 You won 10Crores!!!!💕")
                                    print("Thank you for playing KBC!")
                                else:
                                    print("Incorrect!, Better Luck next time💔")
                            else:
                                print("You took 5Crores💰, Thank you for playing KBC!")
                        else:
                            print("Incorrect!, Better Luck next time💔")
                    else:
                        print("You took 1Crore💰, Thank you for playing KBC!")
                else:
                    print("Incorrect!, Better Luck next time💔")
        else:
            print("Incorrect!, Better Luck next time💔")
        
                  
    else:
        print("You took 10Lakhs💰, Thank you for playing KBC!")
    
else:
    print("Incorrect!, Better Luck next time💔")
