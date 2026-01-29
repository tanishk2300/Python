import random
import time

print("💖 Welcome to TRUTH 😇 or DARE 😈 - Couple Chat Booster 💖\n")

player = input("Enter your name: ")
points = 0

print("\nChoose Mood Mode:")
print("1. Cute 😇")
print("2. Flirty 😏")
print("3. Romantic 🌹")
print("4. Bold 🔥")

mode = int(input("Enter mode number: "))

# Mood-based questions
truths = {
    1: [
        "😇 What makes you smile instantly?",
        "🐻 Who is your comfort person?",
        "💭 What reminds you of me?"
    ],
    2: [
        "😏 What was your first dirty thought about me?",
        "👀 Which part of me attracts you most?",
        "🙈 Have you imagined kissing me?"
    ],
    3: [
        "🌹 When did you start feeling something for me?",
        "❤️ What do you miss about me right now?",
        "💌 What does love mean to you?"
    ],
    4: [
        "🔥 What would you do if we were alone right now?",
        "😈 What is your biggest secret desire?",
        "💋 Describe our perfect night together"
    ]
}

dares = {
    1: [
        "😊 Send a sweet emoji with my name",
        "💬 Say one nice thing about me",
        "🌸 Type 'You make me smile'"
    ],
    2: [
        "😉 Send a flirty line right now",
        "😘 Type my name 3 times with emojis",
        "😏 Send a teasing message"
    ],
    3: [
        "💖 Say 'I miss you' in your own style",
        "🌹 Write a mini love message",
        "💑 Describe our future in one line"
    ],
    4: [
        "🔥 Describe a kiss in one sentence",
        "😈 Send your boldest thought",
        "💋 Say what you want from me right now"
    ]
}

punishments = [
    "😈 Punishment: Send 'I miss you ❤️' three times",
    "🔥 Punishment: Send a heart emoji 10 times",
    "😏 Punishment: Say something you like about me"
]

while True:
    print("\n----------------------------")
    print(f"❤️ Love Points: {points}")
    print("Choose:")
    print("1 Truth 😇  (+5 points)")
    print("2 Dare 😈  (+10 points)")
    print("3 Exit🚪")

    choice = input("Enter choice: ")

    print("\n⏳ Thinking...")
    time.sleep(1)

    if choice == "1":
        print("\n😇 TRUTH:")
        print(random.choice(truths[mode]))
        input("Answar")
        points += 5
        done = input("\nDid you complete it? (yes/no): ").lower()
        if done == "yes":
                points += 10
                print("🔥 Respect! Dare completed 😏")
        else:
               print(random.choice(punishments))

    


    elif choice == "2":
        print("\n😈 DARE:")
        dare = random.choice(dares[mode])
        print(dare)
        print("do first ")
        time.sleep(5)

        done = input("\nDid you complete it? (yes/no): ").lower()
        if done == "yes":
            points += 10
            print("🔥 Respect! Dare completed 😏")
        else:
            print(random.choice(punishments))
    elif choice=="3":
         a=input("enter password for exit:")
         if a==player:
              break
         else:
              print("invalid pass... 😂")
    else:
        print("\n❌ Invalid choice 😜")

    

    # Special reward
    if points >= 50:
        print("\n🎉 SPECIAL MOMENT UNLOCKED 🎉")
        print("💑 You both owe each other a real hug or call 😏❤️")
        break
