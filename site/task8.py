import re


def main(expr: str):
    d = dict()
    re_expr = r"define\s*`(\w+)\s*=\s*\{\s*([\-\d\s,]+)\}\."
    res = re.findall(re_expr, expr)
    for found in res:
        d[found[0]] = [int(num) for num in re.findall(r"-*\d+", found[1])]
    return d


print(main(
    "{ define `inbice= { 5294 , -8264 , 2080}. define `arvexe_205 ={ -3386, 7435}. define `tequan_887={6494 , 3150 }.}"))
print(main(
    "{ define `orla ={ -743 , -7331 ,7616 ,-9068 }. define `leveza = { 5714 , 3316, 2777 , -9845 }. define `teis= {"
    "6769 , 3586 }. define`esge = {-2341, 3957 }.}"))
