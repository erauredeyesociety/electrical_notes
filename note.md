sudo snap install go --classic

sudo snap install hugo --channel=extended/stable --classic

hugo mod init github.com/erauredeyesociety/electrical_notes

go mod tidy

hugo mod get github.com/imfing/hextra
