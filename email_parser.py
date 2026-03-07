"""
Email parsing functionality for extracting email components
"""

import re
from typing import Dict, List, Optional
from utils import extract_urls, extract_email_addresses

class EmailParser:
    """
    Parser for extracting components from email text
    """
    
    def __init__(self, email_text: str):
        """
        Initialize email parser
        
        Args:
            email_text: Raw email text
        """
        self.raw_text = email_text
        self.parsed_data = self._parse_email()
    
    def _parse_email(self) -> Dict:
        """
        Parse email into components
        
        Returns:
            Dictionary containing parsed email components
        """
        data = {
            'subject': self._extract_subject(),
            'from': self._extract_from(),
            'to': self._extract_to(),
            'body': self._extract_body(),
            'urls': extract_urls(self.raw_text),
            'email_addresses': extract_email_addresses(self.raw_text),
            'headers': self._extract_headers()
        }
        return data
    
    def _extract_subject(self) -> str:
        """
        Extract subject line from email
        
        Returns:
            Subject line or empty string
        """
        subject_match = re.search(r'Subject:\s*(.+?)(?:\n|$)', self.raw_text, re.IGNORECASE)
        if subject_match:
            return subject_match.group(1).strip()
        return ""
    
    def _extract_from(self) -> str:
        """
        Extract sender from email
        
        Returns:
            Sender email or empty string
        """
        from_match = re.search(r'From:\s*(.+?)(?:\n|$)', self.raw_text, re.IGNORECASE)
        if from_match:
            return from_match.group(1).strip()
        return ""
    
    def _extract_to(self) -> str:
        """
        Extract recipient from email
        
        Returns:
            Recipient email or empty string
        """
        to_match = re.search(r'To:\s*(.+?)(?:\n|$)', self.raw_text, re.IGNORECASE)
        if to_match:
            return to_match.group(1).strip()
        return ""
    
    def _extract_body(self) -> str:
        """
        Extract email body
        
        Returns:
            Email body text
        """
        # Try to find body after headers
        body_match = re.search(r'\n\n(.+)', self.raw_text, re.DOTALL)
        if body_match:
            return body_match.group(1).strip()
        
        # If no clear separation, return the whole text
        return self.raw_text
    
    def _extract_headers(self) -> Dict[str, str]:
        """
        Extract email headers
        
        Returns:
            Dictionary of headers
        """
        headers = {}
        header_pattern = r'([A-Za-z-]+):\s*(.+?)(?=\n[A-Za-z-]+:|\n\n|$)'
        matches = re.finditer(header_pattern, self.raw_text, re.MULTILINE)
        
        for match in matches:
            key = match.group(1).strip()
            value = match.group(2).strip()
            headers[key] = value
        
        return headers
    
    def get_sender_domain(self) -> Optional[str]:
        """
        Extract domain from sender email
        
        Returns:
            Sender domain or None
        """
        sender = self.parsed_data['from']
        email_match = re.search(r'@([\w.-]+)', sender)
        if email_match:
            return email_match.group(1).lower()
        return None
    
    def get_display_name(self) -> Optional[str]:
        """
        Extract display name from sender
        
        Returns:
            Display name or None
        """
        sender = self.parsed_data['from']
        # Match pattern like "Display Name <email@domain.com>"
        name_match = re.search(r'^(.+?)\s*<', sender)
        if name_match:
            return name_match.group(1).strip()
        return None
    
    def get_all_links(self) -> List[str]:
        """
        Get all links from email
        
        Returns:
            List of URLs
        """
        return self.parsed_data['urls']
    
    def get_body_text(self) -> str:
        """
        Get email body text
        
        Returns:
            Body text
        """
        return self.parsed_data['body']
    
    def get_subject(self) -> str:
        """
        Get email subject
        
        Returns:
            Subject line
        """
        return self.parsed_data['subject']
    
    def has_attachments_mentioned(self) -> bool:
        """
        Check if email mentions attachments
        
        Returns:
            True if attachments are mentioned
        """
        attachment_keywords = [
            'attachment', 'attached', 'file', 'document', 'pdf',
            'invoice', 'receipt', 'download', 'click here', 'open'
        ]
        
        body_lower = self.parsed_data['body'].lower()
        subject_lower = self.parsed_data['subject'].lower()
        
        return any(keyword in body_lower or keyword in subject_lower 
                  for keyword in attachment_keywords)
