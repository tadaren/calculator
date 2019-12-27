from enum import Enum, auto
from dataclasses import dataclass

ans = 0

class TokenType(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    MOD = auto()
    POW = auto()
    STAB = auto()
    ENDB = auto()
    ANS = auto()
    NUM = auto()
    END = auto()

class Symbol(Enum):
    START = auto()
    EXPR = auto()
    TERM = auto()
    SNUM = auto()
    POWER = auto()
    FACTOR = auto()


action_goto = [
    {Symbol.START: 0},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.EXPR: 2, Symbol.TERM: 3, Symbol.SNUM: 4, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('s', 12), TokenType.SUB: ('s', 13), TokenType.END: ('r', 0)},
    {TokenType.ADD: ('r', 1), TokenType.SUB: ('r', 1), TokenType.MUL: ('s', 14), TokenType.DIV: ('s', 15), TokenType.MOD: ('s', 16), TokenType.ENDB: ('r', 1), TokenType.END: ('r', 1)},
    {TokenType.ADD: ('r', 4), TokenType.SUB: ('r', 4), TokenType.MUL: ('r', 4), TokenType.DIV: ('r', 4), TokenType.MOD: ('r', 4), TokenType.ENDB: ('r', 4), TokenType.END: ('r', 4)},
    {TokenType.ADD: ('r', 8), TokenType.SUB: ('r', 8), TokenType.MUL: ('r', 8), TokenType.DIV: ('r', 8), TokenType.MOD: ('r', 8), TokenType.ENDB: ('r', 8), TokenType.END: ('r', 8)},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.SNUM: 17, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.SNUM: 18, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('r', 11), TokenType.SUB: ('r', 11), TokenType.MUL: ('r', 11), TokenType.DIV: ('r', 11), TokenType.MOD: ('r', 11), TokenType.ENDB: ('r', 11), TokenType.POW: ('s', 19), TokenType.END: ('r', 11)},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.EXPR: 20, Symbol.TERM: 3, Symbol.SNUM: 4, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('r', 14), TokenType.SUB: ('r', 14), TokenType.MUL: ('r', 14), TokenType.DIV: ('r', 14), TokenType.MOD: ('r', 14), TokenType.ENDB: ('r', 14), TokenType.POW: ('r', 14), TokenType.END: ('r', 14)},
    {TokenType.ADD: ('r', 15), TokenType.SUB: ('r', 15), TokenType.MUL: ('r', 15), TokenType.DIV: ('r', 15), TokenType.MOD: ('r', 15), TokenType.ENDB: ('r', 15), TokenType.POW: ('r', 15), TokenType.END: ('r', 15)},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.TERM: 21, Symbol.SNUM: 4, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.TERM: 22, Symbol.SNUM: 4, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.SNUM: 23, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.SNUM: 24, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.SNUM: 25, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('r', 9), TokenType.SUB: ('r', 9), TokenType.MUL: ('r', 9), TokenType.DIV: ('r', 9), TokenType.MOD: ('r', 9), TokenType.ENDB: ('r', 9), TokenType.POW: ('r', 9), TokenType.END: ('r', 9)},
    {TokenType.ADD: ('r', 10), TokenType.SUB: ('r', 10), TokenType.MUL: ('r', 10), TokenType.DIV: ('r', 10), TokenType.MOD: ('r', 10), TokenType.ENDB: ('r', 10), TokenType.POW: ('r', 10), TokenType.END: ('r', 10)},
    {TokenType.ADD: ('s', 6), TokenType.SUB: ('s', 7), TokenType.STAB: ('s', 9), TokenType.ANS: ('s', 10), TokenType.NUM: ('s', 11), Symbol.SNUM: 26, Symbol.POWER: 5, Symbol.FACTOR: 8},
    {TokenType.ADD: ('s', 12), TokenType.SUB: ('s', 13), TokenType.ENDB: ('s', 27)},
    {TokenType.ADD: ('r', 2), TokenType.SUB: ('r', 2), TokenType.MUL: ('s', 14), TokenType.DIV: ('s', 15), TokenType.MOD: ('s', 16), TokenType.ENDB: ('r', 2), TokenType.END: ('r', 2)},
    {TokenType.ADD: ('r', 3), TokenType.SUB: ('r', 3), TokenType.MUL: ('s', 14), TokenType.DIV: ('s', 15), TokenType.MOD: ('s', 16), TokenType.ENDB: ('r', 3), TokenType.END: ('r', 3)},
    {TokenType.ADD: ('r', 5), TokenType.SUB: ('r', 5), TokenType.MUL: ('r', 5), TokenType.DIV: ('r', 5), TokenType.MOD: ('r', 5), TokenType.ENDB: ('r', 5), TokenType.END: ('r', 5)},
    {TokenType.ADD: ('r', 6), TokenType.SUB: ('r', 6), TokenType.MUL: ('r', 6), TokenType.DIV: ('r', 6), TokenType.MOD: ('r', 6), TokenType.ENDB: ('r', 6), TokenType.END: ('r', 6)},
    {TokenType.ADD: ('r', 7), TokenType.SUB: ('r', 7), TokenType.MUL: ('r', 7), TokenType.DIV: ('r', 7), TokenType.MOD: ('r', 7), TokenType.ENDB: ('r', 7), TokenType.END: ('r', 7)},
    {TokenType.ADD: ('r', 12), TokenType.SUB: ('r', 12), TokenType.MUL: ('r', 12), TokenType.DIV: ('r', 12), TokenType.MOD: ('r', 12), TokenType.ENDB: ('r', 12), TokenType.END: ('r', 12)},
    {TokenType.ADD: ('r', 13), TokenType.SUB: ('r', 13), TokenType.MUL: ('r', 13), TokenType.DIV: ('r', 13), TokenType.MOD: ('r', 13), TokenType.ENDB: ('r', 13), TokenType.POW: ('r', 13), TokenType.END: ('r', 13)},
]


