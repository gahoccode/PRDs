# Project Architecture

## Data Source Configuration

## Frontend
- Use Linux-friendly fonts that are supported natively

### HTML Templates (templates/)
- **index.html**: Main page with user input form
  - Rendered by the Flask route `/` (see app.py)
  - When users visit the site, the Flask backend serves index.html
  - Displays the form for the risk-free rate and simulation count
  - On form submission, data is sent to the backend for processing
  - Backend redirects to the results page (`/optimize` route)

### Results Display Options
- **Option 1 - results.html**: 
  - Display charts and metrics rendered after optimization is completed
  - Use base64 to serve images directly without saving them

- **Option 2 - outputs folder**: 
  - Serve exported static HTML saved in the output folder
  - Overwrite this file with each new export