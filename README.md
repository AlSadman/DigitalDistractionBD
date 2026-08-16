# Digital Distraction Behaviour Analysis System (V3.0)

An AI-powered behavioral assessment and analytics web application built with Python Flask and Machine Learning. The system predicts distraction levels, academic impact, social impact, and focus levels, providing customized interventions, interactive charts, and wellness recommendations.

---

## 🚀 Deploying to Vercel

This project is pre-configured for instant deployment on [Vercel](https://vercel.com) via Python Serverless Functions.

### Option A: Deploy via GitHub (Recommended)

1. Push this repository to **GitHub**.
2. Go to the [Vercel Dashboard](https://vercel.com/dashboard) and click **"Add New..."** -> **"Project"**.
3. Import your GitHub repository.
4. Keep the default settings (Framework Preset: *Other*, Root Directory: `./`).
5. (Optional) Add Environment Variables:
   - `SECRET_KEY`: A secure random secret key (e.g. `your-random-secret-key`)
6. Click **Deploy**. Vercel will automatically build the Python runtime and deploy your app.

---

### Option B: Deploy via Vercel CLI

1. Install the Vercel CLI globally (if not already installed):
   ```bash
   npm install -g vercel
   ```
2. Log in to your Vercel account:
   ```bash
   vercel login
   ```
3. Deploy the project from the root folder:
   ```bash
   vercel
   ```
4. For production deployment:
   ```bash
   vercel --prod
   ```

---

## 💻 Local Development

### Prerequisites
- Python 3.10+ (Recommended: Python 3.10 - 3.12)
- `pip`

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd Digital_Distraction_System_V3
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask development server**:
   ```bash
   python app.py
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📁 Project Structure

```text
Digital_Distraction_System_V3/
├── api/
│   └── index.py            # Vercel Serverless Function entry point
├── database/
│   └── history.db          # Pre-seeded SQLite history database
├── model/
│   └── digital_distraction_final_model.pkl # Trained ML multi-output pipeline
├── static/
│   ├── css/                # Stylesheets and animations
│   ├── js/                 # Client scripts and Chart.js integration
│   └── images/             # Visual assets
├── templates/              # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── result.html
│   ├── history.html
│   ├── wellness.html
│   ├── behaviour.html
│   ├── risk_profile.html
│   └── research.html
├── utils/
│   ├── prediction.py       # ML model loader and inference engine
│   ├── database.py         # Serverless-aware SQLite storage & history
│   ├── recommendations.py  # Behavioral intervention generator
│   └── charts.py           # Dashboard analytics & chart data formatter
├── app.py                  # Main Flask application
├── config.py               # Application configurations & mappings
├── requirements.txt        # Production dependencies
├── vercel.json             # Vercel routing & serverless build config
├── .vercelignore           # Deployment ignore rules
└── README.md
```

---

## ⚙️ Configuration & Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `SECRET_KEY` | Flask session secret key | `digital-distraction-system-secret-key` |
| `DATABASE_PATH` | Custom path to SQLite DB file (optional) | Local: `database/history.db`, Vercel: `/tmp/history.db` |
| `VERCEL` | Auto-detected on Vercel platform | `1` on Vercel |

---

## 🛡️ Serverless Architecture Notes
- **Database & Ephemeral Storage**: On Vercel, the file system is read-only except `/tmp`. The system automatically handles this by seeding and operating on `/tmp/history.db`.
- **Pre-trained Models**: Serialized models are dynamically referenced using absolute paths relative to the project root, ensuring compatibility across local machines and cloud serverless instances.
