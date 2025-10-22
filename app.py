from flask import Flask, render_template
import requests
from markdown_it import MarkdownIt
import re

app = Flask(__name__)

@app.route("/blog")
def blog():
    return render_template("blog-page/blog.html")

@app.route("/")
def index():
    url = "https://raw.githubusercontent.com/pretty-terminal/pretty/main/README.md"
    
    response = requests.get(url)
    if response.status_code == 200:
        md_content = response.text
        
        md_gfm = MarkdownIt().enable('table') 
        html_content = md_gfm.render(md_content)  

        html_content = convert_markdown_table_to_html(html_content)

        html_content = remove_paragraph_tags(html_content)
    else:
        html_content = "<p>ვერ მოიტანეს Markdown ფაილი.</p>"
    
    return render_template("index.html", html_content=html_content)


def convert_markdown_table_to_html(md_content):
    """Markdown ცხრილებს HTML ცხრილებში გარდაქმნის"""
    table_pattern = r'(\|.*\|[\n]+)'  
    tables = re.findall(table_pattern, md_content)

    for table in tables:
        rows = table.strip().split("\n")
        
        header_row = rows[0].strip().split("|")[1:-1]  
        header_html = "<tr><th>" + "</th><th>".join([col.strip() for col in header_row]) + "</th></tr>"

        body_rows = rows[2:]  
        body_html = ""
        for row in body_rows:
            cols = row.strip().split("|")[1:-1] 
            body_html += "<tr><td>" + "</td><td>".join([col.strip() for col in cols]) + "</td></tr>"

        table_html = f"<table>{header_html}{body_html}</table>"
        
        md_content = md_content.replace(table, table_html)

    return md_content


def remove_paragraph_tags(html_content):
    """<p> ტეგების ამოღება, გარდა ცხრილების"""
    parts = re.split(r'(<table.*?</table>)', html_content, flags=re.DOTALL)
    
    processed_parts = []
    for part in parts:
        if part.startswith('<table'):
            processed_parts.append(part)
        else:
            processed_part = part.replace('<p>', '').replace('</p>', '')
            processed_parts.append(processed_part)
    
    return ''.join(processed_parts)



if __name__ == "__main__":
    app.run(debug=True)
