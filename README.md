# 🖥️ System Info Script

Simple Python CLI application for displaying system information such as CPU, memory, disk usage, and OS details.

---

## 🎯 Project Goal

The goal of this project was to:

* practice Python fundamentals
* work with system-level data
* build a simple interactive CLI application
* simulate a basic monitoring tool (DevOps-oriented)

---

## ⚙️ Features

* Display system information (OS, hostname, boot time)
* Show CPU usage and core count
* Monitor memory and swap usage
* Display disk usage and partitions
* Interactive menu for selecting specific data
* Clear screen between actions for better user experience

---

## 🛠️ Technologies Used

* Python
* `psutil` – system resource monitoring
* `platform` – OS information
* `colorama` – colored CLI output

---

## 🚀 How It Works

1. User runs the script
2. Interactive menu is displayed
3. User selects what information to view:

   * system
   * CPU
   * memory
   * disk
4. Selected data is displayed in the console
5. Screen is cleared between actions for better readability
6. Program runs continuously until user exits

---

## 🧠 What I Learned

* Working with external Python libraries (`psutil`, `colorama`)
* Handling user input in CLI applications
* Structuring code using functions
* Creating interactive loops (`while True`)
* Improving user experience in terminal applications

---

## ⚠️ Challenges & Solutions

**Problem:**
Issues with Python environment and library installation on Windows

**Solution:**
Used WSL (Linux environment) and proper package installation with:

```bash
pip install psutil colorama
```

---

**Problem:**
Accidentally committed `venv` directory to GitHub

**Solution:**

* Removed it using `git rm -r --cached venv`
* Added `.gitignore` to prevent future issues

---

## 📦 Installation

```bash
git clone https://github.com/your-username/system-info-script.git
cd system-info-script
pip install -r requirements.txt
python main.py
```

---

## 📌 Future Improvements

* Add real-time monitoring (auto-refresh)
* Implement warning alerts (e.g. high CPU usage)
* Export logs to file
* Improve UI layout

---

## 👤 Author

Martin Tomcik
Aspiring DevOps Engineer ☁️
