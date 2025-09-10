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

---

# Create API Contract Documentation

After generating the Pydantic models, create an `API_CONTRACT.md` file that serves as a human-readable single source of truth for all API endpoints. This document should be accessible to frontend developers, AI agents, QA engineers, and technical writers.

## API_CONTRACT.md Structure

1. **Endpoint Overview**
   - HTTP method and path
   - Brief description of purpose
   - Authentication requirements

2. **Request Specifications**
   - Path parameters with types and descriptions
   - Query parameters with types, validation rules, and examples
   - Request body schema with all fields, types, validation rules, and examples
   - Required vs optional fields clearly marked

3. **Response Specifications**
   - Success response schema with all fields, types, and descriptions
   - HTTP status codes and their meanings
   - Error response formats and common error codes
   - Example responses for success and error cases

4. **Data Type Definitions**
   - Custom types referenced across endpoints
   - Enumeration values and their meanings
   - Date/time format specifications
   - UUID formats and validation rules

5. **Validation Rules**
   - Field-level constraints (min/max length, value ranges, regex patterns)
   - Business logic validation rules
   - Cross-field validation requirements

6. **Changelog**
   - Version history of API changes
   - Breaking changes with migration guides
   - Deprecation notices

## Example Entry Format

```markdown
## POST /api/v1/users

Creates a new user account.

**Authentication:** Required (Bearer token)

### Request
**Headers:**
- `Authorization: Bearer <token>`

**Body:**
```json
{
  "email": "user@example.com",      // string, required, valid email format
  "username": "johndoe",             // string, required, 3-20 chars, alphanumeric + underscore
  "password": "SecurePass123!",      // string, required, min 8 chars, must contain uppercase, lowercase, number, special char
  "profile": {
    "first_name": "John",           // string, optional, max 50 chars
    "last_name": "Doe",              // string, optional, max 50 chars
    "birth_date": "1990-01-01"      // string, optional, ISO 8601 date format
  }
}
```

### Response
**Success (201 Created):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",  // UUID
  "email": "user@example.com",
  "username": "johndoe",
  "profile": {
    "first_name": "John",
    "last_name": "Doe",
    "birth_date": "1990-01-01"
  },
  "created_at": "2023-10-15T14:30:00Z",         // ISO 8601 datetime
  "updated_at": "2023-10-15T14:30:00Z"
}
```

**Error (400 Bad Request):**
```json
{
  "error": "VALIDATION_ERROR",
  "message": "Invalid input data",
  "details": {
    "email": "Invalid email format",
    "password": "Password must contain at least one uppercase letter"
  }
}
```
```

## Generation Instructions

1. After creating Pydantic models, extract all endpoint information from:
   - The generated Pydantic schemas
   - Original function signatures and docstrings
   - Route definitions and their configurations

2. For each endpoint, document:
   - All possible request parameters with their validation rules
   - Complete response schemas including nested objects
   - Clear examples that demonstrate valid usage
   - Error scenarios and their response formats

3. **Print the exact Pydantic model declarations** in the API contract:
   - Include all imports at the top of each model section
   - Show the complete class definition with all Field() descriptions
   - Display all constraints (min_length, max_length, gt, lt, regex, etc.)
   - Include default values and optional fields
   - Show both Request and Response models exactly as declared

4. Maintain consistency:
   - Use the same field names as defined in Pydantic models
   - Keep descriptions synchronized between code and documentation
   - Update the contract whenever schemas change

5. Make it actionable:
   - Include copy-paste ready examples
   - Provide clear validation rules that can be implemented
   - Document edge cases and special handling

## Model Documentation Format

For each endpoint, include the exact Pydantic model declarations:

```markdown
### Models

**Request Model:**
```python
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional
from uuid import UUID

class CreateUserRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    email: str = Field(
        description="User's email address",
        pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    )
    username: str = Field(
        min_length=3,
        max_length=20,
        description="Unique username for the user"
    )
    password: str = Field(
        min_length=8,
        description="User's password (must contain uppercase, lowercase, number, special char)"
    )
    profile: Optional[dict] = Field(
        None,
        description="Optional user profile information"
    )
```

**Response Model:**
```python
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class UserResponse(BaseModel):
    id: UUID = Field(description="Unique user identifier")
    email: str = Field(description="User's email address")
    username: str = Field(description="User's username")
    profile: dict = Field(description="User profile data")
    created_at: datetime = Field(description="Account creation timestamp")
    updated_at: datetime = Field(description="Last update timestamp")
```
```
