phrases = 'Hello World !'

def occurence(phrase):
    count_dict = {} 
    for char in phrase:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict


print(occurence(phrases))


numbers = [10,20,30,40,60,110]

def moyenne(number):
    moyen = sum(number) / len(number)
    return moyen




def moyenneLoop(numbers):
    moy = 0
    for num in numbers:
        moy += num  
    moy /= len(numbers)  
    return moy


print(moyenneLoop(numbers))


tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]

def rechercheMinMax(tab) :
    min= 0
    max = 0
    
    for numMin in tab :
      if min < numMin :
          min = numMin
    for numMax in tab:
       if max > numMax :
           max = numMax
    my_dict = {"min": max, "max": min}
    return my_dict
print(rechercheMinMax(tableau))