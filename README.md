# ⚡ Electricity Bill Generator

A web-based Electricity Bill Generator developed using **Python, Flask, MySQL, HTML, CSS, PDFKit, and wkhtmltopdf**. The application automates electricity bill calculation based on unit consumption, stores consumer and billing records in a database, and generates downloadable PDF bills.

This project demonstrates full-stack web development, database integration, backend processing, and dynamic PDF generation.

---

## 📌 Project Overview

The Electricity Bill Generator is designed to automate the process of electricity bill generation. Users can search consumers using their consumer number, calculate bills based on electricity consumption, store records in a MySQL database, and download professionally formatted PDF bills.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Programming |
| Flask | Web Framework |
| MySQL | Database Management |
| HTML5 | Frontend Structure |
| CSS3 | User Interface Styling |
| Jinja2 | Dynamic Template Rendering |
| PDFKit | PDF Generation |
| wkhtmltopdf | HTML-to-PDF Engine |
| Git | Version Control |
| GitHub | Project Hosting |

---

## 🧠 My Knowledge & Usage

| Technology | Usage in Project | Knowledge Level |
|------------|-----------------|----------------|
| Python | Business logic, bill calculation, database operations | Intermediate |
| Flask | Routing, form handling, template rendering | Intermediate |
| MySQL | Database design, queries, data storage | Intermediate |
| HTML5 | Page structure, forms, tables | Intermediate |
| CSS3 | Styling, responsive layouts, bill formatting | Intermediate |
| Jinja2 | Dynamic data rendering in templates | Intermediate |
| PDFKit | PDF bill generation from HTML templates | Beginner to Intermediate |
| wkhtmltopdf | HTML to PDF conversion engine | Beginner |
| Git | Version control and project tracking | Beginner to Intermediate |
| GitHub | Code hosting and project management | Beginner to Intermediate |

---

## 📂 Project Structure

```text
Electricity_bill/
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       └── logo.png
│
├── templates/
│   ├── index.html
│   ├── consumer.html
│   └── bill.html
│
├── app.py
├── database.py
├── electricity_bill.sql
├── README.md
└── requirements.txt
```

---

## 🗄️ Database Design

### Consumers Table

Stores consumer information:

- Consumer Number
- Consumer Name
- Mobile Number
- Email Address
- Address
- Division
- Meter Number
- Sanctioned Load
- Connection Date

### Bills Table

Stores generated bill details:

- Bill Number
- Consumer Number
- Bill Month
- Bill Date
- Due Date
- Units Consumed
- Current Bill
- Previous Due
- Payable Amount

---

## 🎯 Learning Outcomes

- Full Stack Web Development
- Python Backend Development
- Flask Web Framework
- MySQL Database Integration
- SQL Query Handling
- Dynamic Web Applications
- PDF Generation using PDFKit
- Frontend and Backend Integration
- Software Project Structure
- Version Control using Git and GitHub
- Real-World Application Development

---

## 🔮 Future Enhancements

- Online Bill Payment Gateway
- Email Bill Delivery
- SMS Notifications
- Admin Dashboard
- Consumer Registration Module
- Bill Payment History
- Monthly Usage Analytics
- Report Generation
- Multi-User Authentication
- Role-Based Access Control
