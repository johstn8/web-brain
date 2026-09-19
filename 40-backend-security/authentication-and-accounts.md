---
type: canonical
status: canonical
updated: 2026-08-03
review_by: 2027-02-03
impacts:
  - user-data
  - email
  - audit-log
  - billing
  - qa
---

# Authentication and Accounts

## Modell

- Interne zufällige `user_id` ist Identität. E-Mail und Provider-IDs sind verifizierte Identifikatoren, nicht Primärschlüssel.
- Ein Nutzerkonto kann mehrere Login-Methoden besitzen: Passwort, OAuth/OIDC, Passkey.
- E-Mail bei Signup verifizieren; Enumeration durch gleichartige öffentliche Antworten minimieren.

## Account Linking

Ziel: Eine verifizierte E-Mail führt zu einem Konto, unabhängig davon, ob zuerst Passwort oder Google genutzt wurde.

1. Provider liefert E-Mail plus verifizierten Status.
2. Nur verifizierte Provider-E-Mail automatisch matchen.
3. Existiert Konto mit verifizierter gleicher E-Mail, Provider-Identität sicher daran binden und Nutzer informieren.
4. Ist eine Seite unverified oder Provider-Vertrauen unklar, Besitz über bestehende Methode oder verifizierte E-Mail bestätigen. Nicht blind mergen.
5. Signup mit vorhandener E-Mail erstellt kein Duplikat; sicher in Sign-in/Recovery führen, ohne öffentliche Enumeration.
6. Passwortlogin darf für ein per OAuth erstelltes Konto erst nach bewusstem Passwort-Setup über verifizierten Recovery-Flow möglich sein.
7. Unlink nur erlauben, wenn mindestens eine sichere Login-Methode bleibt.

Clerk beschreibt vergleichbares Linking auf Basis übereinstimmender verifizierter E-Mails und zusätzliche Verifikation bei unbestätigten Adressen.[^link]

## Authenticatoren

- Passkeys/WebAuthn bevorzugen, besonders für privilegierte Rollen; phishing-resistent durch Bindung an den Verifier-Namen.[^nist]
- MFA mindestens optional, für Admins und sensible Aktionen verpflichtend; Recovery Codes sicher bereitstellen.
- OTP ist besser als nur Passwort, aber nicht phishing-resistent.
- Passwort: lange Passphrasen erlauben, Paste und Password Manager erlauben, bekannte kompromittierte Werte blocken, keine willkürlichen Kompositionsregeln.

## Abuse-Schutz

- Signup/Login/Reset rate-limitieren, verdächtige Bots adaptiv challengen, Alerts und Geräte-/Sessionverwaltung.
- Disposable-E-Mail-Blockliste kann Spam reduzieren, ist aber fehleranfällig und kein Sicherheitsbeweis. Ablehnung erklären, Supportweg und Telemetrie vorsehen. Clerk kombiniert Blocklisten, Subaddress-Regeln, Bot-Schutz und Enumeration-Schutz.[^restrictions][^bots][^enum]

## Session

- Rotieren nach Login und Privilegwechsel; kurze Idle- und absolute Laufzeit nach Risiko.
- HttpOnly/Secure/SameSite Cookies, CSRF-Schutz, serverseitige Revocation.
- Aktive Sessions sichtbar und einzeln widerrufbar.
- Re-Authentifizierung vor E-Mail-, Passwort-, MFA-, Zahlungs- oder Löschänderung.

[^link]: [Clerk: OAuth account linking](https://clerk.com/docs/guides/configure/auth-strategies/social-connections/account-linking)
[^nist]: [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html)
[^restrictions]: [Clerk: Restrictions and disposable emails](https://clerk.com/docs/guides/secure/restricting-access)
[^bots]: [Clerk: Bot protection](https://clerk.com/docs/guides/secure/bot-protection)
[^enum]: [Clerk: User enumeration protection](https://clerk.com/docs/guides/secure/user-enumeration-protection)

