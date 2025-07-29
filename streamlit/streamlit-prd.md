# Technical Requirements Documentation

## Input Components

### Available Input Types

The following input components are available for user interaction:

- **HTML**: `<textarea>` element
- **Streamlit**: `st.input()` for single-line input
- **Streamlit**: `st.text_area()` for multi-line input

### Implementation Example

```python
user_question = st.text_area(
    "Ask your question:",
    height=150,  # Height parameter determines the size of the chatbox
    placeholder="Type your message here...",
    max_chars=1000
)
```

#### Parameters
- **Label**: "Ask your question:"
- **Height**: 150px
- **Placeholder**: "Type your message here..."
- **Character Limit**: 1000 characters

## Theme Specifications

### Shadcn Color Palette

| Component | Color Code | Usage |
|-----------|------------|-------|
| Background | `#0A0A0A` | Main application background |
| Chart Text | `#E5E5E5` | Text color for charts and data visualization |
| Section Text | `#828282` | Secondary text color for sections |
| Chat Box Background | `#212121` | Background color for chat containers |
| Border | `#434343` | Border color for UI elements |
| Gradient Start | `#3C3C3C` | Starting color for gradient effects |
| Gradient End | `#807F80` | Ending color for gradient effects |
| Hover Background | `#252525` | Background color on hover states |

### Color Usage Guidelines

- Use **Background** (`#0A0A0A`) for the main application backdrop
- Apply **Chart Text** (`#E5E5E5`) for primary readable content
- Utilize **Section Text** (`#828282`) for secondary information and labels
- Implement **Chat Box Background** (`#212121`) for conversational interfaces
- Apply **Border** (`#434343`) to define component boundaries
- Use the **Gradient** (`#3C3C3C` to `#807F80`) for visual depth and modern aesthetics
- Apply **Hover Background** (`#252525`) for interactive element feedback
