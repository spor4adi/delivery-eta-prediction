# Delivery ETA Prediction

A machine learning project to predict food delivery time (ETA) based on order, weather, traffic, and location data.

# Problem Statement 
What's being predicted: the time taken from order placement to the order being delivered to (received by) the customer — captured in Time_taken (min).
This is a regression problem, since we're predicting a continuous value (minutes), not a category.
The prediction is made at order-placement time, meaning the model can only use data available at that instant — anything that happens afterward (pickup, in-transit weather/traffic, etc.) is off-limits.


Status: In progress — currently building out the initial pipeline.

