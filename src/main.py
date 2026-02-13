#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

def run(script):
    print(f"\n=== Running {script} ===")
    subprocess.run(["python3", script], check=True)

def main():
    # 1. Analyse SG(k)
    run("sg_families_analysis.py")

    # 2. Heatmaps
    run("heatmaps.py")

    # 3. Comparaison entropie/DB
    run("compare_sg_families.py")

    # 4. Analyse des orbites
    run("cube30_orbits.py")
    
    # 5. détecter automatiquement une période 9
    run("period9_detector.py")

    # 6. Création image période 9
    run("period9_plot.py")

    # 7. Génération du PDF
    run("pdf_report.py")

    print("\n=== Pipeline complet terminé ===")

if __name__ == "__main__":
    main()
