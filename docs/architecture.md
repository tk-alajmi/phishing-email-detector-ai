# Phishing Email Detector AI - Architecture

## System Overview

The Phishing Email Detector AI is a modular cybersecurity tool designed to analyze emails and detect phishing attempts using a multi-layered detection approach.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INPUT                              │
│  (Email Text / File / Paste)                                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   APP.PY (CLI Interface)                    │
│  - Menu System                                              │
│  - Input Handling                                           │
│  - Result Display                                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              PHISHING DETECTOR (detector.py)                │
│  - Orchestrates Analysis Pipeline                           │
│  - Coordinates All Detection Modules                        │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ EMAIL PARSER │ │ UTILS MODULE │ │ PHISHING     │
│              │ │              │ │ MODEL        │
│ - Extract    │ │ - URL Extract│ │              │
│   Headers    │ │ - Domain     │ │ - Scoring    │
│ - Parse Body │ │   Analysis   │ │   Engine     │
│ - Get URLs   │ │ - Shortener  │ │ - Pattern    │
│ - Sender Info│ │   Detection  │ │   Detection  │
└──────────────┘ └──────────────┘ └──────────────┘
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  INDICATOR DETECTION                        │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Text-Based Indicators:                              │   │
│  │  • Urgent Language                                  │   │
│  │  • Credential Requests                              │   │
│  │  • Threat Language                                  │   │
│  │  • Generic Greetings                                │   │
│  │  • Poor Grammar                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ URL-Based Indicators:                               │   │
│  │  • Suspicious URLs                                  │   │
│  │  • Shortened URLs                                   │   │
│  │  • IP Address URLs                                  │   │
│  │  • Suspicious TLDs                                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Domain-Based Indicators:                            │   │
│  │  • Domain Mismatch                                  │   │
│  │  • Spoofing Attempts                                │   │
│  │  • Unusual Sender                                   │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   SCORING ENGINE                            │
│                                                             │
│  Weighted Scoring System:                                   │
│  - Each indicator has assigned weight (0-20 points)         │
│  - Total score calculated (0-100)                           │
│  - Classification based on thresholds:                      │
│    * 0-29:  SAFE                                            │
│    * 30-59: SUSPICIOUS                                      │
│    * 60+:   PHISHING                                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   OUTPUT RESULTS                            │
│                                                             │
│  - Risk Score (0-100)                                       │
│  - Classification (SAFE/SUSPICIOUS/PHISHING)                │
│  - Detected Indicators List                                 │
│  - Detailed Analysis Report                                 │
│  - Security Recommendations                                 │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. CLI Interface (app.py)
- **Purpose**: User interaction layer
- **Functions**:
  - Display menu and banner
  - Accept user input (paste, file, examples)
  - Format and display results with color coding
  - Handle errors gracefully

### 2. Phishing Detector (detector.py)
- **Purpose**: Main orchestration engine
- **Functions**:
  - Coordinate analysis pipeline
  - Combine results from all modules
  - Generate comprehensive reports
  - Calculate final risk assessment

### 3. Email Parser (email_parser.py)
- **Purpose**: Email structure analysis
- **Functions**:
  - Extract headers (From, To, Subject)
  - Parse email body
  - Extract URLs and email addresses
  - Identify sender domain and display name

### 4. Utilities (utils.py)
- **Purpose**: Helper functions for analysis
- **Functions**:
  - URL extraction and validation
  - Domain extraction and analysis
  - Shortened URL detection
  - IP address detection in URLs
  - Suspicious TLD identification

### 5. Phishing Model (model/phishing_model.py)
- **Purpose**: Detection logic and scoring
- **Functions**:
  - Pattern matching for phishing indicators
  - Weighted scoring system
  - Risk classification
  - Keyword and phrase detection

## Detection Pipeline Flow

1. **Input Stage**: User provides email text
2. **Parsing Stage**: Email is parsed into components
3. **Analysis Stage**: Multiple indicators are checked
4. **Scoring Stage**: Weighted score is calculated
5. **Classification Stage**: Risk level is determined
6. **Output Stage**: Results are formatted and displayed

## Indicator Weights

| Indicator | Weight | Description |
|-----------|--------|-------------|
| Credential Request | 20 | Requests for passwords, SSN, etc. |
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

## Extensibility

The modular architecture allows for easy extension:

- **Add new indicators**: Extend PhishingModel class
- **Integrate AI/NLP**: Add API calls in detector.py
- **Custom scoring**: Modify weights in PhishingModel
- **New input methods**: Extend app.py menu system
- **Database logging**: Add logging module for tracking

## Security Considerations

- No external network calls by default (offline analysis)
- No email content is stored or transmitted
- All analysis is performed locally
- Optional AI integration can be configured with API keys
