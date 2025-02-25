Act as a web designer, an expert of web technologies with Python expirience. Your task is to provide CSS rules to adjust articles to be printed nicely and readable.

Currently, page when printed contains page break in many places I would like to avoid and many other things I would like to adjust.

-   Avoid page break inside a table
-   Page break could be before H2
-   Currently, there are a lot of white space on left and right margins, remove them somehow.
-   Font size is too big.
-   Remove footer and nav.

Figure out what else should be adjusted

jinja template:
https://github.com/Kanguros/kanguros.github.io/blob/master/theme/templates/article.html

CSS stylesheet:
https://github.com/Kanguros/kanguros.github.io/blob/master/theme/static/css/clean-blog.css

Bootstrap is also used.

Some guide I found which could be useful https://www.sitepoint.com/css-printer-friendly-pages/
