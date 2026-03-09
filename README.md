# Dirección de Recursos Humanos I — CaixaBank
### Doble Grado ADE-Ingenierías · Universidad de Granada

> **Esta es la Entrega 1 de 4** del proyecto grupal de la asignatura.
> Temas cubiertos en esta entrega: **Tema 2** (Análisis y Diseño de Puestos) y **Tema 3** (Planificación de RRHH).

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

---

## Estructura del repositorio

```
RecursosHumanosCaixaBank/
│
├── main.tex                        # Archivo principal (compilar este)
│
├── secciones/                      # Un archivo .tex por sección
│   ├── 00_portada.tex
│   ├── 01_introduccion.tex         # Empresa y organigrama
│   ├── 02_tema2_analisis_puestos.tex
│   ├── 03_tema2_descripcion_puestos.tex
│   ├── 04_tema2_rediseno_puestos.tex
│   ├── 05_tema2_nuevas_tendencias.tex
│   ├── 06_tema3_planificacion.tex
│   ├── 07_tema3_oferta_demanda.tex
│   ├── 08_tema3_equilibrio.tex
│   ├── 09_tema3_criterios_evaluacion.tex
│   ├── 10_tema3_procesos_sustractivos.tex
│   ├── 11_tema3_alternativas.tex
│   └── 12_anexo.tex                # Preguntas y respuestas de la entrevista
│
├── imagenes/                       # Organigrama, logos, gráficos
├── compilado/                      # PDF final (se puede ignorar en Git si es grande)
├── .gitignore                      # Ignora archivos auxiliares de LaTeX
└── README.md                       # Este archivo
```

**Regla de oro:** cada persona trabaja sobre **su/sus archivo(s) asignado(s)** para evitar conflictos de fusión.

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
- **macOS:** abre Terminal y ejecuta `xcode-select --install` (ya viene incluido).
- **Linux (Ubuntu/Debian):** `sudo apt install git`

### Paso 2 — Configura tu identidad en Git (solo la primera vez)

Abre una terminal y escribe:

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

### Opción A — Con `latexmk` (recomendada, más automática)

`latexmk` detecta automáticamente cuántas pasadas necesita (para índices, referencias, etc.).

```bash
# Desde la raíz del repositorio:
latexmk -pdf main.tex

# Para limpiar los archivos auxiliares:
latexmk -c
```

El PDF resultante será `main.pdf` en la raíz del proyecto.

**Instalar latexmk:**
- Windows (con MiKTeX): `miktex-console` → Packages → buscar `latexmk`
- macOS/Linux: viene incluido con TeX Live (`sudo apt install texlive-full`)

### Opción B — Con `pdflatex` directamente

```bash
pdflatex main.tex
pdflatex main.tex   # Segunda pasada para el índice de contenidos
```

### Opción C — Con un editor gráfico (más fácil para Windows/macOS)

