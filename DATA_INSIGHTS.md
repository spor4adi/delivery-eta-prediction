# Data Insights

### 1. Target is mildly right skewed
* **Evidence:** skew ≈ 0.48, floor near 10 min, no long extreme tail
* **Implication:** minor log/sqrt transform experiment for linear models; likely unnecessary for tree based models

### 2. Traffic is a deterministic function of hour
* **Evidence:** hour to traffic mapping holds with zero exceptions across all 45,257 rows
* **Implication:** use `order_hour` (or an hour bucket) rather than `Road_traffic_density`, since the two are redundant and including both wastes a feature slot

### 3. multiple_deliveries is the strongest, non linear driver found so far
* **Evidence:** larger effect on delivery time than distance, and the relationship isn't a straight line
* **Implication:** keep as a feature, but encode as categorical/ordinal or let a tree model capture the curve rather than assuming linear scaling

### 4. Distance alone is a weak predictor
* **Evidence:** little relationship to delivery time on its own
* **Implication:** deprioritize as a standalone feature; a distance × traffic interaction is an untested hypothesis worth trying later, not yet supported by evidence

### 5. Weather is near random, but a Jam + Fog/Cloudy interaction spike exists
* **Evidence:** weather alone carries almost no signal; a traffic × weather combination shows a spike
* **Implication:** exclude weather standalone; treat the interaction as a candidate feature pending a sample size check