from functools import reduce


def indent_text(text, indent):
    return reduce(lambda line1,line2: '%s\n%s' % (line1, line2),
                  map(lambda line: (' ' * 4 * indent) + line,
                      text.splitlines()))