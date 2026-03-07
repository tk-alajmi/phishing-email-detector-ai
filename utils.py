"""
Utility functions for phishing email detection
"""

import re
from urllib.parse import urlparse
from typing import List, Set

def extract_urls(text: str) -> List[str]:
    """
    Extract all URLs from text
    
    Args:
        text: Input text to search for URLs
        
    Returns:
        List of URLs found in the text
    """
    # Regular expression to match URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, text)
    return urls

def extract_domains(urls: List[str]) -> List[str]:
    """
    Extract domains from a list of URLs
    
    Args:
        urls: List of URLs
        
    Returns:
        List of domains
    """
    domains = []
    for url in urls:
        try:
            parsed = urlparse(url)
            if parsed.netloc:
                domains.append(parsed.netloc.lower())
        except:
            continue
    return domains

def is_shortened_url(url: str) -> bool:
    """
    Check if URL is from a known URL shortening service
    
    Args:
        url: URL to check
        
    Returns:
        True if URL is shortened, False otherwise
    """
    shorteners = [
        'bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly',
        'is.gd', 'buff.ly', 'adf.ly', 'bit.do', 'short.link',
        'tiny.cc', 'cli.gs', 'pic.gd', 'DwarfURL.com', 'yfrog.com',
        'migre.me', 'ff.im', 'tiny.pl', 'url4.eu', 'tr.im',
        'twit.ac', 'su.pr', 'twurl.nl', 'snipurl.com', 'short.to',
        'BudURL.com', 'ping.fm', 'post.ly', 'Just.as', 'bkite.com',
        'snipr.com', 'fic.kr', 'loopt.us', 'doiop.com', 'twitthis.com',
        'htxt.it', 'AltURL.com', 'RedirX.com', 'DigBig.com', 'short.ie',
        'u.mavrev.com', 'kl.am', 'wp.me', 'rubyurl.com', 'om.ly',
        'to.ly', 'bit.do', 'lnkd.in', 'db.tt', 'qr.ae', 'adf.ly',
        'bitly.com', 'cur.lv', 'tinyurl.com', 'ow.ly', 'bit.ly',
        'ity.im', 'q.gs', 'is.gd', 'po.st', 'bc.vc', 'twitthis.com',
        'u.to', 'j.mp', 'buzurl.com', 'cutt.us', 'u.bb', 'yourls.org',
        'x.co', 'prettylinkpro.com', 'scrnch.me', 'filoops.info',
        'vzturl.com', 'qr.net', '1url.com', 'tweez.me', 'v.gd',
        'tr.im', 'link.zip.net'
    ]
    
    try:
        domain = urlparse(url).netloc.lower()
        return any(shortener in domain for shortener in shorteners)
    except:
        return False

def extract_email_addresses(text: str) -> List[str]:
    """
    Extract email addresses from text
    
    Args:
        text: Input text to search for email addresses
        
    Returns:
        List of email addresses found
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

def has_ip_address_url(url: str) -> bool:
    """
    Check if URL uses IP address instead of domain name
    
    Args:
        url: URL to check
        
    Returns:
        True if URL contains IP address, False otherwise
    """
    try:
        domain = urlparse(url).netloc
        # Check for IPv4 pattern
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        return bool(re.search(ip_pattern, domain))
    except:
        return False

def count_special_chars(text: str) -> int:
    """
    Count special characters in text
    
    Args:
        text: Input text
        
    Returns:
        Count of special characters
    """
    special_chars = set('!@#$%^&*()_+-=[]{}|;:,.<>?')
    return sum(1 for char in text if char in special_chars)

def has_suspicious_tld(url: str) -> bool:
    """
    Check if URL has a suspicious top-level domain
    
    Args:
        url: URL to check
        
    Returns:
        True if TLD is suspicious, False otherwise
    """
    suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.work', '.click']
    
    try:
        domain = urlparse(url).netloc.lower()
        return any(domain.endswith(tld) for tld in suspicious_tlds)
    except:
        return False

def normalize_text(text: str) -> str:
    """
    Normalize text by removing extra whitespace and converting to lowercase
    
    Args:
        text: Input text
        
    Returns:
        Normalized text
    """
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text.lower()
