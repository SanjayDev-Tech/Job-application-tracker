🚀 Job Application Tracker

A modular, OOP-based CLI application to manage, track, and analyze job applications with JSON persistence, analytics insights, and automated follow-up reminders.

📌 Problem It Solves

Job hunting is chaotic.

Applications get lost in emails

Follow-ups are forgotten

No clear insight into success rate

No data-driven improvement

Most students track jobs in Excel or Notion manually.

But real question:

Why not treat job hunting like a system?

This project builds a structured, data-driven job tracking engine.

🧠 Core Idea

Design a scalable backend-style system that:

Models each job application as an object

Persists data using JSON storage

Provides analytics insights

Automates follow-up reminders

This is not just a CRUD app.

It simulates real-world backend architecture principles.

## ✨ Features

- 📌 Add, update, and delete job applications
- 🗂 Persistent storage using JSON
- 📊 Analytics dashboard (status breakdown, success rate, trends)
- ⏰ Automated follow-up reminder detection
- 🧱 Modular clean architecture
- 🧠 Object-Oriented Domain Modeling

🏗 Architecture Overview

The project follows clean modular design:
## 🏗 Architecture Overview

The project follows a clean modular design:

```
job_tracker/
│
├── models.py        # Application entity (OOP core)
├── tracker.py       # Business logic layer
├── storage.py       # JSON persistence engine
├── analytics.py     # Metrics & statistics engine
├── reminders.py     # Follow-up detection system
└── main.py          # CLI interface
```
🔹 OOP-Based Domain Modeling

Each job application is represented as a structured object with:

Company

Role

Date Applied

Status

Notes

ID

Encapsulation ensures data integrity and controlled updates.

🔹 JSON Persistence Layer

Implements:

Object → Dictionary conversion

Dictionary → Object reconstruction

Automatic data saving

State restoration on restart

Simulates lightweight database behavior without external DB dependency.

🔹 Analytics Engine

Generates actionable insights:

Total applications

Interview rate

Rejection ratio

Offer conversion rate

Active vs Closed applications

Turns raw data into measurable performance metrics.

🔹 Automated Follow-Up Reminders

Detects stale applications:

Identifies applications older than X days

Flags pending follow-ups

Encourages proactive job search behavior

🛠 Tech Stack

Python (Core Language)

OOP Principles

JSON File Handling

CLI-Based Interface

Modular Architecture Design

🎯 Engineering Concepts Demonstrated

Object-Oriented Design

Encapsulation

Separation of Concerns

Data Persistence

Basic Analytics Modeling

Clean Code Structuring

Type Hinting

Error Handling

📊 Example Workflow

Add new job application

Update status (Applied → Interview → Offer)

Add notes

Save data automatically

View analytics dashboard

Get follow-up suggestions

🚀 Why This Project Stands Out

Unlike beginner-level CRUD scripts, this project:

Uses layered architecture

Separates domain logic from storage

Simulates real backend design

Demonstrates thinking beyond syntax

It reflects systems thinking, not just Python basics.

📈 Future Enhancements

SQLite integration

Email follow-up automation

Web dashboard (Flask/FastAPI)

CSV export

Data visualization charts

REST API version
