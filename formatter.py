format_15 = {0: lambda a, b, c,: a.rjust(54) + 
                                 b.rjust(8) +
                                 c.rjust(12) + 
                                '\n',
          1: lambda a, b, c, d: '{}     {} {} {}\n'.format(a,b,c,d),
          2: lambda x, y, z: '{} {} {}\n'.format(x,y,z),
          3: lambda a, b: a.rjust(39) + 
                          b.rjust(6) +
                          '\n',
          4:  lambda a, b, c, d: a.rjust(34) + 
                                 b.rjust(5) +
                                 c.rjust(9) +
                                 d.rjust(5) +
                                 '\n' * 3,
          5: lambda a, b, c, d: a.rjust(22) + 
                                b.rjust(35) +
                                c.rjust(2) +
                                d.rjust(12) +
                                '\n',
          6:lambda x: x + '\n',
          7:lambda a, b, c, d, e, f, g: a.rjust(9) + 
                                         b.rjust(13) + 
                                         c.rjust(11) + 
                                         d.rjust(5) +
                                         e.rjust(7) +
                                         f.rjust(19) +
                                         g.rjust(11) +
                                         '\n',
          8:lambda x: x + '\n',
          9:lambda a, b, c, d, e, f, g, h, i , j, k, l: a.rjust(6) + 
                                                         b.rjust(6) + 
                                                         c.rjust(5) + 
                                                         d.rjust(6) +
                                                         e.rjust(12) +
                                                         f.rjust(3) +
                                                         g.rjust(9) +
                                                         h.rjust(4) + 
                                                         i.rjust(4) + 
                                                         j.rjust(3) + 
                                                         k.rjust(9) +
                                                         l.rjust(11) +
                                                        '\n',
          10:lambda a, b, c, d, e, f: a.rjust(38) + 
                                         b.rjust(7) + 
                                         c.rjust(3) + 
                                         d.rjust(10) +
                                         e.rjust(9) +
                                         f.rjust(11) +
                                         '\n',
          11:lambda a, b, c, d, e, f: a.rjust(38) + 
                                         b.rjust(7) + 
                                         c.rjust(3) + 
                                         d.rjust(10) +
                                         e.rjust(9) +
                                         f.rjust(11) +
                                         '\n',
          12:lambda a, b, c, d, e, f: a.rjust(38) + 
                                         b.rjust(6) + 
                                         c.rjust(5) + 
                                         d.rjust(9) +
                                         e.rjust(9) +
                                         f.rjust(11) +
                                         '\n',
          13:lambda a, b, c, d, e, f: a.rjust(38) + 
                                         b.rjust(8) + 
                                         c.rjust(3) + 
                                         d.rjust(9) +
                                         e.rjust(9) +
                                         f.rjust(11) +
                                         '\n',
          14:lambda a: a.rjust(38) + '\n',
          15:lambda a: a.rjust(38) + '\n',
          16:lambda a: a.rjust(38) + '\n',
          17:lambda x: x + '\n',
          18:lambda a, b: a.rjust(8) + 
                          b.rjust(11) +
                          '\n' * 6,
          19:lambda a, b, c, d, e, f: a.rjust(5) + 
                                         b.rjust(9) + 
                                         c.rjust(15) + 
                                         d.rjust(16) +
                                         e.rjust(11) +
                                         f.rjust(15) +
                                         '\n',
          20:lambda a, b, c: a.rjust(3) + 
                             b.rjust(4) + 
                             c.rjust(22) + 
                             '\n',
          21:lambda a, b, c, d, e, f, g: a.rjust(3) + 
                                         b.rjust(6) + 
                                         c.rjust(20) + 
                                         d.rjust(14) +
                                         e.rjust(4) +
                                         f.rjust(5) +
                                         g.rjust(20) +
                                         '\n',
          22:lambda a, b, c: a.rjust(3) + 
                             b.rjust(11) + 
                             c.rjust(15) + 
                             '\n' * 2,
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
                                                         k.rjust(4) +
                                                        '\n',
          24:lambda a, b: a.rjust(72) + 
                          b.rjust(2)}

