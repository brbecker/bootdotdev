# python3 src/main.py
# uv run src/main.py
uv run python -m src.main
cd public && uv run python -m http.server 8888
