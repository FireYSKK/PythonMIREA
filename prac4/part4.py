class Body:
    def __init__(self, document):
        self.document = document

    def __enter__(self):
        self.document.code.append("\t" * self.document.align + "<body>")
        self.document.align += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.document.align -= 1
        self.document.code.append("\t" * self.document.align + "</body>")


class Div:
    def __init__(self, document):
        self.document = document

    def __enter__(self):
        self.document.code.append("\t" * self.document.align + "<div>")
        self.document.align += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.document.align -= 1
        self.document.code.append("\t" * self.document.align + "</div>")


class HTML:
    def __init__(self):
        self.code = []
        self.align = 0

    def body(self):
        return Body(self)

    def div(self):
        return Div(self)

    def p(self, text: str):
        self.code.append("\t" * self.align + "<p>" + text + "</p>")

    def get_code(self):
        print(*self.code, sep='\n')


html = HTML()

with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

html.get_code()
