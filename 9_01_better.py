import numpy as np

# Setting up random range:
minvalue = 1
maxvalue = 10


def predict_number(number:int=1) -> int:
    
    # Setting up initial guessing range bounds: 
    lowerLimit = minvalue
    upperLimit = maxvalue
    
    count = 0 
    
    # The number to seek for:
    # (Un)quote the next line to fix(reset) random seed
    #np.random.seed(1)
    number = np.random.randint(minvalue, maxvalue)
    
    # First try - the middle of the range:
    predict_number = int(upperLimit + lowerLimit) / 2
            
    while True:
        
        if predict_number > number:
            count += 1
            #print(number, lowerLimit, upperLimit, predict_number)
            # Moving the RIGHT guessing range bound
            # to previous guess value      
            upperLimit = predict_number
            predict_number = int((upperLimit + lowerLimit) / 2)                   
      
        elif predict_number < number:
            count += 1
            #print(number, lowerLimit, upperLimit, predict_number)
            # Moving the LEFT guessing range limit
            # to previous guess value       
            lowerLimit = predict_number
            predict_number = int((upperLimit + lowerLimit) / 2)            
            
        else:
            # Exit the cycle with the number guessed 
            break
    
    return count             

def average_score(predict_number):    
    #Finds average number of tries in 1000 runs   
        
    # Array of 1000 random numbers to be guessed:
    # (Un)quote the next line to fix(reset) random seed
    #np.random.seed(1)
    random_array = np.random.randint(minvalue, maxvalue, size=(10))
    
    # Applying prediction func to random array:
    count_array = list(map(predict_number, random_array))
    
    # Average number of tries:
    score = int(np.mean(count_array))
    print(f'Your method finds the number in: {score} tries at an average')
    return score

average_score(predict_number)