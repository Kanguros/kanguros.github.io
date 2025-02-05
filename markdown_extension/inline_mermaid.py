"""
Mermaid extensions for Markdown.
Renders the output inline, eliminating the need to configure an output
directory.

Supports output types of SVG and PNG. The output will be taken from the
filename specified in the tag. Example:

```mermaid
graph TD
A[Client] --> B[Load Balancer]
```

Requires the mermaid cli (https://github.com/mermaid-js/mermaid-cli)

Inspired by cesaremorel/markdown-inline-graphviz (http://github.com/cesaremorel/markdown-inline-graphviz)
"""

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from markdown import Extension
from markdown.preprocessors import Preprocessor

# Global vars
BLOCK_RE = re.compile(
    r"^```mermaid\s*\n(?P<content>.*?)```\s*$", re.MULTILINE | re.DOTALL
)

puppeteer_config_content = """{
  "args": ["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu"]
}
"""


def find_mmdc():
    exec_path = shutil.which("mmdc")
    if exec_path is not None:
        return Path(exec_path)
    raise ValueError(f"Unable to get path to Mermaid CLI 'mmdc' executable.")


class InlineMermaidExtension(Extension):
    def extendMarkdown(self, md):
        """Add InlineMermaidPreprocessor to the Markdown instance."""
        md.registerExtension(self)
        md.preprocessors.register(InlineMermaidPreprocessor(md), "mermaid_block", 27)


class InlineMermaidPreprocessor(Preprocessor):

    def run(self, lines):
        """Match and generate mermaid code blocks."""

        mmdc = find_mmdc()

        text = "\n".join(lines)
        while True:
            m = BLOCK_RE.search(text)
            if not m:
                break

            content = m.group("content")

            with tempfile.TemporaryDirectory() as tmp:
                tmp_dir = Path(tmp)
                tmp_svg_path = tmp_dir / "out.svg"

                puppeteer_config = tmp_dir / "puppeteer-config.json"
                with puppeteer_config.open("w+") as f:
                    f.write(puppeteer_config_content)

                args = [str(mmdc),
                        "--theme", "neutral",
                        "--backgroundColor", "transparent",
                        "-p", str(puppeteer_config),
                        "-o", str(tmp_svg_path)
                        ]

                try:
                    res = subprocess.run(
                        args,
                        input=content,
                        capture_output=True,
                        text=True,
                        check=True,
                    )
                except Exception as e:
                    return (
                        "<pre>Failed to invoke mmdc command</pre>"
                        f"<pre>Error : {str(e)} </pre>"
                        f"<pre>Type : {str(e.__class__)}</pre>"
                        f"<pre>Args : {str(args)}</pre>"
                        f"<pre>{content}</pre>"
                    ).split("\n")

                if not tmp_svg_path.is_file():
                    return (
                        "<pre>Error : Image not created</pre>"
                        f"<pre>Args :{str(args)}</pre>"
                        f"<pre>stdout : {res.stdout} </pre>"
                        f"<pre>stderr : {res.stderr}</pre>"
                        f"<pre>graph code : {content}</pre>"
                    ).split("\n")

                # with tmp_svg_path.open("rb") as fb:
                #     svg_bytes_content = fb.read()
                #     encoded_image_content = base64.b64encode(svg_bytes_content).decode("utf-8")
                #     img_tag = f'<img src="data:image/svg+xml;base64,{encoded_image_content}">'

                with tmp_svg_path.open("r") as f:
                    svg_content = f.read()
                if not svg_content:
                    return (
                        f"<pre>Error : Content of a {tmp_svg_path} is empty</pre>"
                        f"<pre>Args : {str(args)} </pre>"
                        f"<pre>{content}</pre>"
                    ).split("\n")

                text = "{}\n{}\n{}".format(
                    text[: m.start()],
                    # self.md.htmlStash.store(img_tag),
                    self.md.htmlStash.store(svg_content),
                    text[m.end():],
                )

        return text.split("\n")


def makeExtension(**kwargs):
    return InlineMermaidExtension(**kwargs)
