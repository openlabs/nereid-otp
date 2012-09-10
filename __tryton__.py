{
    'name': 'Nereid OTP',
    'version': '2.4.0.1dev',
    'author': 'Openlabs Technologies & Consulting (P) Ltd.',
    'email': 'info@openlabs.co.in',
    'website': 'http://www.openlabs.co.in/',
    'description': '''Extends nereid users to use OTPs.

Batteries Included:

  * HOTP Device support
  * TOTP Device support
''',
    'depends': [
        'nereid',
    ],
    'xml': [
       'user.xml',
       'urls.xml',
    ],
    'translation': [
    ],
}
