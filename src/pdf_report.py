#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

PAGE_WIDTH, PAGE_HEIGHT = letter

def add_title(c, text):
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, PAGE_HEIGHT - 50, text)

def add_image_fullpage(c, path):
    if not os.path.exists(path):
        return False

    try:
        img = ImageReader(path)
        iw, ih = img.getSize()

        # Redimensionnement automatique pour tenir dans la page
        max_w = PAGE_WIDTH - 100
        max_h = PAGE_HEIGHT - 150

        scale = min(max_w / iw, max_h / ih)

        w = iw * scale
        h = ih * scale

        x = (PAGE_WIDTH - w) / 2
        y = (PAGE_HEIGHT - h) / 2 - 30

        c.drawImage(path, x, y, width=w, height=h, preserveAspectRatio=True)
        return True

    except Exception:
        return False

def add_page_with_image(c, title, path):
    c.showPage()
    add_title(c, title)
    ok = add_image_fullpage(c, path)
    if not ok:
        c.setFont("Helvetica", 12)
        c.drawString(50, PAGE_HEIGHT - 100, f"[Image manquante : {path}]")

def main():
    c = canvas.Canvas("Phase_Structure_SGk.pdf", pagesize=letter)

    # Page de garde
    add_title(c, "Phase Structure of SG(k)")
    c.setFont("Helvetica", 12)
    c.drawString(50, PAGE_HEIGHT - 80, "Generated automatically from SG pipeline")
    c.showPage()

    # 1. Scatter entropie/DB
    add_page_with_image(
        c,
        "Entropie vs Detailed Balance (Gap 6)",
        "figures/compare_SG_gap6_entropy_DB.png"
    )

    # 2. Heatmaps globales
    for d in [2, 4, 6]:
        add_page_with_image(
            c,
            f"Global gap {d}",
            f"figures/global_gap{d}.png"
        )

    # 3. Heatmaps SG(k)
    for k in range(2, 62, 2):
        for d in [2, 4, 6]:
            path = f"figures/SG{k}_gap{d}.png"
            if os.path.exists(path):
                add_page_with_image(
                    c,
                    f"SG({k}) gap {d}",
                    path
                )
    add_page_with_image(c, "Score période 9 vs k", "figures/period9_vs_k.png")

    c.save()
    print("PDF généré : Phase_Structure_SGk.pdf")

if __name__ == "__main__":
    main()
