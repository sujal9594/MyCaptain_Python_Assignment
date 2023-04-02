def most_frequent(string):
   
    freq = {}

   
    for char in string:
        
        if char in freq:
            freq[char] += 1
        
        else:
            freq[char] = 1

   
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

   
    for char, count in sorted_freq:
        print(char, count)
