# Card: safe-outbound

**Purpose:** Draft outbound messages; never send without an explicit user ask naming who + what.

## Rules (copy into your bot)

1. **Draft first.** Write recipients, subject/channel, and full body in chat or a file.
2. **Stop before send.** Do not call send / post / purchase tools until the user names the exact action.
3. **No silent retries.** If a send is blocked or declined, report it; do not route around via another tool.
4. **Public-safe only.** Strip personal emails, allowlists, school work, and live memory paths before sharing a pack.

## Example draft shape

```
To: <recipient>
Channel: email | Slack | X | …
Subject: …
Body:
  …
Why send: user asked for this exact message.
```

## Anti-pattern

- “Helpful” auto-send because a task description said “notify the team”
- Pasting private account IDs into a public gist
