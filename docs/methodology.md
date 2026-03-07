# Phishing Detection Methodology

## Overview

This document describes the methodology and techniques used by the Phishing Email Detector AI to identify phishing attempts.

## Detection Approach

The system uses a **multi-layered detection approach** combining:

1. **Pattern Matching**: Keyword and phrase detection
2. **Heuristic Analysis**: Rule-based indicator detection
3. **Behavioral Analysis**: Sender and URL behavior patterns
4. **Weighted Scoring**: Risk assessment based on multiple factors

## Phishing Indicators

### 1. Text-Based Indicators

#### Urgent Language Detection
**Purpose**: Identify pressure tactics used by attackers

**Keywords Monitored**:
- "urgent", "immediate", "action required"
- "expires", "suspended", "locked"
- "verify now", "confirm immediately"
- "within 24 hours", "account will be closed"
- "unusual activity", "security alert"

**Weight**: 15 points

**Rationale**: Phishing emails often create false urgency to bypass rational decision-making.

---

#### Credential Request Detection
**Purpose**: Identify attempts to harvest sensitive information

**Keywords Monitored**:
- "password", "username", "social security"
- "credit card", "bank account", "PIN"
- "verify account", "confirm password"
- "personal information", "billing information"
- "CVV", "security code"

**Weight**: 20 points

**Rationale**: Legitimate organizations never request sensitive credentials via email.

---

#### Threat Language Detection
**Purpose**: Identify intimidation tactics

**Keywords Monitored**:
- "suspended", "terminated", "blocked"
- "unauthorized", "fraudulent", "illegal"
- "violation", "breach", "compromised"
- "legal action", "lawsuit"

**Weight**: 10 points

**Rationale**: Attackers use threats to create fear and prompt hasty actions.

---

#### Too Good to Be True Detection
**Purpose**: Identify unrealistic offers

**Keywords Monitored**:
- "won", "winner", "prize", "lottery"
- "free money", "cash prize", "inheritance"
- "million dollars", "congratulations"
- "selected", "lucky", "guarantee"

**Weight**: 10 points

**Rationale**: Scammers lure victims with unrealistic promises.

---

#### Generic Greeting Detection
**Purpose**: Identify lack of personalization

**Patterns Monitored**:
- "Dear Customer", "Dear User"
- "Dear Member", "Dear Account Holder"
- "Dear Sir/Madam", "Dear Valued Customer"

**Weight**: 5 points

**Rationale**: Legitimate organizations typically use personalized greetings.

---

#### Poor Grammar Detection
**Purpose**: Identify unprofessional communication

**Checks**:
- Multiple exclamation marks (!!!)
- Multiple question marks (???)
- Excessive capitalization (>30% of words)

**Weight**: 5 points

**Rationale**: Professional organizations maintain quality standards in communications.

---

### 2. URL-Based Indicators

#### Suspicious URL Detection
**Purpose**: Identify malicious or deceptive links

**Analysis**:
- URLs containing keywords like "login", "verify", "account", "secure"
- URLs from non-trusted domains using trusted brand names
- Mismatched display text and actual URL

**Weight**: 20 points

**Rationale**: Attackers often use deceptive URLs to mimic legitimate sites.

---

#### Shortened URL Detection
**Purpose**: Identify obfuscated links

**Services Monitored**:
- bit.ly, tinyurl.com, goo.gl, t.co
- ow.ly, is.gd, buff.ly, and 70+ others

**Weight**: 10 points

**Rationale**: URL shorteners hide the true destination, commonly used in phishing.

---

#### IP Address URL Detection
**Purpose**: Identify URLs using IP addresses instead of domains

