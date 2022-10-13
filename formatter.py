'''text formatters. these are function stored in a dictionary that will perform formatting.'''

def sift_num(text):
    label = ' '.join([word for word in text.split() if not word.replace(',','')
                                                        .replace('.','')
                                                        .replace('-','').isnumeric()])
    numbers = ' '.join([word for word in text.split() if word.replace(',','')
                                                        .replace('.','')
                                                        .replace('-','').isnumeric()])
    return label, numbers

def format_income(income):
    num_space = [7, 12]
    labels, numbers = sift_num(income)
    labels = labels.ljust(16)
    numbers = text_spacer(*numbers.strip().split(), spaces=num_space)
    return labels + numbers

def format_partition(partition):
    return partition.rjust(3)    

def format_deductions(deductions):
    num_space = [9, 11]
    labels, numbers = sift_num(deductions)
    labels = labels.rjust(20)
    numbersplit = numbers.strip().split()
    numbers = text_spacer(*numbersplit, spaces=num_space)
    return labels + numbers

def format_10(*args):
    income, partition, deductions = ' '.join(args).partition('|')
    if income and deductions:
        income = format_income(income)
        deductions = format_deductions(deductions)
        return income + format_partition(partition) + deductions

    if deductions and not income:
        deductions = format_deductions(deductions)
        return format_divider(*partition) + deductions

    if income and not deductions:
        income = format_income(income)
        return income + format_partition(partition)

    if not income and not deductions:
        return format_divider(*partition)

def format_divider(*args):
    arg = args[0]
    return arg.rjust(38)

def text_spacer(*args, spaces=None):
    placeholder = ''

    for arg,space in zip(args,spaces):
        placeholder += arg.rjust(space)
    return placeholder

format_header = {0: lambda a, b, c,: a.rjust(54) + 
                                     b.rjust(8) +
                                     c.rjust(12),
                1: lambda a, b, c, d: '{}     {} {} {}'.format(a,b,c,d),
                2: lambda x, y, z: '{} {} {}'.format(x,y,z),
                3: lambda a, b: a.rjust(39) + 
                                b.rjust(6),
                4:  lambda a, b, c, d: a.rjust(34) + 
                                       b.rjust(5) +
                                       c.rjust(9) +
                                       d.rjust(5) +
                                       '\n' * 2,
                5: lambda a, b, c, d: a.rjust(22) + 
                                      b.rjust(35) +
                                      c.rjust(2) +
                                      d.rjust(12),
                6:lambda x: x,
                7:lambda a, b, c, d, e, f, g: a.rjust(9) +
                                              b.rjust(13) +
                                              c.rjust(11) +
                                              d.rjust(5) +
                                              e.rjust(7) +
                                              f.rjust(19) +
                                              g.rjust(11),
                8:lambda x: x}

format_content = {  9: format_10,
                    10: format_10,
                    11: format_10,
                    12: format_10,
                    13: format_10,
                    14: format_10,
                    15: format_10,
                    16: format_10,
                    }

format_summary = {17:lambda x: x,
                  18:lambda a, b: a.rjust(8) + 
                                  b.rjust(11) +
                                  '\n' * 5,
                  19:lambda a, b, c, d, e, f: a.rjust(5) + 
                                              b.rjust(9) + 
                                              c.rjust(15) + 
                                              d.rjust(16) +
                                              e.rjust(11) +
                                              f.rjust(16),
                  20:lambda a, b, c: a.rjust(3) + 
                                     b.rjust(4) + 
                                     c.rjust(22),
                  21:lambda a, b, c, d, e, f, g: a.rjust(3) + 
                                                b.rjust(6) + 
                                                c.rjust(20) + 
                                                d.rjust(14) +
                                                e.rjust(4) +
                                                f.rjust(5) +
                                                g.rjust(20),
                  22:lambda a, b, c: a.rjust(3) + 
                                     b.rjust(11) + 
                                     c.rjust(15) + 
                                     '\n',
                  23:lambda a, b, c, d, e, f, g, h, i , j, k: a.rjust(7) + 
                                                              b.rjust(4) + 
                                                              c.rjust(6) + 
                                                              d.rjust(7) +
                                                              e.rjust(8) +
                                                              f.rjust(4) +
                                                              g.rjust(7) +
                                                              h.rjust(3) + 
                                                              i.rjust(11) + 
                                                              j.rjust(13) + 
                                                              k.rjust(4),
                  24:lambda a, b: a.rjust(72) + 
                                  b.rjust(2)
}