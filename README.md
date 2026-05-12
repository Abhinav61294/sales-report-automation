## Author
Abhinav Saxena

# Sales Report Automation Tool

## Overview
This project automates sales data analysis and reporting using Python.

The tool processes raw e-commerce sales data, generates business insights, creates charts, and exports automated Excel reports.

---

## Features
- Load and process CSV sales datasets
- Clean missing values
- Generate business KPIs
- Identify top-selling categories
- Analyze regional performance
- Generate monthly sales reports
- Create automated charts
- Export Excel reports automatically

---

## Technologies Used
- Python
- Pandas
- Matplotlib
- OpenPyXL

---

## Project Structure

sales-report-automation/
│
├── input/
├── output/
├── charts/
├── main.py
├── requirements.txt
└── README.md

---

## Outputs
### Generated Files
- Monthly sales chart (`charts/monthly_sales.png`)
- Automated Excel report (`output/final_report.xlsx`)

---

## How to Run

Install dependencies:

```bash
pip install pandas matplotlib openpyxl
```

Run the project:

```bash
python main.py
```

---

## Future Improvements
- Interactive dashboards
- Automated email reports
- Streamlit web interface
- Cloud deployment