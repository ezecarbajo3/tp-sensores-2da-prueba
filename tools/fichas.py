"""Genera las páginas de las hojas técnicas y los recuadros de la lectura guiada.

Para cada ficha:
  · renderiza a PNG las páginas seleccionadas (img/fichas/<ficha>-pNN.png)
  · calcula los recuadros de cada paso en % de la página:
      - en tablas, el recuadro se encaja entre las líneas que separan las filas
        (queda centrado sobre la fila completa);
      - en texto suelto, se centra sobre la altura visual de las letras.
  · escribe img/fichas/fichas.json (se copia al objeto FICHAS de index.html)
  · con --preview, dibuja los recuadros sobre las páginas en tools/preview/
    para revisarlos a ojo.

Uso:  python3 tools/fichas.py [--preview]
(--preview escribe en tools/preview/ o en la carpeta indicada en FICHAS_PREVIEW)
"""
import json
import os
import sys

import fitz  # PyMuPDF
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "img", "fichas")
PREV = os.environ.get("FICHAS_PREVIEW", os.path.join(RAIZ, "tools", "preview"))
ZOOM = 4.0  # px por pt: nítido con zoom ~4x en un proyector 1080p
PAD = 3.0  # margen horizontal de los recuadros, en pt


# ------------------------------------------------------------------ geometría
def separadores(page):
    """Segmentos horizontales (y, x0, x1) de líneas y bordes de rectángulos."""
    segs = []
    for dr in page.get_drawings():
        for it in dr["items"]:
            if it[0] == "l":
                a, b = it[1], it[2]
                if abs(a.y - b.y) < 0.8 and abs(a.x - b.x) > 15:
                    segs.append(((a.y + b.y) / 2, min(a.x, b.x), max(a.x, b.x)))
            elif it[0] == "re":
                r = it[1]
                if r.width > 15:
                    if r.height < 2:
                        segs.append(((r.y0 + r.y1) / 2, r.x0, r.x1))
                    else:
                        segs += [(r.y0, r.x0, r.x1), (r.y1, r.x0, r.x1)]
    return segs


def buscar(page, texto, n=0):
    hits = page.search_for(texto)
    if len(hits) <= n:
        raise SystemExit(f"No encontré {texto!r} (#{n}) en la página {page.number + 1}")
    return hits[n]


def linea(page, hit):
    """Span de texto cuyo centro está más cerca del centro del hit."""
    c = (hit.tl + hit.br) / 2
    best, dist = None, 1e9
    for b in page.get_text("dict", clip=hit + (-2, -2, 2, 2))["blocks"]:
        for ln in b.get("lines", []):
            for sp in ln["spans"]:
                if not sp["text"].strip():
                    continue
                r = fitz.Rect(sp["bbox"])
                d = abs((r.y0 + r.y1) / 2 - c.y)
                if r.intersects(hit) and d < dist:
                    best, dist = sp, d
    return best


def fila(page, hit, segs, x=None):
    """Encaja el texto entre el separador inmediatamente superior e inferior."""
    cx = (hit.x0 + hit.x1) / 2
    sp = linea(page, hit)
    cy = sp["origin"][1] - 0.34 * sp["size"] if sp else (hit.y0 + hit.y1) / 2
    m = 0.3 * (sp["size"] if sp else hit.height)
    arriba = [y for y, a, b in segs if a - 1 <= cx <= b + 1 and y <= cy - m]
    abajo = [y for y, a, b in segs if a - 1 <= cx <= b + 1 and y >= cy + m]
    if not arriba or not abajo:
        return None
    y0, y1 = max(arriba), min(abajo)
    if y1 - y0 > 4 * hit.height:  # demasiado lejos: no es una fila de tabla
        return None
    x0, x1 = x if x else (hit.x0 - PAD, hit.x1 + PAD)
    # recorta el recuadro a la derecha hasta donde termina el texto de la fila:
    # así el zoom puede ser mayor sin perder contenido
    der = [sp["bbox"][2] for b in page.get_text("dict", clip=fitz.Rect(x0, y0, x1, y1))["blocks"]
           for ln in b.get("lines", []) for sp in ln["spans"]
           if sp["text"].strip() and y0 <= (sp["bbox"][1] + sp["bbox"][3]) / 2 <= y1]
    if der:
        x1 = min(x1, max(der) + 3 * PAD)
    return fitz.Rect(x0, y0, x1, y1)


def visual(page, hit, x=None):
    """Recuadro centrado sobre la altura visual del texto (no sobre su caja tipográfica)."""
    best = linea(page, hit)
    if best is None:
        return hit + (-PAD, -PAD, PAD, PAD)
    base, s = best["origin"][1], best["size"]
    cy = base - 0.34 * s
    x0, x1 = x if x else (hit.x0 - PAD, hit.x1 + PAD)
    return fitz.Rect(x0, cy - 0.82 * s, x1, cy + 0.82 * s)


def caja(page, segs, sel):
    """sel: lista de selectores que se unen en un solo recuadro.
       ("t", texto, n, x)  → fila de tabla si la hay; si no, texto visual
       ("v", texto, n, x)  → texto visual (sin encajar en fila)
       ("r", x0, y0, x1, y1) → rectángulo explícito en pt"""
    out = None
    for s in sel:
        if s[0] == "r":
            r = fitz.Rect(*s[1:])
        else:
            _, texto, n, x = (list(s) + [0, None])[:4]
            hit = buscar(page, texto, n)
            r = (fila(page, hit, segs, x) if s[0] == "t" else None) or visual(page, hit, x)
        out = r if out is None else out | r
    return out