def power(f, p, sn):
    sn = sn.evaluate()
    if sn < 0:
        raise ValueError("error")
    return f.evaluate() ** sn

rules = [
    (1, Symbol.START, lambda e: e.evaluate()),
    (1, Symbol.EXPR, lambda t: t.evaluate()),
    (3, Symbol.EXPR, lambda e, a, t: e.evaluate() + t.evaluate()),
    (3, Symbol.EXPR, lambda e, s, t: e.evaluate() - t.evaluate()),
    (1, Symbol.TERM, lambda sn: sn.evaluate()),
    (3, Symbol.TERM, lambda t, m, sn: t.evaluate() * sn.evaluate()),
    (3, Symbol.TERM, lambda t, d, sn: t.evaluate() // sn.evaluate()),
    (3, Symbol.TERM, lambda t, m, sn: t.evaluate() % sn.evaluate()),
    (1, Symbol.SNUM, lambda p: p.evaluate()),
    (2, Symbol.SNUM, lambda a, sn: sn.evaluate()),
    (2, Symbol.SNUM, lambda s, sn: -sn.evaluate()),
    (1, Symbol.POWER, lambda f: f.evaluate()),
    (3, Symbol.POWER, power),
    (3, Symbol.FACTOR, lambda start, e, end: e.evaluate()),
    (1, Symbol.FACTOR, lambda a: ans),
    (1, Symbol.FACTOR, lambda n: n.num),
]


class Expr:
    def __init__(self, symbol, expr, arg):
        self.symbol = symbol
        self.e = expr
        self.arg = arg
    
    def evaluate(self):
        ret = self.e(*self.arg)
        return ret

    def __str__(self):
        # return f'Expr({self.symbol}, {self.arg})'
        return f'Expr({self.symbol})'


class Token:
    def __init__(self, type_, *arg):
        self.type_ = type_
        if self.type_ == TokenType.NUM:
            self.num = arg[0]
    
    def __str__(self):
        if self.type_ == TokenType.NUM:
            return str(self.type_) + ' ' + str(self.num)
        return str(self.type_)


class Tokenizer:
    def __init__(self, line):
        self.token_map = {
            '+': TokenType.ADD,
            '-': TokenType.SUB,
            '*': TokenType.MUL,
            '/': TokenType.DIV,
            '%': TokenType.MOD,
            '^': TokenType.POW,
            '(': TokenType.STAB,
            ')': TokenType.ENDB,
            'ans': TokenType.ANS
        }
        self.line = line.replace(' ', '')
        self.index = 0
    
    def next_token(self):
        num_start_index = self.index
        num_end_index = self.index
        while self.index < len(self.line) and num_end_index < len(self.line) and str.isdecimal(self.line[num_start_index:num_end_index+1]):
            num_end_index += 1
        if str.isdecimal(self.line[num_start_index:num_end_index]):
            self.index = num_end_index
            return Token(TokenType.NUM, int(self.line[num_start_index:num_end_index]))
        if self.index < len(self.line):
            for k, v in self.token_map.items():
                if self.line[self.index:self.index+len(k)] == k:
                    token_type = v
                    token = Token(token_type)
                    self.index += len(k)
                    return token
        return Token(TokenType.END)


class Parser:
    def __init__(self, line):
        self.tokenizer = Tokenizer(line)
        self.stack = [1]

    def parse(self):
        next_token = self.tokenizer.next_token()
        while True:
            state = self.stack[-1]
            action = action_goto[state].get(next_token.type_, None)
            if action is None:
                # print([str(e) for e in self.stack])
                # print(f'state: {state}, type: {next_token.type_}')
                # print(f'action: {action}')
                raise SyntaxError('error')
            mode, index = action
            if mode == 's':
                self.stack.append(next_token)
                self.stack.append(index)
                next_token = self.tokenizer.next_token()
            elif mode == 'r':
                num, symbol, rule = rules[index]
                arg = self.stack[-num*2:]
                # print(f'arg: {arg[::2]}')
                r = Expr(symbol, rule, arg[::2])
                if symbol == Symbol.START:
                    return r
                del self.stack[-num*2:]
                next_state = action_goto[self.stack[-1]][symbol]
                self.stack.append(r)
                self.stack.append(next_state)


def calc(line):
    parser = Parser(line)
    return parser.parse().evaluate()

 
def main():
    global ans
    while True:
        line = input('> ').strip()
        if line == 'exit':
            break
        try:
            ans = calc(line)
            print('=', ans)
        except Exception as e:
            print('error')


if __name__ == "__main__":
    main()
