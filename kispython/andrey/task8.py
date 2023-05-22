import re


def main(input_str):
    # Находим все блоки
    blocks = re.findall(
        r'{(.+?)}\s*\|>\s*"(.+?)"',
        input_str, re.DOTALL)
    result = []
    # Разбиваем содержимое блоков
    for block in blocks:
        params = [p.strip() for p in block[0].split(",")]
        result.append((block[1], params))
    return result

print(main('( do opt { edce,ratied_563 , maarza_424 , quedra } |>"zaat". end,do\nopt{ rixe_655 , getite_65 , erre_86 } |> "didice". end, do opt {\nedbexe_313 , tianin_145 , velala_625 } |> "onaonbe". end, do\nopt{soa_875, reraare_313 }|> "xeerti_261". end,)'))
