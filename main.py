import os
import time
import colorama

colorama.init()
while True:
    
    print(f"{colorama.Fore.RED}------------------ Python experiments v0.1 ------------------{colorama.Fore.RESET}\nList:")
    for i,v in enumerate(os.listdir("./exp")):
        print(f"\n{colorama.Fore.YELLOW}[{i+1}] {v}{colorama.Fore.RESET}")
    ReplyFile = input("\n>")
    if ReplyFile in os.listdir("./exp"):
        os.system(f"python3 ./exp/{ReplyFile}")
        time.sleep(0.5)
        os.system("clear")
        continue
    elif ReplyFile.isdigit():
        os.system(f"python3 ./exp/{os.listdir('./exp')[int(ReplyFile)-1]}")
        time.sleep(0.5)
        os.system("clear")
        continue
    else:
        print(f"{colorama.Fore.RED}Invalid option!{colorama.Fore.RESET}")
        time.sleep(0.5)
        os.system("clear")
        continue
    
        