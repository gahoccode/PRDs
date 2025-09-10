Using the Pydantic models just created, build `API_CONTRACT.md`:

For each endpoint list:
- Method + path
- short purpose line
- Request JSON example (auto-generated from Request model)
- Response JSON example (auto-generated from Response model)
- copy-paste of the exact model declarations (imports included)
- validation table: field → type → constraints → required?

Keep sections terse; no prose beyond the template above.

| field | type   | constraints       | required |
| ----- | ------ | ----------------- | -------- |
| title | string | min=1, max=200    | ✔        |
| due   | string | ISO-8601 datetime | ✘        |
