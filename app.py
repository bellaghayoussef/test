from flask import Flask, jsonify, request
from playwright.sync_api import sync_playwright

app = Flask(__name__)

# Test route
@app.route("/scrape/<path:url>", methods=["GET"])
def scrape(url):    
    target_url = f"https://vitrina.hstn.me/api/{url}"  # <-- f-string fixes it
    print(target_url)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
        print(target_url)
        page = browser.new_page()
        page.goto(target_url)
        
        # Get raw response body (not just HTML content)
        content = page.evaluate("() => document.body.innerText")
        
        browser.close()
    z
    try:
        # Return JSON directly
        return jsonify(eval(content))
    except Exception:
        # If not JSON, return raw content
        return content

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', False), host='0.0.0.0', port=8080)