"""
Phishing detection model with scoring logic
"""

from typing import Dict, List, Tuple
import re

class PhishingModel:
    """
    Machine learning-inspired phishing detection model
    Uses weighted scoring system for phishing indicators
    """
    
    def __init__(self):
        """
        Initialize the phishing model with weights and keywords
        """
        # Phishing indicator weights (0-100 scale)
        self.weights = {
            'urgent_language': 15,
            'suspicious_url': 20,
            'domain_mismatch': 15,
            'credential_request': 20,
            'shortened_url': 10,
            'ip_address_url': 15,
            'suspicious_tld': 10,
            'spoofing_attempt': 15,
            'poor_grammar': 5,
            'generic_greeting': 5,
            'threat_language': 10,
            'too_good_to_be_true': 10,
            'attachment_mention': 5,
            'unusual_sender': 10
        }
        
        # Phishing keywords and patterns
        self.urgent_keywords = [
            'urgent', 'immediate', 'action required', 'act now', 'limited time',
            'expires', 'suspended', 'locked', 'verify now', 'confirm immediately',
            'within 24 hours', 'account will be closed', 'unusual activity',
            'security alert', 'verify your account', 'confirm your identity',
            'update your information', 'click here immediately', 'respond now'
        ]
        
        self.credential_keywords = [
            'password', 'username', 'social security', 'ssn', 'credit card',
            'bank account', 'account number', 'pin', 'verify account',
            'confirm password', 'update password', 'reset password',
            'login credentials', 'personal information', 'billing information',
            'payment details', 'card details', 'cvv', 'security code'
        ]
        
        self.threat_keywords = [
            'suspended', 'terminated', 'blocked', 'restricted', 'disabled',
            'unauthorized', 'fraudulent', 'illegal', 'violation', 'breach',
            'compromised', 'hacked', 'stolen', 'legal action', 'lawsuit'
        ]
        
        self.too_good_keywords = [
            'won', 'winner', 'prize', 'lottery', 'free money', 'cash prize',
            'inheritance', 'million dollars', 'claim your', 'congratulations',
            'selected', 'chosen', 'lucky', 'bonus', 'reward', 'gift card',
            'free gift', 'no cost', 'risk free', 'guarantee'
        ]
        
        self.generic_greetings = [
            'dear customer', 'dear user', 'dear member', 'dear account holder',
            'dear sir/madam', 'dear valued customer', 'hello user',
            'dear client', 'dear friend'
        ]
        
        self.trusted_domains = [
            'google.com', 'microsoft.com', 'apple.com', 'amazon.com',
            'paypal.com', 'facebook.com', 'twitter.com', 'linkedin.com',
            'github.com', 'stackoverflow.com', 'reddit.com'
        ]
    
    def calculate_risk_score(self, indicators: Dict[str, bool]) -> int:
        """
        Calculate risk score based on detected indicators
        
        Args:
            indicators: Dictionary of indicator names and their presence (True/False)
            
        Returns:
            Risk score from 0-100
        """
        score = 0
        for indicator, present in indicators.items():
            if present and indicator in self.weights:
                score += self.weights[indicator]
        
        # Cap at 100
        return min(score, 100)
    
    def classify_risk(self, score: int) -> str:
        """
        Classify risk level based on score
        
        Args:
            score: Risk score (0-100)
            
        Returns:
            Risk classification: SAFE, SUSPICIOUS, or PHISHING
        """
        if score < 30:
            return "SAFE"
        elif score < 60:
            return "SUSPICIOUS"
        else:
            return "PHISHING"
    
    def detect_urgent_language(self, text: str) -> bool:
        """
        Detect urgent/pressure language
        
        Args:
            text: Email text to analyze
            
        Returns:
            True if urgent language detected
        """
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.urgent_keywords)
    
    def detect_credential_request(self, text: str) -> bool:
        """
        Detect requests for credentials or personal information
        
        Args:
            text: Email text to analyze
            
        Returns:
            True if credential request detected
        """
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.credential_keywords)
    
    def detect_threat_language(self, text: str) -> bool:
        """
        Detect threatening language
        
        Args:
            text: Email text to analyze
            
        Returns:
            True if threat language detected
        """
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.threat_keywords)
    
    def detect_too_good_to_be_true(self, text: str) -> bool:
        """
        Detect 'too good to be true' offers
        
        Args:
            text: Email text to analyze
            
        Returns:
            True if suspicious offers detected
        """
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.too_good_keywords)
    
    def detect_generic_greeting(self, text: str) -> bool:
        """
        Detect generic greetings (lack of personalization)
        
        Args:
            text: Email text to analyze
            
        Returns:
            True if generic greeting detected
        """
        text_lower = text.lower()
        return any(greeting in text_lower for greeting in self.generic_greetings)
    
    def detect_poor_grammar(self, text: str) -> bool:
        """
        Detect poor grammar and spelling (simplified check)
        
        Args:
            text: Email text to analyze
            
        Returns:
            True if poor grammar indicators detected
        """
        # Check for multiple exclamation marks
        if '!!!' in text or '???' in text:
            return True
        
        # Check for excessive capitalization
        words = text.split()
        if len(words) > 10:
            caps_words = sum(1 for word in words if word.isupper() and len(word) > 2)
            if caps_words / len(words) > 0.3:
                return True
        
        return False
    
    def is_trusted_domain(self, domain: str) -> bool:
        """
        Check if domain is in trusted list
        
        Args:
            domain: Domain to check
            
        Returns:
            True if domain is trusted
        """
        if not domain:
            return False
        
        domain_lower = domain.lower()
        return any(trusted in domain_lower for trusted in self.trusted_domains)
    
    def analyze_text_patterns(self, text: str) -> Dict[str, bool]:
        """
        Analyze text for various phishing patterns
        
        Args:
            text: Email text to analyze
            
        Returns:
            Dictionary of detected patterns
        """
        return {
            'urgent_language': self.detect_urgent_language(text),
            'credential_request': self.detect_credential_request(text),
            'threat_language': self.detect_threat_language(text),
            'too_good_to_be_true': self.detect_too_good_to_be_true(text),
            'generic_greeting': self.detect_generic_greeting(text),
            'poor_grammar': self.detect_poor_grammar(text)
        }
