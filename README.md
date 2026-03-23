# Dirección de Recursos Humanos I — CaixaBank
### Doble Grado ADE-Ingenierías · Universidad de Granada

> Guía de trabajo actualizada para un repositorio con **múltiples prácticas independientes**
> compartiendo la misma plantilla, bibliografía y recursos globales.

---

## Índice

1. [Qué cambió en la organización](#qué-cambió-en-la-organización)
2. [Estructura del repositorio](#estructura-del-repositorio)
3. [Flujo recomendado por práctica](#flujo-recomendado-por-práctica)
4. [Compilación rápida](#compilación-rápida)
5. [Colaboración con Git (sin conflictos)](#colaboración-con-git-sin-conflictos)
6. [Uso con Overleaf](#uso-con-overleaf)
7. [Reglas del equipo](#reglas-del-equipo)

---

## Qué cambió en la organización

Antes había un único maestro (`practica.tex`).
Ahora el proyecto se organiza por entregas/prácticas:

- `practicat2t3.tex`: documento maestro para los temas 2 y 3.
- `practicat4t5.tex`: documento maestro para los temas 4 y 5.
- `capitulos/practicat2t3/`: capítulos de contenido de temas 2 y 3.
- `capitulos/practicat4t5/`: carpeta preparada para temas 4 y 5.

La idea es **aislar contenido por práctica** y reutilizar configuración global sin duplicar clases ni recursos.

---

## Estructura del repositorio

```text
RecursosHumanosCaixaBank/
│
├── practicat2t3.tex                  # Maestro de temas 2 y 3 (compila)
├── practicat4t5.tex                  # Maestro de temas 4 y 5 (limpio)
├── ugrTFG.cls                        # Plantilla institucional UGR
├── library.bib                       # Bibliografía global compartida
├── glosario.tex                      # Glosario global opcional
├── alpha-es.bst
├── plain-es.bst
│
├── preliminares/
│   ├── declaracion-originalidad.tex
│   ├── resumen.tex
│   └── tablacontenidos.tex
│
├── capitulos/
│   ├── bibliografia/
│   │   ├── bibliografiat2t3.tex      # Referencias de temas 2 y 3
│   │   └── bibliografiat4t5.tex      # Referencias de temas 4 y 5
│   ├── practicat2t3/
│   │   ├── cap1_empresa.tex
│   │   ├── cap2_tema2.tex
│   │   └── cap3_tema3.tex
│   └── practicat4t5/                 # Aquí irá el contenido nuevo
│
├── apendices/
│   └── entrevista.tex
│
├── img/
├── imagenes/
└── README.md
```

---

## Flujo recomendado por práctica

### `practicat2t3` (mantenimiento / correcciones)

1. Edita solo archivos en `capitulos/practicat2t3/` (y, si hace falta, `apendices/` o `preliminares/`).
2. Compila `practicat2t3.tex`.
3. Revisa PDF y corrige.

### `practicat4t5` (nuevo trabajo)

1. Crea capítulos nuevos dentro de `capitulos/practicat4t5/`.
2. Añade en `practicat4t5.tex` los `\input{...}` de `capitulos/practicat4t5/...`.
3. Compila `practicat4t5.tex`.

### Patrón recomendado para nuevos `\input` en `practicat4t5`

```tex
\mainmatter
\input{capitulos/practicat4t5/cap1_...}
\input{capitulos/practicat4t5/cap2_...}
\input{capitulos/practicat4t5/cap3_...}
```

---

## Compilación rápida

### Con `pdflatex`

```bash
# Temas 2 y 3
pdflatex practicat2t3.tex
pdflatex practicat2t3.tex

# Temas 4 y 5
pdflatex practicat4t5.tex
pdflatex practicat4t5.tex
```

### Con `latexmk` (recomendado)

```bash
latexmk -pdf practicat2t3.tex
latexmk -pdf practicat4t5.tex

# Limpiar auxiliares
latexmk -c
```

### Si usáis BibTeX

```bash
pdflatex practicat2t3.tex
bibtex practicat2t3
pdflatex practicat2t3.tex
pdflatex practicat2t3.tex
```

Análogo para `practicat4t5` cuando tenga citas.

---

## Colaboración con Git (sin conflictos)

### Rutina mínima antes de trabajar

```bash
git pull
git status
```

### Ejemplo de ciclo completo

```bash
# Editas solo lo que te corresponde
git add capitulos/practicat4t5/
git commit -m "content: añado primer borrador de capítulos de practicat4t5"
git push
```

### Regla de coordinación

- Si estás en temas 2 y 3, toca `capitulos/practicat2t3/`.
- Si estás en temas 4 y 5, toca `capitulos/practicat4t5/`.
- Evita editar el mismo archivo que otra persona a la vez.

---

## Uso con Overleaf

En Overleaf, elige el documento principal según la práctica activa:

- Para temas 2 y 3: `practicat2t3.tex`
- Para temas 4 y 5: `practicat4t5.tex`

Ruta: **Menu → Main document**.

Antes de editar: **Pull**. Al terminar: **Push**.

---

## Reglas del equipo

1. Trabaja siempre dentro de la carpeta correspondiente (`practicat2t3` o `practicat4t5`).
2. Haz `git pull` al empezar y commits pequeños al terminar bloques de trabajo.
3. No subas archivos auxiliares (`.aux`, `.log`, `.toc`, `.out`, `.synctex.gz`, etc.).
4. Mantén `ugrTFG.cls`, `library.bib`, estilos `.bst` e imágenes como recursos globales compartidos.
5. Si cambias la estructura de `\input` en un maestro, compílalo en ese mismo commit.

---

*Plantilla basada en [latex-mat-ugr/Plantilla-TFG](https://github.com/latex-mat-ugr/Plantilla-TFG), adaptada para prácticas grupales de RRHH I.*
