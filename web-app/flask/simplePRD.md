# Vietnam Stock Portfolio Analyzer - Product Requirements Document

---

## Overview

Create a Python-based web application for analyzing Vietnam stock portfolio performance with comprehensive metrics and visualizations.

---

## Technical Specifications

### Framework & Libraries

| Component | Technology |
|-----------|------------|
| **Backend** | Flask |
| **Frontend** | HTML, CSS, Bootstrap |
| **Data Loader** | vnstock (Vietnam stock prices) |
| **Analysis** | QuantStats (performance metrics, tear sheets, plots) |

---

## Frontend Structure

### HTML Templates (`templates/` folder)

#### `index.html`
**Form Components:**
- **Stock Tickers Input**: Textarea or tag-based input for list of stock tickers
- **Date Range**: Start date and end date inputs
- **Initial Capital**: Numeric input field
- **Layout**: Bootstrap-powered responsive design
- **Submission**: POST request to `/analyze` endpoint

#### `results.html`
**Display Features:**
- Portfolio performance metrics (returns, volatility, Sharpe ratio, drawdowns)
- Embedded charts and tear sheet visuals from QuantStats
- Bootstrap layout for summary statistics and graphics

---

### Static Assets (`static/` folder)

#### `css/style.css`
- Custom styles for layout, charts, and forms
- Responsive design enhancements

#### `js/script.js`
- UI interactivity and user experience enhancements
- Input validation logic:
  - Ticker format validation
  - Date range logic verification

---

## Backend Structure (`app.py`)

### Route Definitions

#### `/` - Home Page
- **Purpose**: Renders `index.html`
- **Function**: Display the main input form

#### `/analyze` - Analysis Endpoint
**Processing Pipeline:**
1. **Data Reception**: Accepts user input from form submission
2. **Data Fetching**: Uses vnstock to retrieve historical data for selected tickers
3. **Portfolio Simulation**: Implements equal-weight portfolio or custom allocation logic
4. **Return Calculation**: Computes portfolio returns based on selected parameters
5. **Analysis Generation**: Utilizes QuantStats to generate:
   - Key performance statistics (Sharpe ratio, Sortino ratio, maximum drawdown)
   - HTML tear sheet (saved to `templates/qs_report.html`)
   - Performance plots (saved to `static/` folder)
6. **Response**: Returns `results.html` with embedded performance visuals and statistics

---

## Testing Framework (`tests/test_app.py`)

### Unit Tests
**Data Layer Tests:**
- vnstock data fetching edge cases
  - Invalid ticker handling
  - Market holiday gap management

**Business Logic Tests:**
- Portfolio return calculation accuracy
- QuantStats output parsing reliability
- File generation functionality

### Integration Tests
**Route Testing:**
- Homepage route (`/`) validation
- Analysis route (`/analyze`) functionality
- POST request behavior with valid and invalid inputs

**Frontend Tests** (Optional)
- Client-side validation logic verification
- Metrics and visualization rendering tests

---

## User Experience Features

### Design Elements
- **Bootstrap-based responsive layout** for optimal viewing across devices
- **Interactive charts** with optional download and zoom capabilities
- **Clear portfolio health indicators** and performance timeline display
- **Tear sheet download option** for detailed offline analysis

### Performance Metrics Display
- Real-time portfolio statistics
- Visual performance charts
- Risk assessment indicators
- Historical performance analysis

---

## Implementation Notes

### Data Flow
1. User inputs stock tickers, date range, and initial capital
2. Backend fetches historical data using vnstock
3. Portfolio analysis performed with QuantStats
4. Results displayed with embedded charts and metrics
5. Optional tear sheet generation for detailed reporting

### Error Handling
- Invalid ticker symbol validation
- Date range validation
- Market data availability checks
- Portfolio calculation error management

---

## Future Enhancements
- Real-time data updates
- Advanced portfolio optimization algorithms
- Multi-currency support
- Mobile application development
- API integration for third-party services

---

*Last Updated: September 2025*
