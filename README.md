# 🎯 Phishing Email Detector AI

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Security](https://img.shields.io/badge/security-phishing%20detection-red)
![Status](https://img.shields.io/badge/status-active-success)

**AI-powered phishing email detection tool with risk scoring and suspicious link analysis for cybersecurity professionals**

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Output](#-example-output)
- [Detection Methodology](#-detection-methodology)
- [Project Structure](#-project-structure)
- [Architecture](#-architecture)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🔍 Overview

Phishing Email Detector AI is a comprehensive cybersecurity tool designed to analyze emails and detect phishing attempts using advanced pattern recognition, heuristic analysis, and weighted scoring algorithms. Built for SOC analysts, security engineers, and cybersecurity professionals, this tool provides detailed risk assessments and actionable insights.

### Why This Tool?

- **🛡️ Enhanced Security**: Protect against phishing attacks with multi-layered detection
- **⚡ Real-time Analysis**: Instant email analysis with detailed reporting
- **🎯 High Accuracy**: Weighted scoring system minimizes false positives
- **📊 Detailed Reports**: Comprehensive breakdown of detected indicators
- **🔒 Privacy-Focused**: All analysis performed locally, no data transmission
- **🎓 Educational**: Learn about phishing techniques and detection methods

---

## ✨ Features

### Core Capabilities

- ✅ **Email Phishing Detection** - Analyze emails for phishing indicators
- ✅ **Risk Scoring System** - 0-100 risk score with classification (SAFE/SUSPICIOUS/PHISHING)
- ✅ **Suspicious Link Detection** - Identify malicious URLs, shortened links, and IP-based URLs
- ✅ **Domain Analysis** - Detect domain spoofing and mismatches
- ✅ **Pattern Recognition** - Identify urgent language, credential requests, and threats
- ✅ **Sender Verification** - Analyze sender domains and detect spoofing attempts
- ✅ **Grammar Analysis** - Detect poor grammar and unprofessional formatting
- ✅ **Multiple Input Methods** - Paste text, load from file, or use examples
- ✅ **Color-Coded Output** - Easy-to-read terminal interface with risk visualization
- ✅ **Detailed Reporting** - Comprehensive analysis with detected indicators

### Detection Indicators

#### Text-Based Indicators
- 🚨 Urgent/pressure language
- 🔑 Credential harvesting attempts
- ⚠️ Threat and intimidation language
- 🎁 Too-good-to-be-true offers
- 👤 Generic greetings (lack of personalization)
- 📝 Poor grammar and spelling

#### URL-Based Indicators
- 🔗 Suspicious URLs with phishing patterns
- 📎 Shortened URLs (bit.ly, tinyurl, etc.)
- 🌐 IP address URLs instead of domains
- 🏴 Suspicious top-level domains (.tk, .ml, etc.)

#### Domain-Based Indicators
- 🎭 Domain mismatch between sender and links
- 👻 Email spoofing attempts
- 🔍 Unusual sender domains

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/tk-alajmi/phishing-email-detector-ai.git
cd phishing-email-detector-ai
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
python app.py
```

---

## 💻 Usage

### Interactive CLI Mode

Run the application and follow the interactive menu:

```bash
python app.py
```

### Menu Options

1. **Paste email text directly** - Copy and paste email content
2. **Load email from file** - Analyze email from a text file
3. **Analyze example phishing email** - Test with provided phishing sample
4. **Analyze example safe email** - Test with provided safe email sample
5. **Exit** - Close the application

### Example: Analyzing an Email from File

```bash
python app.py
# Select option 2
# Enter file path: examples/phishing_email_sample.txt
```

### Example: Pasting Email Text

```bash
python app.py
# Select option 1
# Paste your email content
# Type 'END' on a new line when finished
```

---

## 📊 Example Output

### Phishing Email Detection

```
======================================================================
EMAIL ANALYSIS RESULT
======================================================================

Risk Score: 85/100
Classification: PHISHING

Email Details:
----------------------------------------------------------------------
Subject: URGENT: Your PayPal Account Has Been Suspended
Sender: security-alert@paypal-verify-account.tk
URLs Found: 2

Detected Phishing Indicators:
----------------------------------------------------------------------
  • Urgent Language
  • Credential Request
  • Suspicious Url
  • Domain Mismatch
  • Shortened Url
  • Suspicious Tld
  • Threat Language
  • Generic Greeting

======================================================================

✗ RECOMMENDATION: This email is likely a phishing attempt. 
  Do NOT click links or provide information.

======================================================================
```

### Safe Email Detection

```
======================================================================
EMAIL ANALYSIS RESULT
======================================================================

Risk Score: 5/100
Classification: SAFE

Email Details:
----------------------------------------------------------------------
Subject: [GitHub] Your pull request was merged
Sender: noreply@github.com
URLs Found: 3

Detected Phishing Indicators:
----------------------------------------------------------------------
  • Attachment Mention

======================================================================

✓ RECOMMENDATION: This email appears to be safe.

======================================================================
```

---

## 🧠 Detection Methodology

The tool uses a **weighted scoring system** where each indicator contributes to the final risk score:

| Indicator | Weight | Description |
|-----------|--------|-------------|
| Credential Request | 20 | Requests for passwords, SSN, credit cards |
| Suspicious URL | 20 | URLs with phishing patterns |
| Urgent Language | 15 | Pressure tactics and urgency |
| Domain Mismatch | 15 | Sender domain doesn't match content |
| Spoofing Attempt | 15 | Display name spoofing |
| IP Address URL | 15 | URLs using IP instead of domain |
| Threat Language | 10 | Threatening consequences |
| Shortened URL | 10 | Use of URL shorteners |
| Suspicious TLD | 10 | Uncommon or suspicious domains |
| Too Good to Be True | 10 | Unrealistic offers |
| Unusual Sender | 10 | Suspicious sender domain |
| Generic Greeting | 5 | Lack of personalization |
| Poor Grammar | 5 | Grammar and spelling issues |
| Attachment Mention | 5 | References to attachments |

### Risk Classification

- **SAFE (0-29)**: Email appears legitimate
- **SUSPICIOUS (30-59)**: Exercise caution, verify sender
- **PHISHING (60-100)**: High probability of phishing attempt

For detailed methodology, see [docs/methodology.md](docs/methodology.md)

---

## 📁 Project Structure

```
phishing-email-detector-ai/
│
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
│
├── app.py                         # Main CLI application
├── detector.py                    # Phishing detection engine
├── email_parser.py                # Email parsing module
├── utils.py                       # Utility functions
│
├── model/
│   └── phishing_model.py          # Scoring and pattern detection
│
├── examples/
│   ├── phishing_email_sample.txt  # Example phishing email
│   └── safe_email_sample.txt      # Example safe email
│
├── docs/
│   ├── architecture.md            # System architecture
│   └── methodology.md             # Detection methodology
│
└── screenshots/
    ├── demo1.png                  # Running the tool
    ├── demo2.png                  # Analyzing phishing email
    └── demo3.png                  # Analysis results
```

---

## 🏗️ Architecture

The system follows a modular architecture with clear separation of concerns:

```
User Input  CLI Interface  Phishing Detector  Email Parser
                                    
                            Indicator Detection
                                    
                    ┌───────────────┼───────────────┐
                                                  
              Text Analysis    URL Analysis   Domain Analysis
                                                  
                    └───────────────┼───────────────┘
                                    
                            Scoring Engine
                                    
                        Risk Classification
                                    
                          Formatted Output
```

For detailed architecture, see [docs/architecture.md](docs/architecture.md)

---

## 🎯 Use Cases

### For Security Professionals
- **SOC Analysts**: Quick triage of suspicious emails
- **Security Engineers**: Integration into security workflows
- **Incident Responders**: Rapid phishing assessment
- **Security Trainers**: Educational demonstrations

### For Organizations
- **Email Security**: First-line defense against phishing
- **User Training**: Teach employees to recognize phishing
- **Threat Intelligence**: Analyze phishing campaigns
- **Security Audits**: Test email security awareness

---

## 🔧 Advanced Configuration

### Customizing Detection Weights

Edit `model/phishing_model.py` to adjust indicator weights:

```python
self.weights = {
    'urgent_language': 15,      # Adjust weight (0-20)
    'suspicious_url': 20,
    # ... other indicators
}
```

### Adding Custom Keywords

Extend keyword lists in `model/phishing_model.py`:

```python
self.urgent_keywords = [
    'urgent', 'immediate',
    # Add your custom keywords
]
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue describing the bug
2. **Suggest Features**: Share ideas for new features
3. **Submit Pull Requests**: Contribute code improvements
4. **Improve Documentation**: Help make docs clearer
5. **Share Feedback**: Let us know how you're using the tool

### Development Setup

```bash
git clone https://github.com/tk-alajmi/phishing-email-detector-ai.git
cd phishing-email-detector-ai
pip install -r requirements.txt
# Make your changes
# Test thoroughly
# Submit pull request
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Turki Alajmi**

- GitHub: [@tk-alajmi](https://github.com/tk-alajmi)
- Project: [Phishing Email Detector AI](https://github.com/tk-alajmi/phishing-email-detector-ai)

---

## 🙏 Acknowledgments

- Inspired by real-world phishing attacks and cybersecurity best practices
- Built for the cybersecurity community
- Designed for educational and professional use

---

## ⚠️ Disclaimer

This tool is provided for educational and professional cybersecurity purposes. While it provides valuable analysis, it should be used as part of a comprehensive security strategy, not as the sole defense against phishing attacks. Always exercise caution with suspicious emails.

---

## 📞 Support

If you encounter issues or have questions:

1. Check the [documentation](docs/)
2. Review [existing issues](https://github.com/tk-alajmi/phishing-email-detector-ai/issues)
3. Open a new issue with details

---

## 🔮 Future Enhancements

- [ ] Machine learning integration for improved accuracy
- [ ] Real-time threat intelligence integration
- [ ] Email attachment analysis
- [ ] SPF/DKIM/DMARC validation
- [ ] Web interface (GUI)
- [ ] API endpoint for integration
- [ ] Multi-language support
- [ ] Database logging and analytics
- [ ] Automated reporting

---

<div align="center">

**⭐ Star this repository if you find it useful! ⭐**

**Made with ❤️ for the Cybersecurity Community**

</div>
