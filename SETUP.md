# Setup

Die Workflows sind Exporte einer laufenden Instanz und nicht als Template gedacht, sondern als Einblick in den Aufbau. Wer sie trotzdem importieren will:

1. In n8n **Workflows → Add workflow → … → Import from File** und die JSON-Datei wählen. Die Reihenfolge ist egal, verknüpft wird erst in Schritt 3.
2. Für jeden Node mit `CREDENTIAL_ID` eine eigene Credential anlegen und zuweisen: Google Sheets, Drive, Docs und Gmail (OAuth2), Anthropic, Tavily, CloudConvert, Recraft (Header Auth), n8n API.
3. Platzhalter ersetzen:

| Platzhalter | Bedeutung |
|---|---|
| `WF02_ID`, `WF03_ID`, `WF09_ID` | ID des jeweils importierten Folge-Workflows |
| `ERROR_WORKFLOW_ID` | ID von `system/fehler-alarm.json`, in den Workflow-Settings |
| `TAVILY_SUB_ID`, `ETSY_TOKEN_SUB_ID` | Sub-Workflows für Websuche und Etsy-OAuth (Etsy-OAuth nicht enthalten) |
| `GOOGLE_FILE_ID` | eigene Sheets, Ordner und DOCX-Master-Vorlagen |
| `you@example.com` | Empfänger für Freigabe- und Fehlermails |
| `your-n8n.example.com` | eigene n8n-URL |
| `CHANGE_ME_RETRY_TOKEN` | frei wählbarer Token für den Retry-Webhook |

4. Gotenberg muss im selben Docker-Netz unter `http://gotenberg:3000` erreichbar sein.

Benötigte Sheets: `Buch-Master` (eine Zeile pro Buch, Spalten siehe Sheets-Nodes in WF01) und `Blacklist` (bisherige Nischen).