# ------------------------------------------------------------------ fichas
T, V, R = "t", "v", "r"
FICHAS = {
    # Cada paso: (página, [grupos de selectores]); cada grupo es un recuadro.
    "tc10c": ("ds_te6503_es_es.pdf", [
        (1, [[(R, 46, 70, 262, 128)], [(V, "Industria de alimentos y bebidas")]]),
        (3, [[(T, "Modelos K, J, E, N, T", 0, (50, 546))]]),
        (3, [[(T, "Tipo K", 0, (50, 546)), (T, "-40 ... +750", 1, (50, 546))]]),
        (3, [[(T, "Marcado de la polaridad", 0, (50, 546)), (R, 50, 200.5, 546, 306)]]),
        (2, [[(R, 336, 122, 462, 192)],
             [(V, "Conexión a proceso (seleccionable)", 0, (62, 200)), (V, "Vaina de tubo", 0, (62, 200))]]),
        (8, [[(T, "Señal de salida", 0, (50, 546)), (T, "4 ... 20 mA", 0, (50, 546))]]),
    ]),
    "tr10c": ("ds_te6003_es_es.pdf", [
        (1, [[(R, 46, 70, 262, 128)], [(R, 330, 196, 512, 410)]]),
        (3, [[(T, "Pt100, Pt1000", 0, (50, 546))]]),
        (3, [[(T, "0,1 ... 1,0 mA", 0, (50, 546))]]),
        (3, [[(R, 50, 108, 298, 352)]]),
        (3, [[(T, "Clase A 2)", 0, (50, 546)), (T, "Clase AA 2)", 0, (50, 546)), (R, 50, 418, 300, 476)],
             [(V, "No con conexionado de 2 hilos")]]),
        (8, [[(T, "Señal de salida", 0, (50, 546)), (T, "4 ... 20 mA", 0, (50, 546))]]),
    ]),
    "tw2000": ("TW2000-01_ES-ES.pdf", [
        (1, [[(T, "Rango de medición", 0, (44, 572))]]),
        (4, [[(R, 196, 120, 440, 312)], [(V, "OUT1:", 0, (42, 260)), (V, "OUT2:", 0, (42, 260))]]),
        (2, [[(T, "Salida analógica de corriente", 0, (44, 572))]]),
        (1, [[(T, "Señal de salida", 0, (44, 572)), (T, "Alimentación", 1, (44, 572))]]),
        (2, [[(T, "Opciones de parametrización", 0, (44, 572))]]),
        (4, [[(R, 196, 498, 556, 700)]]),
    ]),
    "ntcle100": ("ntcle100.pdf", [
        (1, [[(V, "These thermistors have a negative", 0, (318, 560)), (V, "plated copper wires", 0, (318, 560))]]),
        (1, [[(T, "Operating temperature range:", 0, (55, 292)), (R, 55, 371, 292, 418)]]),
    ]),
    "lm35": ("lm35.pdf", [
        (1, [[(V, "Linear + 10-mV/°C Scale Factor")]]),
        (1, [[(V, "Operates From 4 V to 30 V")]]),
        (3, [[(R, 380, 98, 492, 196)]]),
    ]),
}


def recortar(img_path):
    """Reduce a paleta de 64 colores: mismo aspecto, archivo mucho más liviano."""
    im = Image.open(img_path).convert("RGB")
    im.quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(img_path, optimize=True)


def main(preview=False):
    os.makedirs(OUT, exist_ok=True)
    if preview:
        os.makedirs(PREV, exist_ok=True)
    datos = {}
    for key, (pdf, pasos) in FICHAS.items():
        doc = fitz.open(os.path.join(RAIZ, pdf))
        p0 = doc[0].rect
        paginas = sorted({p for p, _ in pasos})
        out_pasos = []
        cajas_por_pag = {}
        for p, grupos in pasos:
            page = doc[p - 1]
            segs = separadores(page)
            W, H = page.rect.width, page.rect.height
            cajas = []
            for g in grupos:
                r = caja(page, segs, g)
                cajas.append([round(r.x0 / W * 100, 2), round(r.y0 / H * 100, 2),
                              round(r.width / W * 100, 2), round(r.height / H * 100, 2)])
                cajas_por_pag.setdefault(p, []).append(r)
            out_pasos.append({"p": p, "cajas": cajas})
        for p in paginas:
            pix = doc[p - 1].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), alpha=False)
            path = os.path.join(OUT, f"{key}-p{p:02d}.png")
            pix.save(path)
            recortar(path)
            if preview:
                pg = doc[p - 1]
                for r in cajas_por_pag.get(p, []):
                    pg.draw_rect(r, color=(1, 0, 0), width=1.2)
                pg.get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(os.path.join(PREV, f"{key}-p{p:02d}.png"))
        datos[key] = {"ratio": round(p0.width / p0.height, 4), "total": len(doc),
                      "paginas": paginas, "pasos": out_pasos}
        kb = sum(os.path.getsize(os.path.join(OUT, f"{key}-p{p:02d}.png")) for p in paginas) // 1024
        print(f"  {key}: {len(paginas)} págs. ({kb} KB), {len(out_pasos)} pasos")
    with open(os.path.join(OUT, "fichas.json"), "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=1)
    print(json.dumps(datos, ensure_ascii=False))


if __name__ == "__main__":
    main(preview="--preview" in sys.argv)
