from contextlib import contextmanager


class HTML:
    _doc = ''

    @contextmanager
    def body(self):
        body = HTMLElement('body')
        self._doc += f'<{body.name}>\n'
        yield
        self._doc += f'</{body.name}>\n'

    @contextmanager
    def div(self):
        div = HTMLElement('div')
        self._doc += f'<{div.name}>\n'
        yield
        self._doc += f'</{div.name}>\n'

    def p(self, text):
        self._doc += f'<p>{text}</p>\n'

    def __str__(self):
        return self._doc


class HTMLElement:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    html = HTML()
    with html.body():
        with html.div():
            html.p('First string.')
            html.p('Second string.')
        with html.div():
            html.p('Third string.')
    print(html)