format_30 = {0: lambda a, b, c,: a.rjust(54) + 
                                 b.rjust(8) +
                                 c.rjust(12) + 
                                '\n',
          1: lambda a, b, c, d: '{}     {} {} {}\n'.format(a,b,c,d),
          2: lambda x, y, z: '{} {} {}\n'.format(x,y,z),
          3: lambda a, b: a.rjust(39) + 
                          b.rjust(6) +
                          '\n',
          4:  lambda a, b, c, d: a.rjust(34) + 
                                 b.rjust(5) +
                                 c.rjust(9) +
                                 d.rjust(5) +
                                 '\n' * 3,
          5: lambda a, b, c, d: a.rjust(22) + 
                                b.rjust(35) +
                                c.rjust(2) +
                                d.rjust(12) +
                                '\n',
          6:lambda x: x + '\n',
          7:lambda a, b, c, d, e, f, g: a.rjust(9) + 
                                         b.rjust(13) + 
                                         c.rjust(11) + 
                                         d.rjust(5) +
                                         e.rjust(7) +
                                         f.rjust(19) +
                                         g.rjust(11) +
                                         '\n',
          8:lambda x: x + '\n',
          9:lambda a, b, c, d, e, f, g, h, i , j, k, l: a.rjust(6) + 
                                                         b.rjust(6) + 
                                                         c.rjust(5) + 
                                                         d.rjust(6) +
                                                         e.rjust(12) +
                                                         f.rjust(3) +
                                                         g.rjust(9) +
                                                         h.rjust(4) + 
                                                         i.rjust(4) + 
                                                         j.rjust(3) + 
                                                         k.rjust(9) +
                                                         l.rjust(11) +
                                                        '\n',
          10:lambda a, b, c, d, e, f: a.rjust(38) + 
                                         b.rjust(7) + 
                                         c.rjust(3) + 
                                         d.rjust(10) +
                                         e.rjust(9) +
                                         f.rjust(11) +
                                         '\n',
          11:lambda a, b, c, d, e, f: a.rjust(38) + 
                                         b.rjust(7) + 
                                         c.rjust(3) + 
                                         d.rjust(10) +
                                         e.rjust(9) +
                                         f.rjust(11) +
                                         '\n',
          12:lambda a, b, c, d, e, f: a.rjust(38) + 
                                         b.rjust(6) + 
                                         c.rjust(5) + 
                                         d.rjust(9) +
                                         e.rjust(9) +
                                         f.rjust(11) +
                                         '\n',
          13:lambda a, b, c, d, e, f: a.rjust(38) + 
                                         b.rjust(8) + 
                                         c.rjust(3) + 
                                         d.rjust(9) +
                                         e.rjust(9) +
                                         f.rjust(11) +
                                         '\n',
          14:lambda a: a.rjust(38) + '\n',
          15:lambda a: a.rjust(38) + '\n',
          16:lambda a: a.rjust(38) + '\n',
          17:lambda x: x + '\n',
          18:lambda a, b: a.rjust(8) + 
                          b.rjust(11) +
                          '\n' * 6,
          19:lambda a, b, c, d, e, f: a.rjust(5) + 
                                         b.rjust(9) + 
                                         c.rjust(15) + 
                                         d.rjust(16) +
                                         e.rjust(11) +
                                         f.rjust(15) +
                                         '\n',
          20:lambda a, b, c: a.rjust(3) + 
                             b.rjust(4) + 
                             c.rjust(22) + 
                             '\n',
          21:lambda a, b, c, d, e, f, g: a.rjust(3) + 
                                         b.rjust(6) + 
                                         c.rjust(20) + 
                                         d.rjust(14) +
                                         e.rjust(4) +
                                         f.rjust(5) +
                                         g.rjust(20) +
                                         '\n',
          22:lambda a, b, c: a.rjust(3) + 
                             b.rjust(11) + 
                             c.rjust(15) + 
                             '\n' * 2,
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
                                                         k.rjust(4) +
                                                        '\n',
          24:lambda a, b: a.rjust(72) + 
                          b.rjust(2)}