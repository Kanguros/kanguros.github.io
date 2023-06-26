# [kanguros.github.io](https://kanguros.github.io)

My personal blog with all of its content. Build and deployed using `pelican` library. With modified theme `svbtle`.

## Prerequisits

- Python
- poetry

## Installation

In order to have virtual environment ready to write posts and see them how they actually look on the website, run the
code-snippet below:

```commandline
git clone https://github.com/Kanguros/kanguros.github.io.git
cd kanguros.github.io
poetry install 
```

## Usage

Once installed, you may use the commands below:

- `invoke build` - Build site, append mode.
- `invoke rebuild` - Remove existing files then build.
- `invoke serve` - Serve site on localhost.
- `invoke reserve` - Clean build and then serve (`rebuild` and `serve`).

Website generated locally is saved to `./local_output` folder

## Theme

Currently used theme is [Semantic UI](). Many modifications
have been made. In templates and css files.

## Workflow

Generating website, deployment to desire branch and sending to host server is done through GitHub Actions.

### 1. Build Action

Definition of the workflow which build whole site and push it to the `deploy` branch is in
file `.github/workflows/build.yml`

### 2. Deploy Action

Once generated content has been pushed to `deploy` branch, GitHub Pages default action is executed. It loads the file to
a GitHub Pages _server_ under address provided in a Repository settings.

## Articles

Each article has to be placed in `content/posts/` directory as an `*.md` file type.  
Push changes with a Pull Request to the `main` branch.
Once approved, it will execute `build.yml` Action.

### Structure

Each _Article_ has to match template below:

> **Title**: Required; Main header of the article.  
> **Date**: Required; Data of posting.  
> **Author**: Required; One of the `Name Surname` defined authors.  
> **Summary**: Required. Short description of the article.    
> **Category**: Optional; By default, it gets an `General` Category.  
> **Tags**: Optional.   
> **Cover**: Optional; If not provided, default header image one will be used.
>
> [MAIN CONTENT]
> Article's content written in Markdown.

### PyCharm File Template

To help ourself, [`PyCharm's File Template`](
https://www.jetbrains.com/help/pycharm/using-file-and-code-templates.html) definition below.

_Settings -> Editor -> File and Code Templates_

Template to Copy/Paste

```
Title: ${FILE_NAME}  
Date: ${DATE}  
Author: Name Surname
Tags: 

[MAIN CONTENT]
```

## Links

- https://docs.getpelican.com/en/latest/ - Pelican documentation
- https://github.com/peaceiris/actions-gh-pages - GitHub Action for deploying static website



