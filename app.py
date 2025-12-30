from flask import Flask, send_file
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/")
def generate_pdf():

    html = """
    <!DOCTYPE html>
    <html lang="te">
    <head>
    <meta charset="UTF-8">
    <style>
    @font-face {
      font-family: 'NotoTelugu';
      src: url('https://fonts.gstatic.com/s/notoseriftelugu/v27/tDbu2oqkWl0zqCL7g1W8KOZK0C1k.ttf');
    }
    body {
      font-family: 'NotoTelugu', serif;
      font-size: 14px;
    }
    table {
      border-collapse: collapse;
      width: 100%;
    }
    th, td {
      border: 1px solid black;
      padding: 6px;
    }
    </style>
    </head>
    <body>

    <h2>Monthly Report</h2>

    <table>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Amount</th>
      </tr>
      <tr>
        <td>1</td>
        <td>వడ్లమాని. రాఘవులు నాయుడు</td>
        <td>5000</td>
      </tr>
      <tr>
        <td>2</td>
        <td>కుట్టుబోయిన. వరలక్ష్మమ్మ</td>
        <td>4200</td>
      </tr>
    </table>

    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html)
        page.pdf(path="report.pdf", format="A4")
        browser.close()

    return send_file("report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run()
