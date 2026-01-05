from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("ENVIRONMENT", "unknown")
    version = os.getenv("VERSION", "1.0.0")
    pod = socket.gethostname()
    
    return f"""
    <html>
    <head>
        <title>CI/CD Demo - {env}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }}
            .container {{
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.2);
                text-align: center;
            }}
            h1 {{ color: #333; }}
            .env {{ 
                display: inline-block;
                padding: 10px 20px;
                margin: 20px 0;
                border-radius: 5px;
                font-weight: bold;
                font-size: 1.2em;
            }}
            .dev {{ background: #4CAF50; color: white; }}
            .qa {{ background: #FF9800; color: white; }}
            .prod {{ background: #f44336; color: white; }}
            .info {{ 
                margin-top: 20px;
                padding: 15px;
                background: #f5f5f5;
                border-radius: 5px;
            }}
            .info p {{ margin: 5px 0; color: #666; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>CI/CD Pipeline Demo</h1>
            <div class="env {env}">{env.upper()} Environment</div>
            <div class="info">
                <p><strong>Version:</strong> {version}</p>
                <p><strong>Pod:</strong> {pod}</p>
                <p><strong>Status:</strong> Running</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

