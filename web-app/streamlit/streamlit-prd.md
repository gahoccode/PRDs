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

