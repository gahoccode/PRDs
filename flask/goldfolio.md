# Vietnamese Financial Markets Analysis with Streamlit
## Product Requirements Document (Revised)

## 1. Overview

This document outlines the requirements for a Vietnamese financial markets analysis application built with Streamlit that combines data from multiple sources to provide investment insights. The application will analyze gold prices and currency exchange rates to identify patterns and market indicators using Streamlit's interactive data visualization capabilities.

## 2. Data Sources

- **Gold Price Data**: SJC gold prices with buy/sell rates
- **Exchange Rate Data**: VCB exchange rates for USD/VND pair

Refer to Gold.py to load gold price data. Do not modify Gold.py.

## 4. Functional Requirements

### 4.1 Gold Price Spread Analysis

#### 4.1.1 Buy/Sell Spread Trends
- Calculate daily spread between buy and sell prices for SJC gold
- Generate time series visualizations of spread trends
- Identify long-term patterns in spread behavior
- Calculate moving averages of spreads (7-day, 30-day, 90-day)

#### 4.1.2 Spread Volatility as Market Stress Indicator
- Calculate spread volatility using rolling standard deviation
- Establish normal vs. stressed market thresholds
- Create alerts for when spread volatility exceeds thresholds
- Compare spread volatility with market events

#### 4.1.3 Temporal Variations in Spread Patterns
- Apply 7-day moving average to smooth daily spread data
- Implement seasonality decomposition using the following methodology:
  1. Calculate monthly averages for gold spread data
  2. Compute monthly indices (Monthly Spread ÷ Average Monthly Spread)
  3. Calculate average seasonal indices across multiple years
  4. Deseasonalize data by dividing actual spread by seasonal indices
  5. Analyze the deseasonalized data for trends and patterns
  6. Reseasonalize projections by multiplying trend forecasts by seasonal indices
- Generate heat maps showing spread patterns across time periods


## 5. Technical Requirements

### 5.1 Data Processing
- Daily data ingestion from SJC 
- Date alignment and handling of missing values:
  - Sort time series by date in ascending order
  - Apply dropna() to remove missing values
  - Ensure consistent datetime index format
- Calculation of derived metrics:
  - Daily returns = df['price'].pct_change()
  - Annualized returns = Daily returns * 252
- Monthly returns = Daily returns *30
  - Volatility = Standard deviation of daily returns * √252
  - Spreads = Sell price - Buy price
- Implementation of rolling window analyses

## 6. Implementation Phases

### Phase 1: Data Integration
- Set up data ingestion from all sources
- Implement data cleaning and alignment
- Create base calculation functions
- Develop simple Streamlit time series visualizations

### Phase 2: Core Analysis
- Implement gold spread analysis functions
- Build basic Streamlit visualization components using st.line_chart and st.bar_chart

### Phase 3: Advanced Analytics
- Build interactive Streamlit dashboards with tabs and sidebars

### Phase 4: Refinement
- Optimize performance for large datasets using @st.cache_data
- Enhance Streamlit visualization aesthetics with custom CSS
- Add export capabilities with st.download_button

## 7. Success Metrics

- Accurate identification of market stress periods
- Consistency in correlation measurements
- Statistically significant lag relationships
- User engagement with visualizations and insights

## 8. API Rate Limiting Controls

### 8.1 Rate Limiter Configuration
- **Enable/Disable**: Option to turn rate limiters on or off
- **Delay Parameter**: Configurable delay between API calls (in seconds)
- **Batch Size**: Number of requests to process before applying delay
- **Retry Logic**: Configuration for failed request handling

### 8.2 Source-Specific Rate Limits
- **SJC Gold API**: 
  - Default delay: 2 seconds
  - Default interval: 1 day
  - Configurable range: 1-10 seconds
- **VCB Exchange Rate API (USD/VND)**:
  - Default delay: 2 seconds
  - Default interval: 1 day
  - Configurable range: 1-5 seconds

### 8.3 Rate Limit Monitoring in Streamlit
- Real-time display of API call rates using st.progress()
- Warning indicators when approaching rate limits using st.warning()
- Logging of rate limit events with st.write() to console
- Historical usage analytics visualized with st.bar_chart()


# Install dependencies
uv sync


## Appendix A: Streamlit Visualization Specifications

### Gold Price Spread Visualization
- **Type**: Multi-line chart using st.line_chart() or Plotly integration
- **X-axis**: Time (daily)
- **Y-axis**: Gold price and spread value
- **Features**:
  - Primary line showing gold buy price
  - Secondary line showing gold sell price
  - Shaded area representing spread
  - Overlay of rolling volatility
  - Implementation: st.plotly_chart() for advanced features

### Currency Impact Visualization
- **Type**: Correlation heatmap using Streamlit+Seaborn
- **Features**:
  - Color-coded correlation strengths
  - Time slider implemented with st.slider()
  - Implementation: st.pyplot() with seaborn heatmap

### Asset Correlation Dashboard
- **Type**: Interactive correlation matrix in Streamlit tabs
- **Features**:
  - Color gradient representing correlation strength
  - Date range selection with st.date_input()
  - Drill-down capability using st.expander()
  - Lag adjustment controls using st.slider()
  - Implementation: Combination of st.pyplot() and st.plotly_chart()
