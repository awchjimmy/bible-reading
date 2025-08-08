# bible-reading
bible reading app

### app name scriptures
- [x] 切換書、切換章節
- [x] 後台基本維護

### feature requests
- [ ] 螢光筆畫重點 highlight verses
- [ ] 筆記 take notes
- [ ] 詩歌本 song book
- [ ] 家譜 family tree
- [ ] 插畫 gallery
- [ ] 成就 achievements

---

## For developers

### How to set up

1. Setup uv
```sh
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# or Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Install latest python
```sh
uv python install
```

3. Install dependencies
```sh
uv sync
```

### How to run server

1. Run server
```sh
uv run ./manage.py runserver
```

2. Check browser
Your site is available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
