# Pre-commits for blog

## HTML

```yaml
-   repo: https://github.com/Lucas-C/pre-commit-hooks-lxml
    sha: v1.1.0
    hooks:
    -   id: forbid-non-std-html-attributes
    -   id: detect-missing-css-classes
        args:
        - --css-files-dir
        - .
        - --html-files-dir
        - .
```

## Markdown

[pymarkdown](https://github.com/jackdewinter/pymarkdown)

```yaml
repos:
    - repo: https://github.com/jackdewinter/pymarkdown
      rev: main
      hooks:
          - id: pymarkdown
```