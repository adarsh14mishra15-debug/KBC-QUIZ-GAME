import random

print("WELCOME TO KBC!")

# A bigger bank of questions to draw from — more than we need per game,
# so each playthrough can be different.
question_bank = [
    {"q": "What is the capital of India?",
     "options": ["A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"], "answer": "A"},
    {"q": "What is the capital of America?",
     "options": ["A. New York", "B. Washington D.C.", "C. Boston", "D. Miami"], "answer": "B"},
    {"q": "What is the capital of UK?",
     "options": ["A. London", "B. Manchester", "C. Birmingham", "D. Liverpool"], "answer": "A"},
    {"q": "What is the capital of Canada?",
     "options": ["A. Toronto", "B. Ottawa", "C. Vancouver", "D. Montreal"], "answer": "B"},
    {"q": "What is the capital of Australia?",
     "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"], "answer": "C"},
    {"q": "What is the capital of Japan?",
     "options": ["A. Osaka", "B. Tokyo", "C. Kyoto", "D. Nagoya"], "answer": "B"},
    {"q": "What is the capital of France?",
     "options": ["A. Lyon", "B. Marseille", "C. Nice", "D. Paris"], "answer": "D"},
    {"q": "Who won the World Cup as captain of the Indian cricket team in 2011?",
     "options": ["A. virat kohli", "B. rohit sharma", "C. ms dhoni", "D. ajinkya rahane"], "answer": "C"},
]

# Prize ladder — position in the game, not tied to any specific question.
prize_ladder = ["10 Lakhs", "50 Lakhs", "1 Crore", "5 Crores", "10 Crores"]

# Randomly pick as many questions as there are prizes, in random order.
questions = random.sample(question_bank, len(prize_ladder))
for q, prize in zip(questions, prize_ladder):
    q["prize"] = prize

lifeline_used = False  # 50-50 lifeline, can only be used once per game

for i, q in enumerate(questions, start=1):
    print(f"\nQ{i}: {q['q']}")
    print(*q["options"])

    if not lifeline_used:
        use = input("Use 50-50 lifeline? (YES/NO): ").strip().upper()
        if use == "YES":
            lifeline_used = True
            correct_letter = q["answer"]
            wrong_options = [opt for opt in q["options"] if not opt.startswith(correct_letter)]
            options_to_show = random.sample(wrong_options, 1) + [opt for opt in q["options"] if opt.startswith(correct_letter)]
            print("Here are your 2 options:")
            print(*options_to_show)

    ans = input("Enter your answer (A/B/C/D): ").strip().upper()

    if ans != q["answer"]:
        print("Incorrect!, Better Luck next time")
        break

    if i == len(questions):
        print(f"Congratulations!!!! You won {q['prize']}!!!!")
        print("Thank you for playing KBC!")
        break

    print(f"Correct!, You won {q['prize']}!!!!")
    print("Do you want to continue?")
    out = input("YES OR NO: ").strip().upper()

    if out != "YES":
        print(f"You took {q['prize']}, Thank you for playing KBC!")
        break
