# TP Sensores · Familia 6: Temperatura

Apoyo visual de la exposición del Seminario de Sensores — ING2222 Tecnología de Control, FI-UNMdP.

**Ver la presentación:** https://ezecarbajo3.github.io/tp-sensores-2da-prueba/

## Uso durante la exposición

| Tecla | Acción |
|---|---|
| `1` – `7` | Ir a cada bloque |
| `0` | Volver al inicio |
| `Av Pág` / `Espacio` | Pantalla siguiente (sirve con presentador) |
| `Re Pág` | Pantalla anterior |
| `←` `→` | Pasos de la hoja técnica en pantalla |
| `F` | Pantalla completa |
| `?` | Ayuda |

## Correr en local

```bash
python3 -m http.server 8137
```

y abrir http://localhost:8137 (también abre con doble clic en `index.html`).

## Estructura

- `index.html` — la página completa (HTML, CSS y JS). Nombres de expositores en `EXPOSITORES` y textos de las hojas técnicas en `FICHAS`.
- `img/fichas/` — páginas de las hojas técnicas usadas en la lectura guiada.
- `tools/fichas.py` — regenera esas páginas y los recuadros desde los PDF (`python3 tools/fichas.py`).
- `*.pdf` — copias locales de las hojas técnicas oficiales (WIKA, Vishay, Texas Instruments, ifm).
