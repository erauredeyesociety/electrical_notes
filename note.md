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