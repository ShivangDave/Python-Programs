class fibonacci:
    def __init__(self):
        self.memo = [0,1]

    def fib(self,number):
        if number<=0:
            return 0
        elif number==1:
            return 1
        else:
            if len(self.memo)<=number:
                self.memo.insert(number,self.fib(number-1)+self.fib(number-2))
            else:
                self.memo[number] = self.fib(number-1)+self.fib(number-2)
        return self.memo[number]

if __name__ == '__main__':
    obj = fibonacci()
    print('Fibonacci sum is '+str(obj.fib(6)))