- **[TeXstudio](https://www.texstudio.org/)** (gratuito, multiplataforma): abre `main.tex` y pulsa F5.
- **[VS Code](https://code.visualstudio.com/)** + extensión **LaTeX Workshop**: compilación automática al guardar.
- **[Overleaf](https://www.overleaf.com/)** online: ver sección siguiente.

### Distribución LaTeX recomendada por sistema operativo

| Sistema | Distribución |
|---------|-------------|
| Windows | [MiKTeX](https://miktex.org/) o [TeX Live](https://tug.org/texlive/) |
| macOS   | [MacTeX](https://www.tug.org/mactex/) |
| Linux   | `sudo apt install texlive-full texlive-lang-spanish` |

---

## Usar Overleaf con Git

[Overleaf](https://www.overleaf.com) es un editor LaTeX online que permite compilar sin instalar nada. La versión gratuita permite conectarlo con Git.

### Cómo vincular Overleaf con este repositorio de GitHub

1. Crea una cuenta en [overleaf.com](https://www.overleaf.com) (puedes usar tu email de la UGR).
2. En Overleaf, haz clic en **New Project** → **Import from GitHub**.
3. Autoriza a Overleaf para acceder a tu GitHub.
4. Selecciona el repositorio `RecursosHumanosCaixaBank`.
5. Overleaf sincronizará el repositorio. Usa el botón **Sync → Push to GitHub** para subir cambios desde Overleaf al repositorio, y **Pull from GitHub** para traer cambios de otros.

> **Importante:** si usas Overleaf, sincroniza **antes de empezar a editar** (Pull) y **al terminar** (Push), para no sobreescribir el trabajo de los demás.

---

## Flujo de trabajo con Git: cómo colaborar sin pisarnos

El flujo recomendado para el equipo es **uno por uno en la rama principal** (sin ramas separadas, para no complicarlo):

### Flujo de trabajo básico (antes de cada sesión de trabajo)

```bash
# 1. SIEMPRE empieza actualizando tu copia local con los últimos cambios del equipo:
git pull

# 2. Edita los archivos que te corresponden (¡solo los tuyos!).

# 3. Comprueba qué archivos has modificado:
git status

# 4. Añade los cambios al "staging area":
git add secciones/XX_nombre_del_archivo.tex
# (o añade varios de golpe: git add secciones/)

# 5. Crea un commit con un mensaje descriptivo:
git commit -m "feat: completo análisis de puestos con datos de la entrevista"

# 6. Sube tus cambios al repositorio remoto:
git push
```

### ¿Qué pasa si hay un conflicto?

Un conflicto ocurre cuando dos personas han editado el mismo fragmento del mismo archivo. Git te avisará al hacer `git pull` o `git push`. Para resolverlo:

```bash
# Git marcará el conflicto en el archivo con estas marcas:
# <<<<<<< HEAD
# [Tu versión]
# =======
# [Versión del compañero]
# >>>>>>> origin/main
```

1. Abre el archivo en tu editor.
2. Decide qué versión conservar (o combina ambas manualmente).
3. Elimina las marcas `<<<<<<<`, `=======` y `>>>>>>>`.
4. Guarda el archivo.
5. Haz `git add <archivo>` y luego `git commit`.

**Para evitar conflictos:** respeta la asignación de secciones que aparece abajo.

### Asignación de secciones por persona

| Persona | Archivos asignados |
|---------|--------------------|
| Persona 1 | `00_portada.tex`, `01_introduccion.tex` |
| Persona 2 | `02_tema2_analisis_puestos.tex`, `03_tema2_descripcion_puestos.tex` |
| Persona 3 | `04_tema2_rediseno_puestos.tex`, `05_tema2_nuevas_tendencias.tex` |
| Persona 4 | `06_tema3_planificacion.tex`, `07_tema3_oferta_demanda.tex`, `08_tema3_equilibrio.tex` |
| Persona 5 | `09_tema3_criterios_evaluacion.tex`, `10_tema3_procesos_sustractivos.tex`, `11_tema3_alternativas.tex`, `12_anexo.tex` |

> Ajustadlo según vuestro propio reparto. Si sois 4 personas, repartid el trabajo de la Persona 5 entre las demás.

---

## Convención de commits

Usad mensajes de commit descriptivos. Ejemplos:

```
feat: añado descripción del puesto de Director de Oficina
fix: corrijo error de compilación en tema2_analisis
content: completo respuestas del anexo con datos entrevista
style: mejoro formato de tablas en sección 3
draft: esqueleto de la sección planificacion RRHH
```

Prefijos útiles:
- `feat:` contenido nuevo
- `fix:` corrección de errores
- `content:` completar o mejorar contenido existente
- `style:` cambios de formato sin modificar contenido
- `draft:` borrador inicial de una sección

---

## Normas del equipo

1. **No edites archivos que no sean los tuyos** sin avisar al grupo (evita conflictos).
2. **Haz `git pull` siempre antes de empezar a escribir** en tu sesión de trabajo.
3. **Haz commits frecuentes y pequeños**, no uno gigante al final.
4. **No subas archivos auxiliares de LaTeX** (`.aux`, `.log`, `.synctex.gz`...). El `.gitignore` ya los excluye, pero comprobadlo con `git status` antes de hacer `git add`.
5. **Comunicación activa:** avisad al grupo por el canal de mensajería cuando terminéis una sección o si encontráis algún problema.
6. **Respeta los comentarios `% TODO:`** en el LaTeX: son recordatorios de qué falta completar en cada sección.
7. **Antes de entregar**, eliminad o comentad las cajas amarillas `\begin{notaequipo}...\end{notaequipo}` del `main.tex` si no queréis que aparezcan en la entrega final (o dejadlas si el/la profesor/a no lo prohíbe).

---

*Repositorio creado y configurado para el grupo de trabajo — Curso 2025/2026*
