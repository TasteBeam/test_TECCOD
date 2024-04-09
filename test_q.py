from typing import List

def unique_num(num_list):
    return list(set(num_list))



def simple_num(left, right):
    s = []
    for num in range(left, right + 1):
        if num % 2 == 0:
            continue
        d = 3
        while d * d <= num and num % d != 0:
            d += 2
        if d * d > num:
            s.append(num)
    return s    



class Point():
    def __init__(self, x=0, y=0):
        if type(x) in (int, float) and type(y) in (int, float):
           self.__x = x
           self.__y = y

    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x    
            self.__y = y
        else:
            raise TypeError("x and y must be of type int or float")    

    def get_coord(self):
        return (self.__x, self.__y)    
    
    def get_distance(self, new_x, new_y):
        if type(new_x) in (int, float) and type(new_y) in (int, float):
            return (abs(new_x - self.__x), abs(new_y - self.__y))
        else:
            raise TypeError("new_x and new_y must be of type int or float")
        
def sort_list_by_len(spis: List[str]):
    new_s = sorted(spis, key=len)
    return sorted(new_s, key=len, reverse=True)


s = ['fdsfds', 'eqweqw', 'fseqwwfqfweg', 'popa', 'sadwqeweqewq']

print(sort_list_by_len(s))