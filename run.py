words = []
with open('wordlist.txt', 'r') as f:
    words = f.readlines()
    words = [i.removesuffix('\n') for i in words]

words_cpy = words.copy()



current_guess = 'crane'
valid_input = ['g', 'y', 'b']
status = ''

while(1):
    print(f"Enter {current_guess.upper()} as a guess!")
    res = input("Did I get it right? Enter 'I' for invalid word(y/N): ")
    
    if res.lower() == 'i':
        words.pop(0)
        words_cpy.remove(current_guess)
        with open('wordlist.txt', 'w') as f:
            for i in words_cpy:
                f.write(f"{i}\n")
                
        if len(words) > 0:        
            current_guess = words[0]
        else:
            print("Sorry can't help!")  
            break
        continue
    
    elif res.lower() != 'y':
        while(1):
            status = input("Input single 5 lettered string denoting the status! G-Green Y-Yellow B-Black:\n")
            if len(status) != 5:
                print("The string need to be 5 character long! Try again!")
            for letter in status:
                if letter.lower() not in valid_input:
                    print("Invalid input! String can only contain g,y,b Try again!")
                    break 
            else:
                break
         
        for i, letter in enumerate(status):
            if letter.lower() == 'g':
                words = [j for j in words if j[i] == current_guess[i]]

                
            elif letter.lower() == 'y':
                words = [j for j in words if j[i] != current_guess[i] and current_guess[i] in j]

                
            else:
                
                if current_guess.count(current_guess[i]) == 1:
                    words = [j for j in words if current_guess[i] not in j ]
                
                else:
                    words = [j for j in words if j.count(current_guess[i]) < current_guess.count(current_guess[i])]


        if len(words) < 6 and len(words) > 1:
            print("Possible Solutions:")         
            print('\n'.join(words))
        
        if len(words) > 0:        
            current_guess = words[0]
        else:
            new_word = input("Sorry can't help! Enter the answer if you figure it out!\n")
            
            if new_word:
                words_cpy.append(new_word)
                
                with open('wordlist.txt', 'w') as f:
                    for i in words_cpy:
                        f.write(f"{i}\n") 
            break
        
        
    else:
        print("You got it! Good Job!")
        break