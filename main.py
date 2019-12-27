def power(self, x):
    if x < 0:
        raise ValueError('error')
    return super().__pow__(x)

def main():
    int.__pow__ = power
    ans = 0
    while True:
        line = input('> ')
        if line == 'exit':
            break
        try:
            ans = eval(line.replace('^', '**').replace('/', '//'))
        except:
            print('error')
            continue
        print('=', ans)

if __name__ == "__main__":
    main()