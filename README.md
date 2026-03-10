# Dirección de Recursos Humanos I — CaixaBank
### Doble Grado ADE-Ingenierías · Universidad de Granada

> **Esta es la Entrega 1 de 4** del proyecto grupal de la asignatura.
> Temas cubiertos: **Tema 2** (Análisis y Diseño de Puestos) y **Tema 3** (Planificación de RRHH).

---

## Índice

1. [Sobre el proyecto](#sobre-el-proyecto)
2. [Estructura del repositorio](#estructura-del-repositorio)
3. [Entregas del proyecto](#entregas-del-proyecto)
4. [Cómo empezar: clonar el repositorio](#cómo-empezar-clonar-el-repositorio)
5. [Compilar el LaTeX localmente](#compilar-el-latex-localmente)
6. [Usar Overleaf con Git (recomendado para compartir)](#usar-overleaf-con-git)
7. [Flujo de trabajo con Git: cómo colaborar sin pisarnos](#flujo-de-trabajo-con-git)
8. [Convención de commits](#convención-de-commits)
9. [Normas del equipo](#normas-del-equipo)

---

## Sobre el proyecto

El proyecto consiste en **analizar las prácticas de Recursos Humanos de CaixaBank**, una empresa real con más de 20 trabajadores. El análisis se realiza en grupos de 4-5 personas a lo largo de **4 entregas parciales** durante el curso.

Cada entrega incluye:
- **Trabajo escrito** (este documento LaTeX, exportado a PDF).
- **Presentación oral de 10 minutos** en clase. Todos los miembros del grupo deben intervenir.

Esta plantilla está basada en la clase `ugrTFG`, la plantilla institucional de la UGR para Trabajos de Fin de Grado, adaptada al formato de práctica grupal de asignatura.

---

## Estructura del repositorio

```
RecursosHumanosCaixaBank/
│
├── practica.tex                          # Archivo principal (compilar este)
├── ugrTFG.cls                       # Clase LaTeX institucional UGR
├── library.bib                      # Bibliografía (formato BibTeX)
├── glosario.tex                     # Glosario opcional
├── alpha-es.bst                     # Estilo bibliográfico (español)
├── plain-es.bst                     # Estilo bibliográfico alternativo
│
├── preliminares/
│   ├── declaracion-originalidad.tex # Declaración grupal de originalidad
│   ├── resumen.tex                  # Resumen ejecutivo del trabajo
│   └── tablacontenidos.tex          # Tabla de contenidos
│
├── capitulos/
│   ├── cap1_empresa.tex             # Capítulo 1: Empresa y organigrama
│   ├── cap2_tema2.tex               # Capítulo 2: Tema 2 (análisis de puestos)
│   └── cap3_tema3.tex               # Capítulo 3: Tema 3 (planificación RRHH)
│
├── apendices/
│   └── entrevista.tex               # Apéndice A: Preguntas y respuestas
│
├── img/                             # Imágenes de portada UGR + vuestras figuras
├── .gitignore                       # Ignora archivos auxiliares de LaTeX
└── README.md                        # Este archivo
```

**Regla de oro:** cada persona trabaja sobre **su/sus archivo(s) asignado(s)** para evitar conflictos de fusión en Git.

---

## Entregas del proyecto

| # | Temas | Estado |
|---|-------|--------|
| **Entrega 1** | Tema 2 (Análisis de Puestos) + Tema 3 (Planificación de RRHH) | En curso |
| Entrega 2 | Por determinar | Pendiente |
| Entrega 3 | Por determinar | Pendiente |
| Entrega 4 | Por determinar | Pendiente |

---

## Cómo empezar: clonar el repositorio

### Paso 1 — Instalar Git (si no lo tienes)

- **Windows:** descarga [Git for Windows](https://git-scm.com/download/win) e instálalo.
- **macOS:** abre Terminal y ejecuta `xcode-select --install`.
- **Linux (Ubuntu/Debian):** `sudo apt install git`

### Paso 2 — Configura tu identidad en Git (solo la primera vez)

```bash
git config --global user.name "Tu Nombre Apellido"
git config --global user.email "tu_email@correo.ugr.es"
```

### Paso 3 — Clona el repositorio

```bash
git clone https://github.com/[USUARIO]/RecursosHumanosCaixaBank.git
cd RecursosHumanosCaixaBank
```

> Reemplaza `[USUARIO]` con el nombre de usuario de GitHub del repositorio.

---

## Compilar el LaTeX localmente

Este proyecto usa la clase `ugrTFG` (incluida en el repositorio como `ugrTFG.cls`). No necesitáis instalar ningún paquete adicional más allá de una distribución LaTeX estándar.

### Requisitos de compilación

El documento se compila con **pdflatex** (no requiere XeLaTeX ni LuaLaTeX).

Las fuentes que usa la clase (`mathpazo`, `cabin`, `inconsolata`) están incluidas en las distribuciones LaTeX completas (TeX Live full, MiKTeX con gestor de paquetes activo).

### Opción A — Con `pdflatex` directamente (más sencillo)

```bash
# Desde la raíz del repositorio — SIEMPRE dos pasadas mínimo:
pdflatex practica.tex
pdflatex practica.tex
```

La segunda pasada es necesaria para que el índice de contenidos y las referencias internas se actualicen correctamente.

### Opción B — Con `latexmk` (recomendada, automática)

`latexmk` detecta automáticamente cuántas pasadas necesita:

```bash
latexmk -pdf practica.tex

# Para limpiar los archivos auxiliares:
latexmk -c
```

### Opción C — Con bibliografía BibTeX (si añadís citas a `library.bib`)

Si citáis referencias con `\cite{}`, necesitáis ejecutar BibTeX entre las pasadas de pdflatex:

```bash
pdflatex practica.tex
bibtex practica
pdflatex practica.tex
pdflatex practica.tex
```

O con `latexmk`, que lo hace automáticamente:

```bash
latexmk -pdf practica.tex
```

### Opción D — Con un editor gráfico (más fácil para Windows/macOS)

- **[TeXstudio](https://www.texstudio.org/)** (gratuito, multiplataforma): abre `practica.tex` y pulsa F5. Configura el compilador como pdflatex.
- **[VS Code](https://code.visualstudio.com/)** + extensión **LaTeX Workshop**: compilación automática al guardar. Compila con pdflatex por defecto.
- **[Overleaf](https://www.overleaf.com/)** online: ver sección siguiente. Overleaf usa pdflatex por defecto — compatible al 100%.

### Distribución LaTeX recomendada por sistema operativo

| Sistema | Distribución | Instalación |
|---------|-------------|-------------|
| Windows | [MiKTeX](https://miktex.org/) | Descarga e instala. Activa la instalación automática de paquetes. |
| Windows | [TeX Live](https://tug.org/texlive/) | Más completo, instala `texlive-full` |
| macOS   | [MacTeX](https://www.tug.org/mactex/) | Paquete `.pkg` de instalación directa |
| Linux   | TeX Live | `sudo apt install texlive-full texlive-lang-spanish` |

> **Nota sobre fuentes:** si al compilar obtenéis un error sobre la fuente `cabin`, podéis cambiar la opción en `ugrTFG.cls` (el fallback ya está incluido: usa `iwona` automáticamente si `cabin` no está disponible).

---

## Usar Overleaf con Git

[Overleaf](https://www.overleaf.com) es un editor LaTeX online que permite compilar sin instalar nada. La versión gratuita permite conectarlo con GitHub.

### Cómo vincular Overleaf con este repositorio de GitHub

1. Crea una cuenta en [overleaf.com](https://www.overleaf.com) (puedes usar tu email de la UGR).
2. En Overleaf, haz clic en **New Project** → **Import from GitHub**.
3. Autoriza a Overleaf para acceder a tu GitHub.
4. Selecciona el repositorio `RecursosHumanosCaixaBank`.
5. El archivo principal a compilar es **`practica.tex`** (no `main.tex`). Configúralo en Overleaf: Menú → Compilador → Main document → `practica.tex`.
6. Usa el botón **Sync → Push to GitHub** para subir cambios desde Overleaf, y **Pull from GitHub** para traer cambios de otros.

> **Importante:** sincroniza **antes de empezar a editar** (Pull) y **al terminar** (Push), para no sobreescribir el trabajo de los demás.

---

## Flujo de trabajo con Git: cómo colaborar sin pisarnos

El flujo recomendado es **uno por uno en la rama principal** (sin ramas separadas, para no complicarlo):

### Flujo de trabajo básico (antes de cada sesión de trabajo)

```bash
# 1. SIEMPRE empieza actualizando tu copia local:
git pull

# 2. Edita los archivos que te corresponden (¡solo los tuyos!).

# 3. Comprueba qué archivos has modificado:
git status

# 4. Añade los cambios al "staging area":
git add capitulos/cap2_tema2.tex
# (o añade una carpeta entera: git add capitulos/)

# 5. Crea un commit con un mensaje descriptivo:
git commit -m "feat: completo análisis de puestos con datos de la entrevista"

# 6. Sube tus cambios al repositorio remoto:
git push
```

### ¿Qué pasa si hay un conflicto?

Un conflicto ocurre cuando dos personas han editado el mismo fragmento del mismo archivo. Git te avisará al hacer `git pull` o `git push`. Para resolverlo:

```
<<<<<<< HEAD
[Tu versión del texto]
=======
[Versión del compañero]
>>>>>>> origin/main
```

1. Abre el archivo en tu editor.
2. Decide qué versión conservar (o combina ambas manualmente).
3. Elimina las marcas `<<<<<<<`, `=======` y `>>>>>>>`.
4. Guarda, luego `git add <archivo>` y `git commit`.

**Para evitar conflictos:** respeta la asignación de archivos de cada persona.

### Asignación de archivos por persona

| Persona | Archivos asignados |
|---------|--------------------|
| Persona 1 | `capitulos/cap1_empresa.tex`, `preliminares/resumen.tex` |
| Persona 2 | `capitulos/cap2_tema2.tex` (secciones 1 y 2) |
| Persona 3 | `capitulos/cap2_tema2.tex` (secciones 3 y 4) |
| Persona 4 | `capitulos/cap3_tema3.tex` (secciones 1, 2 y 3) |
| Persona 5 | `capitulos/cap3_tema3.tex` (secciones 4, 5 y 6) + `apendices/entrevista.tex` |

> Ajustadlo según vuestro reparto. Si sois 4 personas, repartid las secciones del Capítulo 3 entre las demás.
>
> Si dos personas trabajan en el mismo archivo (`cap2_tema2.tex` o `cap3_tema3.tex`), coordinaos para no editar las mismas secciones al mismo tiempo.

---

## Convención de commits

Usad mensajes de commit descriptivos con prefijos:

```
feat: añado descripción del puesto de Director de Oficina
fix: corrijo error de compilación en cap2_tema2
content: completo respuestas del apéndice con datos de entrevista
style: mejoro formato de tablas en capítulo 3
draft: esqueleto de la sección planificación RRHH
```

Prefijos:
- `feat:` contenido nuevo
- `fix:` corrección de errores (incluidos errores de LaTeX)
- `content:` completar o mejorar contenido existente
- `style:` cambios de formato sin modificar el contenido
- `draft:` borrador inicial de una sección

---

## Normas del equipo

1. **No edites archivos que no sean los tuyos** sin avisar al grupo (evita conflictos de Git).
2. **Haz `git pull` siempre antes de empezar a escribir** en tu sesión.
3. **Haz commits frecuentes y pequeños**, no uno gigante al final.
4. **No subas archivos auxiliares de LaTeX** (`.aux`, `.log`, `.synctex.gz`...). El `.gitignore` ya los excluye, pero comprobadlo con `git status` antes de `git add`.
5. **Comunicación activa:** avisad al grupo cuando terminéis una sección o si encontráis algún problema.
6. **Respeta los comentarios `% TODO:`** en el LaTeX: son recordatorios de qué falta completar.
7. **Antes de entregar**, si no queréis que las cajas amarillas de recordatorio aparezcan en el PDF final, comentad su contenido o eliminad el `\usepackage[most]{tcolorbox}` y el `\newtcolorbox{notaequipo}` en `practica.tex`.
8. **El archivo principal es `practica.tex`** (no `main.tex`). Aseguraos de configurar vuestro editor o Overleaf para compilar ese archivo.

---

*Plantilla basada en [latex-mat-ugr/Plantilla-TFG](https://github.com/latex-mat-ugr/Plantilla-TFG) — Adaptada para prácticas grupales de RRHH I*

*Repositorio configurado para el grupo de trabajo — Curso 2024/2025*
