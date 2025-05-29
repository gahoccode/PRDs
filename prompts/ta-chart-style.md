Main Price Chart (Top Panel)
Close Price: Solid blue line showing the primary price data
Moving Averages: Used different line styles to distinguish between them:
MA20: Blue dashed line (short-term trend)
MA50: Orange dashed line (medium-term trend)
MA200: Solid red line with increased thickness (long-term trend)
Buy Signals: Used distinct markers and colors to differentiate signal types:
Regular Buy Signals (RSI<30): Blue triangles (^) with size=80
Strong Buy Signals (with pattern+volume): Green stars (*) with size=200
Bullish Engulfing Patterns: Orange circles (o) with size=50, positioned slightly below the price for visibility
Trade Exits: Green circles (o) for profitable exits, Red X marks (x) for losing exits
RSI Panel (Middle Panel)
RSI Line: Purple line for clear distinction from price chart
Threshold Lines: Distinct colors with dashed styling:
Oversold (30): Green dashed line
Overbought (70): Red dashed line
Exit Level (40): Orange dashed line
Signal Markers: Added blue triangles at the RSI level when buy signals occurred
Volume Panel (Bottom Panel)
Making Bullish Volume Spikes Stand Out
The volume spikes were made to stand out through several techniques:

Contrast in Color and Opacity:
Regular volume bars: Light gray with 30% opacity (color='gray', alpha=0.3)
Volume spike bars: Solid purple (color='purple') with 100% opacity
Layering Approach:
Regular volume bars are plotted first as a background
Volume spike bars are plotted on top, creating a visual pop effect
This gives the immediate impression of "important" vs "background" volumes
Additional Marker Enhancement:
For strong buy signals (that include volume spikes), added a prominent green star marker
Star markers are positioned at 1.1× the height of the volume bar: vol * 1.1
Sized at 200 points (quite large) to ensure visibility
The code: axes[2].scatter(idx, vol * 1.1, marker='*', color='green', s=200)
Coordinated Visual System:
Purple for volume spikes in the volume panel coordinates with the purple RSI line
Green stars above volume bars match the green stars on the price chart
This creates a visually cohesive system that helps the eye track related signals across panels