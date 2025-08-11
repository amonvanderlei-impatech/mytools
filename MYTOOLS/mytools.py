PI_INT = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT =  "2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def num_real(len: int, num_int: str):
    len = abs(len)

    if len > 100:
        len = 100
    
    if len == 0:
        return num_int[:len+1]    
    
    return num_int[:len+2]

def pi_real(len: int):
    return num_real(len, PI_INT)

def e_real(len: int):
    return num_real(len, E_INT)
