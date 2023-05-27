class Point(object):
    pass

p = Point()
#{!r}はreprを表示　{!s}はstr　
print('{0!r} {0} {0!s}'.format(p))

class Point2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point ({}, {}))'.format(self.x, self.y)

p2 = Point2(11,22)
print('{0!r}'.format(p2))
print('{0}'.format(p2))
print('{0!s}'.format(p2))