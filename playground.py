from PIL import Image

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def rgb_color():
    im = Image.open('upload/moedas.jpg')
    pix = im.convert('RGB').getdata()
    size = im.size
    colors = {}
    # count = 0
    # for x in range(size[0]):
    for i in range(len(pix)):
        # count += 1
        if colors.get(pix[i]):
            colors[pix[i]]['count'] += 1
        else:
            colors[pix[i]] = {
                'count': 1,
                'hexadecimal': rgb2hex(r=pix[i][0], g=pix[i][1], b=pix[i][2]),
                'RGB': f"{pix[i][0]} {pix[i][1]} {pix[i][2]}"
            }
    pass
    count_validos = 0
    colors_result = {}
    for color in colors:
        c = colors[color]
        #irá contabilizar

        porcetagem = round(c['count']/len(pix)*100, 3)
        #irá pegar as cores que represente pelomenos 0.1 da imagem
        if porcetagem > 0.099:
            count_validos += c['count']
            colors_result[color] = c
    result = []
    for color in colors_result:
        c = colors_result[color]
        c['porcentagem'] = round(c['count']/count_validos*100, 3)
        result.append(c)
