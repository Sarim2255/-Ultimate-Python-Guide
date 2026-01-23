questions = [
    ["Which is the largest desert in the world?", "Gobi", "Sahara", "Antarctic Desert", "Kalahari", 3,"Antarctic Desert"],
    ["Who is known as the father of internet?", "Bell Gates", "Vint Cerf", "Tim Berners-Lee", "Steve Jobs", 2,"Vint Cerf"],
    ["Which country has the most number of islands?","Indonesia","Canada","Sweden","Philippines", 3, "Sweden"],
    ["Mount Everest lies between which two countries?", "China and India", "Nepal and China", "Nepal and India", "India and Bhutan", 2, "Nepal and China"],
    ["Who invented the World Wide Web (WWW)?", "Dennis Ritchie", "Charles Babbage", "Tim Berners-Lee", "Alan Turing", 3, "Tim Berners-Lee"],


    ["Which planet has the most moons?", "Jupiter", "Saturn", "Uranus", "Neptune", 2, "Saturn"],
    ["The Great Wall of China was mainly built to protect against which group?", "Mongols", "Persians", "Turks", "Russians", 1, "Mongols"],
    ["Which is the longest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", 1, "Amazon River"],
    ["Who is Bruce Lee?", "Martial Artist and Actor", "Austronaut", "Singer","Influencer", 1, "Martial Artist and Actor"],
    ["In which country is the ancient city of Petra located?", "Turkey","Greece", "Jordan","Egypt", 4, "Jordan"],
    ["Which country is called the 'Land of the Rising Sun'?"," China", "Japan", "Thailand", "South Korea", 2, "Japan"]
]

prizes = [1000, 5000, 10000, 25000, 50000, 100000, 150000, 250000, 500000, 750000, 1000000]
sum = 0
i = 0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    print("1 for a, 2 for b, 3 for c, 4 for d")
    a = int(input("Enter your answer: "))
    if(question[5]==a):
        print("Correct Answer...")
    else: 
        print(f"Incorrect! Correct Answer -> {question[6]}")
        print("Better Luck Next Time")
        break
    sum += prizes[i]
    print(f"You won {prizes[i]}")
    i +=1