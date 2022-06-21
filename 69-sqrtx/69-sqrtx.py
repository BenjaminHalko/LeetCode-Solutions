class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        last_guess= x/2
        while True:
            guess= (last_guess + x/last_guess)/2
            if abs(guess - last_guess) < 1:
                return int(guess)
            last_guess= guess