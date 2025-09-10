# Infer & write the Pydantic models

1. READ the provided backend source file(s) that currently:
   - contain plain dataclasses, TypedDicts, or no models at all
   - use type-hinted function parameters / return values
   - may have doc-strings or inline comments describing fields

2. EXTRACT for every endpoint handler:
   - the incoming data shape (body, query, path params)
   - the outgoing data shape (whatever is returned or JSONified)
   - any validation clues in docstrings, comments, or default values (e.g., "must be > 0", "ISO date", "uuid4")

3. CREATE one self-contained Python snippet that:
   - declares new Pydantic BaseModel classes named `<Resource>Request` and `<Resource>Response`
   - uses the exact field names you discovered (snake_case)
   - maps the extracted type hints to Pydantic types (str, int, datetime, UUID, Optional[…], list[…])
   - adds Field(…) with:
     * description copied from docstring
     * constraints you inferred (gt, lt, regex, min_length, max_length, default, …)
   - sets `model_config = ConfigDict(extra="forbid")` unless the doc explicitly allows extra keys
   - keeps the file import-safe (include necessary imports: `from pydantic import BaseModel, Field, ConfigDict, …`)

4. OUTPUT FORMAT:
   ```python
   # file: app/schemas/inferred.py
   from pydantic import BaseModel, Field, ConfigDict
   from datetime import datetime
   from uuid import UUID
   from typing import Optional

   class TodoRequest(BaseModel):
       model_config = ConfigDict(extra="forbid")
       title: str = Field(min_length=1, max_length=200, description="Short title of the task")
       due: Optional[datetime] = Field(None, description="Due date in ISO-8601")
   ```

5. RULES:
   - Do not change original function names or business logic.
   - Do not invent fields not mentioned in hints/docstrings.
   - If an endpoint returns different shapes on success vs. error, create only the **success** response model; leave error handling to HTTPException.
   - Emit **one** consolidated code block; no explanatory text outside the block unless it is a short `# comment` inside the code.

Generate the schema snippet now.
