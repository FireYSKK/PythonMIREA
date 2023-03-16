from dataclasses import dataclass
import matplotlib.pyplot as plt

# Dots should be nullprint characters
from matplotlib.patches import ArrowStyle

pairs = "..LEXEGEZACEBISOUSESARMAINDIREA.ERATENBERALAVETIEDORQUANTEISRION"


@dataclass
class FastSeedType:
    a: int
    b: int
    c: int
    d: int


@dataclass
class SeedType:
    w0: int
    w1: int
    w2: int


@dataclass
class PlanSys:
    x: int
    y: int
    economy: int
    govtype: int
    techlev: int
    population: int
    productivity: int
    radius: int
    goatsoupseed: FastSeedType
    name: str


def tweakseed(s: SeedType) -> None:
    temp = (s.w0 + s.w1 + s.w2) & 0xFFFF
    s.w0 = s.w1
    s.w1 = s.w2
    s.w2 = temp


def makesystem(s: SeedType) -> PlanSys:
    longnameflag = s.w0 & 64

    x = s.w1 >> 8
    y = s.w0 >> 8

    govtype = (s.w1 >> 3) & 7

    economy = (s.w0 >> 8) & 7
    if govtype <= 1:
        economy = economy | 2

    techlev = ((s.w1 >> 8) & 3) + (economy ^ 7)
    techlev += (govtype >> 1)
    if (govtype & 1) == 1:
        techlev += 1

    population = 4 * techlev + economy
    population += govtype + 1

    productivity = ((economy ^ 7) + 3) * (govtype + 4)
    productivity *= population * 8

    radius = 256 * (((s.w2 >> 8) & 15) + 11) + x

    goatsoupseed = FastSeedType(
        a=s.w1 & 0xFF,
        b=s.w1 >> 8,
        c=s.w2 & 0xFF,
        d=s.w2 >> 8,
    )

    pair1 = 2 * ((s.w2 >> 8) & 31)
    tweakseed(s)
    pair2 = 2 * ((s.w2 >> 8) & 31)
    tweakseed(s)
    pair3 = 2 * ((s.w2 >> 8) & 31)
    tweakseed(s)
    pair4 = 2 * ((s.w2 >> 8) & 31)
    tweakseed(s)

    name = ""
    name += pairs[pair1:pair1 + 2]
    name += pairs[pair2:pair2 + 2]
    name += pairs[pair3:pair3 + 2]

    if longnameflag != 0:
        name += pairs[pair4:pair4 + 2]

    name = name.replace('.', '')

    thissys = PlanSys(
        x=x,
        y=y,
        economy=economy,
        govtype=govtype,
        techlev=techlev,
        population=population,
        productivity=productivity,
        radius=radius,
        goatsoupseed=goatsoupseed,
        name=name
    )

    return thissys


x_offset, y_offset = 2, 1

world_map, ax = plt.subplots(facecolor='#a9a9a9')
world_map.subplots_adjust(bottom=0.03, top=0.97, left=0.02, right=0.98)
ax.set_facecolor('#000000')

seedtype = SeedType(0x5A4A, 0x0248, 0xB753)
for i in range(255):
    planet = makesystem(seedtype)
    ax.scatter(planet.x, -planet.y, s=planet.radius // 2550, c=['#ffffff'])
    ax.annotate(planet.name,
                xy=(planet.x, -planet.y),
                xytext=(planet.x + x_offset, -planet.y + y_offset),
                ha="left", va="bottom", color='#ffffff', size=7,
                arrowprops=dict(arrowstyle=ArrowStyle("Fancy", head_length=0, head_width=0, tail_width=0)))

plt.show()
