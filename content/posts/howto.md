Title: Markdown in Pelican
Date: 15/06/2023
Author: Kamil Urbanek   
Category: Webdev
Summary: Examples of Markdown formatting available in Pelican.

# Headers and texts

## Second level

### Third level

#### Forth level

**Bold text**
_Italic text_
Underline text

## Quote

> This is single line quote

Another quote

> This is multiline quote.
> It spans on few lines

## Code block

Inline `code text`.

Block code

```python
@task
def clean(c):
    """Remove generated files"""
    path = CONFIG['deploy_path']
    if os.path.isdir(path):
        print(f"Removing directory: {path}")
        shutil.rmtree(path)
        print(f"Creating a empty folder: {path}")
        os.makedirs(path)
    print(f"No directory as: {path}")
```

## Admonitions

Syntax:

```markdown
!!! danger
This is admonition type: `danger` without title.

!!! tip "Custom tip title"
This is admonition type: `tip` with custom title.
```

Available types: `danger`, `error`, `warning`, `caution`, `attention`, `important`, `note`, `hint`, `tip`

!!! danger
This is admonition type: `danger` without title.

!!! tip "Custom tip title"
This is admonition type: `tip` with custom title.

# Progress Bars

```markdown
[=0% "0%"]
[=50% "50%"]
[=100% "100%"]
[=0%]{: .thin}
[=50%]{: .thin}
[=100%]{: .thin}
```

[=0% "0%"]
[=50% "50%"]
[=100% "100%"]
[=0%]{: .thin}
[=50%]{: .thin}
[=100%]{: .thin}

# Article

How to create new article.

## Filename

In folder `content/posts/` create new file according to [template](#template) with *.md extension.

## Template

> **Title**: Required. Main header of the article.  
> **Date**: Required. Data of a posting.  
> **Author**: Required. One of the `Name Surname` defined authors.  
> **Category**: Optional. By default, it gets an `General` Category.  
> **Cover**: Optional. Path to header image. If not provided, default one will be used.  
> **Summary**: Optional. Short description of the article.    
> **Save_as**: Optional. File name of article.  
> **Slug**: Optional, article ID/REF (?). Used in URL creation. If not provided, it takes normalized title.    
> **Template**: Optional, filepath to `Jinja2` template used for generating html representation.  
> **Tags**: Optional
>
> [MAIN CONTENT]
> Article's content written in Markdown.


