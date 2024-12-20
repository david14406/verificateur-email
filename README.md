# Vérificateur d'email

Ce projet permet de vérifier la validité d'une adresse email, y compris sa syntaxe et le domaine.

## Installation

1. Clonez ce repository.
2. Installez les dépendances nécessaires comme `dnspython` pour la vérification des domaines.

## Exemple d'utilisation

```python
from verifier_email import validate_email_syntax, validate_email_domain

email = "test@example.com"

if validate_email_syntax(email):
    print("Syntaxe valide")
else:
    print("Syntaxe invalide")

if validate_email_domain(email):
    print("Domaine valide")
else:
    print("Domaine invalide")
