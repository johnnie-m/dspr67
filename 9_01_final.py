import numpy as np


# Setting up random range:
minvalue = 1
maxvalue = 100


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
    predict_number = (upperLimit - lowerLimit) / 2
            
    while True:
        
        if predict_number > number:
            count += 1
            
            # Moving the RIGHT guessing range bound
            # to previous guess value      
            upperLimit = predict_number
            predict_number = np.random.randint(lowerLimit, upperLimit)                   
      
        elif predict_number < number:
            count += 1
            
            # Moving the LEFT guessing range limit
            # to previous guess value       
            lowerLimit = predict_number
            predict_number = np.random.randint(lowerLimit, upperLimit)            
            
        else:
            # Exit the cycle with the number guessed 
            break
    
    return count             

def average_score(predict_number):    
    #Finds average number of tries in 1000 runs   
        
    # Array of 1000 random numbers to be guessed:
    # (Un)quote the next line to fix(reset) random seed
    #np.random.seed(1)
    random_array = np.random.randint(minvalue, maxvalue, size=(1000))
    
    # Applying prediction func to random array:
    count_array = list(map(predict_number, random_array))
    
    # Average number of tries:
    score = int(np.mean(count_array))
    print(f'Your method finds the number in: {score} tries at an average')
    return score

if __name__ == '__main__':
    average_score(predict_number)