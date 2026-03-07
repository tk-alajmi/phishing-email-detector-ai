"""
Main phishing detection engine
"""

from typing import Dict, List, Tuple
from email_parser import EmailParser
from model.phishing_model import PhishingModel
from utils import (
    extract_domains, is_shortened_url, has_ip_address_url,
    has_suspicious_tld, extract_urls
)

class PhishingDetector:
    """
    Main phishing detection class that coordinates analysis
    """
    
    def __init__(self):
        """
        Initialize the phishing detector
        """
        self.model = PhishingModel()
    
    def analyze_email(self, email_text: str) -> Dict:
        """
        Perform complete phishing analysis on email
        
        Args:
            email_text: Raw email text
            
        Returns:
            Dictionary containing analysis results
        """
        # Parse email
        parser = EmailParser(email_text)
        
        # Get email components
        subject = parser.get_subject()
        body = parser.get_body_text()
        urls = parser.get_all_links()
        sender_domain = parser.get_sender_domain()
        
        # Combine subject and body for text analysis
        full_text = f"{subject} {body}"
        
        # Detect indicators
        indicators = self._detect_all_indicators(
            full_text, urls, sender_domain, parser
        )
        
        # Calculate risk score
        risk_score = self.model.calculate_risk_score(indicators)
        
        # Classify risk
        classification = self.model.classify_risk(risk_score)
        
        # Get detected indicator names
        detected_indicators = [
            self._format_indicator_name(name) 
            for name, present in indicators.items() 
            if present
        ]
        
        return {
            'risk_score': risk_score,
            'classification': classification,
            'indicators': indicators,
            'detected_indicators': detected_indicators,
            'subject': subject,
            'sender': parser.parsed_data['from'],
            'url_count': len(urls)
        }
    
    def _detect_all_indicators(self, text: str, urls: List[str], 
                               sender_domain: str, parser: EmailParser) -> Dict[str, bool]:
        """
        Detect all phishing indicators
        
        Args:
            text: Email text (subject + body)
            urls: List of URLs in email
            sender_domain: Sender's domain
            parser: EmailParser instance
            
        Returns:
            Dictionary of indicators and their presence
        """
        indicators = {}
        
        # Text-based indicators
        text_patterns = self.model.analyze_text_patterns(text)
        indicators.update(text_patterns)
        
        # URL-based indicators
        indicators['suspicious_url'] = self._has_suspicious_urls(urls)
        indicators['shortened_url'] = self._has_shortened_urls(urls)
        indicators['ip_address_url'] = self._has_ip_urls(urls)
        indicators['suspicious_tld'] = self._has_suspicious_tld(urls)
        
        # Domain-based indicators
        indicators['domain_mismatch'] = self._check_domain_mismatch(
            sender_domain, urls
        )
        indicators['unusual_sender'] = self._check_unusual_sender(sender_domain)
        indicators['spoofing_attempt'] = self._check_spoofing(
            parser.parsed_data['from'], sender_domain
        )
        
        # Attachment indicators
        indicators['attachment_mention'] = parser.has_attachments_mentioned()
        
        return indicators
    
    def _has_suspicious_urls(self, urls: List[str]) -> bool:
        """
        Check if email contains suspicious URLs
        
        Args:
            urls: List of URLs
            
        Returns:
            True if suspicious URLs found
        """
        if not urls:
            return False
        
        # Check for multiple redirects or suspicious patterns
        suspicious_patterns = [
            'login', 'verify', 'account', 'secure', 'update',
            'confirm', 'banking', 'paypal', 'amazon', 'microsoft'
        ]
        
        for url in urls:
            url_lower = url.lower()
            # Check if URL contains suspicious keywords
            if any(pattern in url_lower for pattern in suspicious_patterns):
                # Check if it's not from a trusted domain
                domains = extract_domains([url])
                if domains and not self.model.is_trusted_domain(domains[0]):
                    return True
        
        return False
    
    def _has_shortened_urls(self, urls: List[str]) -> bool:
        """
        Check if email contains shortened URLs
        
        Args:
            urls: List of URLs
            
        Returns:
            True if shortened URLs found
        """
        return any(is_shortened_url(url) for url in urls)
    
    def _has_ip_urls(self, urls: List[str]) -> bool:
        """
        Check if email contains URLs with IP addresses
        
        Args:
            urls: List of URLs
            
        Returns:
            True if IP-based URLs found
        """
        return any(has_ip_address_url(url) for url in urls)
    
    def _has_suspicious_tld(self, urls: List[str]) -> bool:
        """
        Check if email contains URLs with suspicious TLDs
        
        Args:
            urls: List of URLs
            
        Returns:
            True if suspicious TLDs found
        """
        return any(has_suspicious_tld(url) for url in urls)
    
    def _check_domain_mismatch(self, sender_domain: str, urls: List[str]) -> bool:
        """
        Check if sender domain doesn't match URL domains
        
        Args:
            sender_domain: Sender's email domain
            urls: List of URLs in email
            
        Returns:
            True if domain mismatch detected
        """
        if not sender_domain or not urls:
            return False
        
        url_domains = extract_domains(urls)
        
        # Check if any URL domain significantly differs from sender domain
        for url_domain in url_domains:
            # If sender claims to be from a major company but URL is different
            major_companies = ['paypal', 'amazon', 'microsoft', 'apple', 'google', 'facebook']
            
            for company in major_companies:
                if company in sender_domain.lower() and company not in url_domain.lower():
                    return True
                if company in url_domain.lower() and company not in sender_domain.lower():
                    return True
        
        return False
    
    def _check_unusual_sender(self, sender_domain: str) -> bool:
        """
        Check if sender domain is unusual or suspicious
        
        Args:
            sender_domain: Sender's email domain
            
        Returns:
            True if sender is unusual
        """
        if not sender_domain:
            return True
        
        # Check for suspicious patterns in domain
        suspicious_patterns = [
            'secure', 'verify', 'account', 'support-',
            'service-', 'update-', 'confirm-'
        ]
        
        domain_lower = sender_domain.lower()
        return any(pattern in domain_lower for pattern in suspicious_patterns)
    
    def _check_spoofing(self, sender_full: str, sender_domain: str) -> bool:
        """
        Check for email spoofing attempts
        
        Args:
            sender_full: Full sender string
            sender_domain: Sender's domain
            
        Returns:
            True if spoofing detected
        """
        if not sender_full or not sender_domain:
            return False
        
        # Check if display name contains different domain
        sender_lower = sender_full.lower()
        trusted_names = ['paypal', 'amazon', 'microsoft', 'apple', 'google', 'bank']
        
        for name in trusted_names:
            if name in sender_lower and name not in sender_domain.lower():
                return True
        
        return False
    
    def _format_indicator_name(self, indicator: str) -> str:
        """
        Format indicator name for display
        
        Args:
            indicator: Indicator key name
            
        Returns:
            Formatted indicator name
        """
        # Convert snake_case to Title Case
        words = indicator.split('_')
        return ' '.join(word.capitalize() for word in words)
    
    def get_detailed_report(self, analysis_result: Dict) -> str:
        """
        Generate detailed text report from analysis
        
        Args:
            analysis_result: Result from analyze_email()
            
        Returns:
            Formatted report string
        """
        report = []
        report.append("=" * 60)
        report.append("PHISHING EMAIL ANALYSIS REPORT")
        report.append("=" * 60)
        report.append("")
        
        # Risk assessment
        report.append(f"Risk Score: {analysis_result['risk_score']}/100")
        report.append(f"Classification: {analysis_result['classification']}")
        report.append("")
        
        # Email details
        report.append("Email Details:")
        report.append("-" * 60)
        report.append(f"Subject: {analysis_result['subject']}")
        report.append(f"Sender: {analysis_result['sender']}")
        report.append(f"URLs Found: {analysis_result['url_count']}")
        report.append("")
        
        # Detected indicators
        if analysis_result['detected_indicators']:
            report.append("Detected Phishing Indicators:")
            report.append("-" * 60)
            for indicator in analysis_result['detected_indicators']:
                report.append(f"  • {indicator}")
        else:
            report.append("No phishing indicators detected.")
        
        report.append("")
        report.append("=" * 60)
        
        return "\n".join(report)
