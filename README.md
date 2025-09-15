# 📊 My Dashboard Tools — Streamlit, Dash & Bokeh  

Welcome! This repository shows **three popular ways to build dashboards in Python** — **Streamlit**, **Dash (Plotly)**, and **Bokeh** — with ready-to-run code, containerization, and CI/CD deployment to Google Cloud Run. 🚀  

---

## 🔎 Features
- ✅ Minimal, clean examples of each framework.  
- 🐳 Docker support (for Dash & Bokeh).  
- ☁️ GitHub Actions pipeline → Build → Deploy to **Google Cloud Run**.  
- 📖 Easy-to-follow structure.  

---

## 📂 Repository Structure

```
my-dashboard/
├─ streamlit_app.py      # Streamlit demo
├─ app.py                # Dash demo
├─ main.py               # Bokeh demo
├─ requirements.txt      # Python dependencies
├─ Dockerfile            # For Dash/Bokeh container builds
└─ .github/
   └─ workflows/
      └─ deploy-cloudrun.yml   # CI/CD pipeline
```

---

## 🚀 Quickstart (Local)

### 1) Streamlit
```bash
pip install streamlit pandas altair
streamlit run streamlit_app.py
```

### 2) Dash
```bash
pip install dash pandas plotly gunicorn
python app.py
```

### 3) Bokeh
```bash
pip install bokeh
bokeh serve --show main.py
```

---

## 🐳 Run with Docker (Dash or Bokeh)

```bash
docker build -t my-dashboard .
docker run -p 8080:8080 my-dashboard
```

---

## ⚡ CI/CD — GitHub Actions → Cloud Run  

This repo comes with a prebuilt GitHub Actions workflow:  

- 🧪 **Test**: run checks/linting.  
- 🏗️ **Build**: containerize app with Cloud Build.  
- ☁️ **Deploy**: publish to Cloud Run.  

Workflow file: `.github/workflows/deploy-cloudrun.yml`  

---

✨ **Tip:** Fork this repo, experiment with the apps, and customize deployment for your own projects!  
