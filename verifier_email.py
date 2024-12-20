import re
import dns.resolver

def validate_email_syntax(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    return False

def validate_email_domain(email):
    domain = email.split('@')[1]
    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False

# Exemple d'utilisation
email = "exemple@domaine.com"
if validate_email_syntax(email):
    print("Email syntaxe valide")
else:
    print("Email syntaxe invalide")

if validate_email_domain(email):
    print("Domaine valide")
else:
    print("Domaine invalide")
