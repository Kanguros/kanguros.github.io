Title: Markdown in Pelican 
Date: 10.03.2022   
Author: Kamil Urbanek   
Category: General
Summary: How to write articles   

## Possibilities of Markdown implementation in Pelican



--- 

## Filename
In folder `content/articles/` create new file according to [template](#template) with *.md extension.

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


# Markdown syntax

---

Usage examples of a Markdown features. 

### Admonitions

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

### Progress Bars

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




