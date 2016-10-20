def f(ham: 42, eggs: int = 'spam') -> 'Nothing to see here':
    print('Annotations:', f.__annotations__)
    print('Arguments:', ham, eggs)

f('wonderful')