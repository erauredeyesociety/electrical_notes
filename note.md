sudo snap install go --classic

sudo snap install hugo --channel=extended/stable --classic

hugo mod init github.com/erauredeyesociety/electrical_notes

go mod tidy

hugo mod get github.com/imfing/hextra

- make sure to mount layouts and static after importing module in hugo.yaml
- make sure to enable math in params



dev@DB-78GB094:~/electrical_notes$ tree -I "public" -I "resources" -I "_vendor"
.
├── README.md
├── content
│   ├── _index.md
│   ├── about.md
│   └── ee_300
│       ├── _index.md
│       ├── exam_1_roadmap_chat.md
│       └── exam_1_roadmap_notebookLM.md
├── go.mod
├── go.sum
├── hugo.yaml
├── layouts
│   └── partials
│       └── head-additions.html
└── note.md

4 directories, 11 files
dev@DB-78GB094:~/electrical_notes$



converting markdown files to PDFs, controlling margins and font size (cheat sheet printing)

⚠️ Limitation: Pandoc won’t execute your <script> Vega chart — you’ll need to replace it with a static PNG/SVG. You can export the chart from Vega (in your browser, right-click → save as PNG/SVG) and embed in the Markdown as:

![Ideal Diode Curve](diode_curve.png)

```bash
sudo apt update
sudo apt install -y pandoc texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-plain-generic texlive-xetex poppler-utils
```

```bash
pandoc exam_1_cheatsheet_pandoc.md -o exam1_cheatsheet.pdf --pdf-engine=xelatex -V geometry:margin=0.25in -V fontsize=9pt
```