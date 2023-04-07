class SVG:
    def __init__(self):
        self.code = []

    def line(self, start_x, start_y, end_x, end_y, color='black'):
        self.code.append(f'<line x1="{start_x}" y1="{start_y}" x2="{end_x}" y2="{end_y}" stroke="{color}" />')

    def circle(self, x, y, r=1, color='black'):
        self.code.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" />')

    def save(self, filename, width, height):
        self.code.insert(0, f'<svg version="1.1" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">')
        self.code.append(f'</svg>')
        with open(filename, 'w') as f:
            for line in self.code:
                f.write(line)


svg = SVG()

svg.line(10, 10, 60, 10, color='black')
svg.line(60, 10, 60, 60, color='black')
svg.line(60, 60, 10, 60, color='black')
svg.line(10, 60, 10, 10, color='black')

svg.circle(10, 10, r=5, color='red')
svg.circle(60, 10, r=5, color='red')
svg.circle(60, 60, r=5, color='red')
svg.circle(10, 60, r=5, color='red')

svg.save('pic.svg', 100, 100)
