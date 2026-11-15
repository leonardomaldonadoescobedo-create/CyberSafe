# 🛡️ CyberSafe

### Learning, Building & Securing.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Development-green)
![Focus](https://img.shields.io/badge/Focus-AI%20Security-red)
![Version](https://img.shields.io/badge/Version-0.4.0-orange)

**CyberSafe** is a Python-based cybersecurity toolkit developed as a Command-Line Interface (CLI) application.

Originally created as an educational programming project, CyberSafe is progressively evolving toward foundational cybersecurity engineering and defensive AI Security applications.

The project currently focuses on password auditing, text analysis, input validation, and structured security event representation.

Its long-term vision is to explore defensive security mechanisms for modern AI-powered applications and Large Language Models (LLMs).

---

## ⚠️ Ethical Disclaimer

CyberSafe is an educational and defensive cybersecurity project.

Its purpose is to explore security concepts, develop defensive tools, and promote responsible software engineering.

All implementations are intended for authorized and ethical use.

---

## 🚀 Key Features

### 1. Password Analyzer

Performs basic password policy validation through automated character checks.

- Minimum password length validation (12 characters).
- Uppercase character detection.
- Lowercase character detection.
- Numeric character detection.
- Individual `PASS`/`FAIL` validation results.
- Basic identification and tracking of weak passwords.

**Security Relevance:** Introduces foundational credential auditing and password policy validation concepts. Its current checks are basic and do not constitute a comprehensive password security assessment.

### 2. Text Analyzer

Performs structural analysis of user-provided text.

- Total character counting.
- Word counting.
- Alphabetic character counting.
- Uppercase character counting.
- Lowercase character counting.
- Numeric character counting.
- Basic text analysis tracking.

**AI Security Relevance:** Provides foundational experience with text inspection, character classification, and input analysis. These concepts will support future input sanitization and preprocessing mechanisms for LLM applications.

### 3. Security Data Manager (Foundation)

Introduces the initial structure for managing security-related event information.

- Security event representation using dictionaries.
- Event identification through predefined IDs.
- Source module classification.
- Security status tracking (`SAFE` / `WARNING`).
- Initial security record generation and display.
- Menu structure for future record management operations.

**Current Limitation:** Record creation and initial display are implemented. Viewing all records, searching, updating, and deleting records are still under development.

### 4. Interactive CLI Architecture

Provides a centralized command-line interface for accessing CyberSafe modules.

- Menu-driven navigation.
- Function-based operation routing.
- Structured program organization.
- Input validation.
- Exception handling using `try/except`.

**Engineering Relevance:** Develops foundational experience with program organization, data handling, error management, and maintainable Python applications.

---

## 💻 Example Output

The following example represents a successful Password Analyzer execution.

```text
=== CyberSafe ===

1. Password Analyzer
2. Text Analyzer
3. Security Data Manager
4. Analysis History
5. About CyberSafe

0. Exit
Which option will you choose?: 1

Introduce a password: [user input]
Minimum (12 characters): PASS
Minimum (a capital): PASS
Minimum (a lowercase): PASS
Minimum (a digit): PASS
The password is secure
```

*Note: This is a representative example of the current CLI implementation.*

---

## ⚙️ Installation & Execution

### Prerequisites

- Python 3.x
- Git
- A terminal or command-line interface.

### 1. Clone the Repository

```bash
git clone <REPOSITORY_URL>
```

### 2. Navigate to the Project Directory

```bash
cd CyberSafe
```

### 3. Execute CyberSafe

```bash
python3 main.py
```

*Note: Replace `main.py` if your main Python file has a different filename.*

---

## 🗺️ Development Roadmap

CyberSafe follows an incremental development approach, expanding from foundational Python programming and cybersecurity tools toward defensive AI Security capabilities.

### Phase 1 — Foundational Cybersecurity

- [x] **v0.1 — Password Analyzer:** Basic password length and character complexity validation.
- [x] **v0.2 — Text Analyzer:** Text metrics and character classification.
- [x] **v0.3 — Security Event Mapping:** Initial structured security event representation.
- [x] **v0.4 — Security Data Manager Foundation:** Initial record generation, event classification, and management menu structure.

### Phase 2 — Security Data Management

- [ ] **v0.5 — Full CRUD Operations:** Implement functional record creation, viewing, searching, updating, and deletion.
- [ ] **v0.6 — Persistent Storage:** Integrate JSON or SQLite for permanent security record storage.
- [ ] **v0.7 — Analysis History & Reporting:** Implement historical event tracking and security report generation.

### Phase 3 — Transition to AI Security

- [ ] **v0.8 — Prompt Injection Detection:** Explore defensive mechanisms for identifying suspicious prompt patterns.
- [ ] **v0.9 — Sensitive Data Protection:** Develop basic PII detection and data sanitization before information reaches an LLM.
- [ ] **v0.10 — LLM Input Security:** Introduce input validation and preprocessing mechanisms for AI-powered applications.

### Phase 4 — Advanced Development

- [ ] **v1.0 — Modular Architecture:** Refactor the application into independent Python modules.
- [ ] **v1.1 — Security Testing:** Introduce automated unit testing and validation workflows.
- [ ] **v1.2 — AI Security Integration:** Explore defensive mechanisms aligned with the OWASP Top 10 for LLM Applications.

---

## 🔬 Technical Direction

CyberSafe aims to progressively explore security challenges associated with modern AI applications.

Future development will investigate:

- LLM Input Security.
- Prompt Injection Defense.
- Personally Identifiable Information (PII) Detection.
- Input Sanitization.
- Secure Data Processing.
- Defensive AI Security Testing.

The project will use the **OWASP Top 10 for LLM Applications** as a technical reference for understanding and prioritizing relevant AI security risks.

These capabilities represent future development objectives and are not currently implemented features.

---

## 📌 Project Status

**Active Development — Fourth Progress (v0.4.0)**

CyberSafe has evolved from basic password and text analysis tools into a CLI application with an initial security event management foundation.

The fourth development stage introduces structured event representation, basic security status classification, and initial record generation.

Current development focuses on strengthening Python programming practices, improving data management, and preparing the foundation for more advanced cybersecurity capabilities.

---

## 👨‍💻 Project Philosophy

CyberSafe is built around continuous learning through practical implementation.

Each development stage introduces new programming concepts, strengthens software engineering practices, and contributes to a deeper understanding of cybersecurity.

The long-term vision is to evolve this educational foundation into a modular defensive security toolkit capable of exploring challenges in modern AI-powered systems.

---

### CyberSafe — Learning, Building & Securing.
