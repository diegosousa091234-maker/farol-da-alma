import sys
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter

def detectar_formato(caminho):
    try:
        with Image.open(caminho) as img:
            return img.format or "JPEG", img.size, img.mode
    except Exception as e:
        return None, None, str(e)

def aplicar_queimadura(imagem):
    im = imagem.convert("RGB")
    w, h = im.size
    im = ImageEnhance.Contrast(im).enhance(1.35)
    im = ImageEnhance.Color(im).enhance(1.45)
    ouro = Image.new("RGB", im.size, (212, 175, 55))
    im = Image.blend(im, ouro, 0.14)
    # Vinheta maçarico
    vign = Image.new("L", (w,h))
    cx, cy = w//2, h//2
    maxd = (cx*cx + cy*cy)**0.5
    pix = []
    for y in range(h):
        for x in range(w):
            d = ((x-cx)**2 + (y-cy)**2)**0.5 / maxd
            v = 255 - int((d**1.8)*190)
            pix.append(max(0, min(255, v)))
    vign.putdata(pix)
    vign = vign.filter(ImageFilter.GaussianBlur(radius=w*0.02))
    dark = Image.new("RGB", im.size, (8,6,18))
    im_q = Image.composite(im, dark, vign)
    im = Image.blend(im, im_q, 0.28)
    im = ImageEnhance.Brightness(im).enhance(1.08)
    return ImageEnhance.Sharpness(im).enhance(1.15)

def processar(caminho):
    caminho = Path(caminho)
    fmt, size, mode = detectar_formato(caminho)
    if not fmt:
        print(f"❌ Não é imagem: {caminho}")
        return
    print(f"\n📖 {caminho.name} | {fmt} | {size} | {mode}")
    with Image.open(caminho) as img:
        print(" 🔥 Queimadura de maçarico...")
        res = aplicar_queimadura(img)
        saida = caminho.parent / f"{caminho.stem}_queimado{caminho.suffix or '.jpg'}"
        res.save(saida, quality=95)
        print(f" ✅ Salvo: {saida}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 queimador.py /caminho/para/imagem.jpg")
    else:
        processar(sys.argv[1])
