# 🛒 E-Commerce Selenium Testing Project

Automated test suite for an e-commerce web application using **Selenium WebDriver** and **Python**. Built to demonstrate functional testing skills across core e-commerce workflows.

---

## 📌 Project Overview

This project automates testing of the [SauceDemo](https://www.saucedemo.com) e-commerce demo site — a standard industry practice site used for QA automation practice.

**Test Coverage:**

| Module | Test File | Test Cases |
|--------|-----------|------------|
| Login & Authentication | `test_login.py` | 5 |
| Product Listing & Sorting | `test_product.py` | 5 |
| Shopping Cart | `test_cart.py` | 5 |
| Checkout Flow | `test_checkout.py` | 5 |
| **Total** | | **20** |

---

## 🧰 Tech Stack

- **Language:** Python 3.x
- **Automation Tool:** Selenium WebDriver 4.x
- **Test Framework:** pytest
- **Browser:** Google Chrome (Headless mode)
- **Driver Management:** webdriver-manager

---

## 📁 Project Structure

```
selenium-ecommerce-tests/
│
├── tests/
│   ├── test_login.py        # Login, logout, and auth tests
│   ├── test_product.py      # Product listing and sorting tests
│   ├── test_cart.py         # Add/remove cart item tests
│   └── test_checkout.py     # End-to-end checkout flow tests
│
├── conftest.py              # Shared pytest fixtures and configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.8 or higher
- Google Chrome browser installed

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Pulendar-7564/selenium-ecommerce-tests.git
cd selenium-ecommerce-tests

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run all tests
pytest tests/ -v

# 4. Run a specific test file
pytest tests/test_login.py -v

# 5. Run tests with HTML report
pytest tests/ -v --html=report.html
```

---

## 🧪 Test Cases

### Login Tests (`test_login.py`)
| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| TC_LOGIN_001 | Valid login | Redirected to inventory page |
| TC_LOGIN_002 | Invalid password | Error message displayed |
| TC_LOGIN_003 | Empty credentials | "Username is required" error |
| TC_LOGIN_004 | Locked out user | "Locked out" error message |
| TC_LOGIN_005 | Logout | Redirected back to login page |

### Product Tests (`test_product.py`)
| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| TC_PROD_001 | Products displayed | At least 1 product visible |
| TC_PROD_002 | Name and price visible | All products have name and price |
| TC_PROD_003 | Sort by price low-high | Prices in ascending order |
| TC_PROD_004 | Sort by name A-Z | Names in alphabetical order |
| TC_PROD_005 | Product detail page | Correct product details shown |

### Cart Tests (`test_cart.py`)
| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| TC_CART_001 | Add item to cart | Badge shows count 1 |
| TC_CART_002 | Add multiple items | Badge shows correct count |
| TC_CART_003 | Remove item | Badge disappears |
| TC_CART_004 | Cart page shows item | Item listed in cart |
| TC_CART_005 | Continue shopping | Returns to inventory |

### Checkout Tests (`test_checkout.py`)
| ID | Test Case | Expected Result |
|----|-----------|-----------------|
| TC_CHK_001 | Checkout page loads | Step 1 URL visible |
| TC_CHK_002 | Valid checkout details | Proceeds to step 2 |
| TC_CHK_003 | Missing first name | Error message shown |
| TC_CHK_004 | Order summary | Item visible in summary |
| TC_CHK_005 | Complete order | "Thank you" confirmation shown |

---

## 👤 Author

**Pulendar Golla**  
📧 gpulendar1619@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/pulendar-golla) | [GitHub](https://github.com/Pulendar-7564)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
