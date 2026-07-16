# python3 -m unittest discover -s src
uv run --with coverage -m coverage run -m unittest discover -s src "$@"
uv run --with coverage -m coverage report
uv run --with coverage -m coverage html
