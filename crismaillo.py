import time

fun_facts = [
    "I am very afraid of pigeons",
    "I can crack an egg with one hand",
    "God, bold of you to assume that anyone can be that interesting",
]

def main():
    i = 0

    print("\n")
    print("Hey I'm Cris. I have been thinking a lot lately about making and creating.")

    while True:
        print("1. what's the purpose of this account?")
        print("2. what is my practice? what do I want to explore?")
        print("3. what does my @ mean?")
        print("4. fun fact about me")
        print("5. exit program")
        
        print("\n")
        choice = input("choose: ")
        print("\n")

        if choice == "1":
            print("this account's purpose is to be a personal trigger, reminder, and ecouragement to set time aside to create")
            print("and most importantly, to document the journey and reflect on what I learn.")
            print("in a way, I want with this to learn how to create fast and slow,\nby that I mean learning quickly but always with care and mind.")
            print("I am inspired by rituals around creative work and focusing on process over outcome.")
            print("however I really don't want this to ever become a focus on productivity and similar discourse,")
            print("I have started realizing that that usually detracts from the actual joy of creating for the sake of creating.")
        elif choice == "2":
            print("my practice, I think, will mostly be focused on web development and general creative computing experimenting.")
            print("however, there'll also be a bit of lino cut and sunprinting. \nI also enjoy film photography but I'll abstain from talking about it \nunless I look into learning how to develop/scan/edit which I'm hoping I will!")
            print("I also would like to explore some basic 3D modelling, generative art and print making in general.")
            print("and finally, putting work into writing and design/communication will also be inherent to what I put out\nand I am really excited to see it develop.")
        elif choice == "3":
            print("i originally was drawn to beep as a reference to a computer beeping,\nhowever I've actually realized today that electronic music is beeps too.")
            print("00000111 is the binary representation of the ASCII character for the bell (beep) character, \ntraditionally it triggered a beep or audible alert (but now we generate sounds through sound libraries).")
        elif choice == "4":
            while i < len(fun_facts):
                print(fun_facts[i])
                i += 1
                if i < len(fun_facts):
                    more = input("\nDo you want more? y for yes, n for no:")
                    if (more == "n"):
                        break
            i = 0
        elif choice == "5":
            print("come back soon :)")
            break
        else:
            print("not an option, make better choices")
        print("_________________________________________________________________________________________________________")
        print("\n")
        time.sleep(3)

if __name__ == "__main__":
    main()


