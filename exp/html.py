import os
import requests
import time


while True:
    
    print("Hello and welcome to my html reading project")
    
    asd = input("\nInput a website\n>")
    
    if "https://" in asd:
        # Get raw html content of the website
        RawHtml = requests.get(asd).text
        
        # Distinguish the tags
        tags = []
        inputTags = ["h", "p", "a", "img", "div", "span", "ul", "li", "ol", "table", "tr", "td", "th", "form", "input", "button", "textarea", "select", "option", "label", "br"]
        while True:
            InputTag = input("Website loaded. Which tags would you like to see?\n>")
            if InputTag.lower() in inputTags:
                
                if f"<{InputTag}" in RawHtml:
                    # Find the HTML Tag and print when it is used in the html
                    print(f"\n{InputTag} tag used in the website")
                    print(RawHTML)
                    for x in RawHtml:
                        print(x)
                        if f"<{InputTag}>" in x:
                            
                            tags.append(f"Line {RawHtml.index(x)+1}: {x}")

                    print(tags)
                    if len(tags) > 1:
                        break
                    
                else:
                    print(f"Could not find {InputTag} in this document.")
            else:
                print("Please input a valid tag.")
        
        # Print Tags
        for i in tags:
            print(i)
            
        # Ask if the user wants to save the tags
        UserSave = input("\nSave Tags?\n>")
        if UserSave.lower().startswith("y"):

            UserName = os.environ['REPL_OWNER']
            
            print("Feature Undone!")
            time.sleep(2)
            End = input("\nEnd Program?\n>")
            if End.lower().startswith("y"):
                break
        else:
            End = input("\nEnd Program?\n>")
            if End.lower().startswith("y"):
                break


    else:
        print(r"Due to compability issues, you must input an Https website.")

        End = input("\nEnd Program?\n>")
        if End.lower().startswith("y"):
            break
            
                