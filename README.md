# 🚀 API Testing Framework (Python + Pytest)

![API Testing](https://img.shields.io/badge/API-Testing-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A lightweight and scalable **API Testing Framework** built using Python.
This project demonstrates automated API testing using **requests** and **pytest**, covering real-world scenarios like GET and POST requests, response validation, and data verification.

---

## 📌 Features

* ✅ Automated API Testing using Python
* ✅ GET & POST request validation
* ✅ JSON response validation
* ✅ Status code verification
* ✅ Clean and modular structure
* ✅ Easily extendable for real-world APIs

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=python" height="40"/>
  <img src="https://skillicons.dev/icons?i=git" height="40"/>
  <img src="https://skillicons.dev/icons?i=github" height="40"/>
  <img src="https://skillicons.dev/icons?i=vscode" height="40"/>
</p>

* Python
* Requests Library
* Pytest Framework

---

## 📂 Project Structure

```id="api1"
api-testing-framework/
│
├── utils/
│   └── api_client.py
│
├── tests/
│   ├── test_get_users.py
│   └── test_create_user.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash id="api2"
git clone https://github.com/YOUR_USERNAME/api-testing-framework.git
cd api-testing-framework
```

---

### 2️⃣ Install Dependencies

```bash id="api3"
pip install -r requirements.txt
```

---

### 3️⃣ Run Test Cases

```bash id="api4"
pytest -v
```

---

## 📊 Test Scenarios Covered

| Test Case          | Description                       |
| ------------------ | --------------------------------- |
| GET Users          | Fetch users and validate response |
| Validate Response  | Check JSON structure and data     |
| Create User (POST) | Send data and verify API response |

---

## 🌐 API Used

This project uses a public API:

```id="api5"
https://jsonplaceholder.typicode.com
```

✔ No authentication required
✔ Stable for testing

---

## 🔥 Key Highlights

* Designed using modular architecture
* Validates real API responses using assertions
* Handles real-world API changes (authentication issues handled)
* Beginner-friendly but scalable for advanced use

---

## 🧠 Learnings from this Project

* Writing automated API test cases
* Handling HTTP methods (GET, POST)
* Parsing and validating JSON responses
* Using pytest for test execution

---

## 🚀 Future Improvements

* Add PUT & DELETE API tests
* Integrate logging system
* Add test reports (Allure / HTML)
* Add environment configuration

---

## 🤝 Contribution

Contributions are welcome. Feel free to fork and improve.

---

## 📧 Contact

**Sumit Singh Chouhan**
BTech CSE | Python Developer

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub.
