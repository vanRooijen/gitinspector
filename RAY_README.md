python -m build

python -m pip install --upgrade dist/gitinspector-0.4.4-py3-none-any.whl

gitinspector --grading --format htmlembedded > git-stats/stats.html
