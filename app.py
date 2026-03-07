"""
Phishing Email Detector AI - Main CLI Application
Cybersecurity tool for detecting phishing emails using AI-powered analysis
"""

import sys
import os
from detector import PhishingDetector
from colorama import init, Fore, Style

# Initialize colorama for Windows color support
init(autoreset=True)

def print_banner():
    """
    Print application banner
    """
    banner = f"""
{Fore.CYAN}{'='*70}
{Fore.CYAN}  ____  _     _     _     _               ____       _            _             
{Fore.CYAN} |  _ \| |__ (_)___| |__ (_)_ __   __ _  |  _ \  ___| |_ ___  ___| |_ ___  _ __ 
{Fore.CYAN} | |_) | '_ \| / __| '_ \| | '_ \ / _` | | | | |/ _ \ __/ _ \/ __| __/ _ \| '__|
{Fore.CYAN} |  __/| | | | \__ \ | | | | | | | (_| | | |_| |  __/ ||  __/ (__| || (_) | |   
{Fore.CYAN} |_|   |_| |_|_|___/_| |_|_|_| |_|\__, | |____/ \___|\__\___|\___|\__\___/|_|   
{Fore.CYAN}                                   |___/                                         
{Fore.CYAN}{'='*70}
{Fore.YELLOW}           AI-Powered Phishing Email Detection & Analysis Tool
{Fore.YELLOW}                    Cybersecurity Portfolio Project
{Fore.CYAN}{'='*70}
    """
    print(banner)

def print_menu():
    """
    Print main menu options
    """
    print(f"\n{Fore.GREEN}[MENU OPTIONS]")
    print(f"{Fore.WHITE}1. Paste email text directly")
    print(f"{Fore.WHITE}2. Load email from file")
    print(f"{Fore.WHITE}3. Analyze example phishing email")
    print(f"{Fore.WHITE}4. Analyze example safe email")
    print(f"{Fore.WHITE}5. Exit")
    print()

def get_email_from_input():
    """
    Get email text from user input
    
    Returns:
        Email text string
    """
    print(f"\n{Fore.YELLOW}Paste your email text below.")
    print(f"{Fore.YELLOW}When finished, type 'END' on a new line and press Enter:\n")
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        except EOFError:
            break
    
    return '\n'.join(lines)

def get_email_from_file(filepath):
    """
    Load email text from file
    
    Args:
        filepath: Path to email file
        
    Returns:
        Email text string or None if error
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File not found: {filepath}")
        return None
    except Exception as e:
        print(f"{Fore.RED}Error reading file: {e}")
        return None

def display_results(result):
    """
    Display analysis results with color coding
    
    Args:
        result: Analysis result dictionary
    """
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}EMAIL ANALYSIS RESULT")
    print(f"{Fore.CYAN}{'='*70}\n")
    
    # Risk score with color coding
    score = result['risk_score']
    classification = result['classification']
    
    if classification == "SAFE":
        color = Fore.GREEN
    elif classification == "SUSPICIOUS":
        color = Fore.YELLOW
    else:  # PHISHING
        color = Fore.RED
    
    print(f"{Fore.WHITE}Risk Score: {color}{score}/100{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Classification: {color}{classification}{Style.RESET_ALL}\n")
    
    # Email details
    print(f"{Fore.CYAN}Email Details:")
    print(f"{Fore.CYAN}{'-'*70}")
    print(f"{Fore.WHITE}Subject: {result['subject']}")
    print(f"{Fore.WHITE}Sender: {result['sender']}")
    print(f"{Fore.WHITE}URLs Found: {result['url_count']}\n")
    
    # Detected indicators
    if result['detected_indicators']:
        print(f"{Fore.RED}Detected Phishing Indicators:")
        print(f"{Fore.RED}{'-'*70}")
        for indicator in result['detected_indicators']:
            print(f"{Fore.YELLOW}  • {indicator}")
    else:
        print(f"{Fore.GREEN}No phishing indicators detected.")
    
    print(f"\n{Fore.CYAN}{'='*70}\n")
    
    # Recommendation
    if classification == "SAFE":
        print(f"{Fore.GREEN}✓ RECOMMENDATION: This email appears to be safe.")
    elif classification == "SUSPICIOUS":
        print(f"{Fore.YELLOW}⚠ RECOMMENDATION: Exercise caution. Verify sender before taking action.")
    else:
        print(f"{Fore.RED}✗ RECOMMENDATION: This email is likely a phishing attempt. Do NOT click links or provide information.")
    
    print(f"{Fore.CYAN}{'='*70}\n")

def main():
    """
    Main application loop
    """
    print_banner()
    
    detector = PhishingDetector()
    
    while True:
        print_menu()
        
        try:
            choice = input(f"{Fore.GREEN}Enter your choice (1-5): {Fore.WHITE}").strip()
            
            if choice == '1':
                # Paste email directly
                email_text = get_email_from_input()
                if email_text.strip():
                    print(f"\n{Fore.CYAN}Analyzing email...{Style.RESET_ALL}")
                    result = detector.analyze_email(email_text)
                    display_results(result)
                else:
                    print(f"{Fore.RED}No email text provided.")
            
            elif choice == '2':
                # Load from file
                filepath = input(f"{Fore.YELLOW}Enter file path: {Fore.WHITE}").strip()
                email_text = get_email_from_file(filepath)
                if email_text:
                    print(f"\n{Fore.CYAN}Analyzing email...{Style.RESET_ALL}")
                    result = detector.analyze_email(email_text)
                    display_results(result)
            
            elif choice == '3':
                # Analyze example phishing email
                example_path = os.path.join('examples', 'phishing_email_sample.txt')
                email_text = get_email_from_file(example_path)
                if email_text:
                    print(f"\n{Fore.CYAN}Analyzing example phishing email...{Style.RESET_ALL}")
                    result = detector.analyze_email(email_text)
                    display_results(result)
            
            elif choice == '4':
                # Analyze example safe email
                example_path = os.path.join('examples', 'safe_email_sample.txt')
                email_text = get_email_from_file(example_path)
                if email_text:
                    print(f"\n{Fore.CYAN}Analyzing example safe email...{Style.RESET_ALL}")
                    result = detector.analyze_email(email_text)
                    display_results(result)
            
            elif choice == '5':
                # Exit
                print(f"\n{Fore.CYAN}Thank you for using Phishing Email Detector AI!")
                print(f"{Fore.YELLOW}Stay safe online! 🔒\n")
                sys.exit(0)
            
            else:
                print(f"{Fore.RED}Invalid choice. Please enter 1-5.")
        
        except KeyboardInterrupt:
            print(f"\n\n{Fore.CYAN}Thank you for using Phishing Email Detector AI!")
            print(f"{Fore.YELLOW}Stay safe online! 🔒\n")
            sys.exit(0)
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}")
            print(f"{Fore.YELLOW}Please try again.\n")

if __name__ == "__main__":
    main()