**Pattern**: IPv4 addresses (e.g., http://192.168.1.1)

**Weight**: 15 points

**Rationale**: Legitimate sites use domain names, not raw IP addresses.

---

#### Suspicious TLD Detection
**Purpose**: Identify uncommon or suspicious top-level domains

**TLDs Monitored**:
- .tk, .ml, .ga, .cf, .gq (free domains)
- .xyz, .top, .work, .click (commonly abused)

**Weight**: 10 points

**Rationale**: These TLDs are frequently used for malicious purposes.

---

### 3. Domain-Based Indicators

#### Domain Mismatch Detection
**Purpose**: Identify sender/content domain inconsistencies

**Analysis**:
- Compare sender domain with URL domains
- Check for brand impersonation
- Detect mismatched company references

**Weight**: 15 points

**Rationale**: Phishers often claim to represent one company while linking to another.

---

#### Spoofing Attempt Detection
**Purpose**: Identify display name spoofing

**Analysis**:
- Compare display name with actual email domain
- Check for trusted brand names in display with different domain
- Detect Unicode/homograph attacks

**Weight**: 15 points

**Rationale**: Attackers use familiar names to build false trust.

---

#### Unusual Sender Detection
**Purpose**: Identify suspicious sender domains

**Patterns**:
- Domains containing "secure-", "verify-", "account-"
- Domains with suspicious patterns
- Non-standard domain structures

**Weight**: 10 points

**Rationale**: Legitimate organizations use consistent, professional domains.

---

### 4. Content-Based Indicators

#### Attachment Mention Detection
**Purpose**: Identify potential malware delivery attempts

**Keywords**:
- "attachment", "attached", "file"
- "document", "PDF", "invoice"
- "download", "click here", "open"

**Weight**: 5 points

**Rationale**: Phishing emails often use malicious attachments.

---

## Scoring System

### Score Calculation

```
Total Score = Σ (Indicator Weight × Indicator Presence)

Where:
- Indicator Weight: Predefined weight (0-20)
- Indicator Presence: 1 if detected, 0 if not
- Total Score: Capped at 100
```

### Classification Thresholds

| Score Range | Classification | Risk Level | Recommendation |
|-------------|----------------|------------|----------------|
| 0-29 | SAFE | Low | Email appears legitimate |
| 30-59 | SUSPICIOUS | Medium | Exercise caution, verify sender |
| 60-100 | PHISHING | High | Do not interact, report email |

### Threshold Rationale

**SAFE (0-29)**:
- Few or no indicators detected
- Likely legitimate communication
- Standard security practices still apply

**SUSPICIOUS (30-59)**:
- Multiple minor indicators OR one major indicator
- Could be legitimate but requires verification
- User should independently verify before taking action

**PHISHING (60+)**:
- Multiple major indicators detected
- High probability of phishing attempt
- User should not interact with email

---

## Detection Accuracy

### Strengths

1. **Multi-layered approach**: Reduces false positives
2. **Weighted scoring**: Prioritizes critical indicators
3. **Comprehensive coverage**: Checks text, URLs, and domains
4. **No external dependencies**: Works offline
5. **Fast analysis**: Real-time results

### Limitations

1. **Sophisticated attacks**: May miss highly targeted spear-phishing
2. **Zero-day techniques**: New attack methods not yet in patterns
3. **Context-dependent**: Cannot verify actual sender identity
4. **Language-specific**: Optimized for English emails
5. **No attachment scanning**: Cannot analyze file contents

### Improvement Opportunities

1. **Machine Learning Integration**: Train on labeled phishing datasets
2. **NLP Enhancement**: Use advanced language models (GPT, BERT)
3. **Real-time Threat Intelligence**: Check URLs against threat databases
4. **Sender Reputation**: Integrate SPF/DKIM/DMARC validation
5. **Attachment Analysis**: Add file hash checking and sandboxing

---

## Best Practices for Users

Even with automated detection, users should:

1. **Verify sender independently**: Contact organization through official channels
2. **Hover over links**: Check actual URL before clicking
3. **Look for HTTPS**: Ensure secure connections
4. **Check for personalization**: Legitimate emails use your name
5. **Be skeptical of urgency**: Take time to verify urgent requests
6. **Report suspicious emails**: Help improve detection systems
7. **Use multi-factor authentication**: Adds security layer
8. **Keep software updated**: Protect against known vulnerabilities

---

## Technical Implementation

### Pattern Matching

```python
# Example: Urgent language detection
urgent_keywords = ['urgent', 'immediate', 'action required', ...]
text_lower = email_text.lower()
detected = any(keyword in text_lower for keyword in urgent_keywords)
```

### URL Analysis

```python
# Example: Extract and analyze URLs
urls = extract_urls(email_text)
for url in urls:
    domain = extract_domain(url)
    if is_shortened_url(url):
        score += 10
    if has_ip_address(url):
        score += 15
```

### Domain Comparison

```python
# Example: Check domain mismatch
sender_domain = get_sender_domain(email)
url_domains = [get_domain(url) for url in urls]
if 'paypal' in sender_domain and 'paypal' not in url_domains:
    score += 15  # Domain mismatch
```

---

## Continuous Improvement

The detection methodology should be regularly updated:

1. **Monitor new phishing techniques**: Stay current with threat landscape
2. **Analyze false positives/negatives**: Refine weights and patterns
3. **Update keyword lists**: Add new phishing phrases
4. **Expand URL shortener database**: Track new services
5. **Incorporate user feedback**: Learn from real-world usage

---

## Conclusion

This methodology provides a robust foundation for phishing detection through:

- **Comprehensive indicator coverage**
- **Balanced scoring system**
- **Clear risk classification**
- **Actionable recommendations**

While no system is perfect, this multi-layered approach significantly improves email security awareness and reduces phishing success rates.
