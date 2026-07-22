# python3 -m unittest discover -s src
uv run --with coverage -m coverage run -m unittest discover "$@"
SAVE=$?
uv run --with coverage -m coverage report
uv run --with coverage -m coverage html
exit $SAVE
