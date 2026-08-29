# Data Dictionary

| Column | Dtype | Nulls | Meaning |
|---|---|---|---|
| ID | str | 0 | Unique identifier for each order/delivery record, the primary key for the row. |
| Delivery_person_ID | str | 0 | Identifier tying the order to a specific delivery rider, the same ID recurs across multiple orders handled by that rider. |
| Delivery_person_Age | float64 | 1854 | Age of the rider who handled the delivery, a rough proxy for experience level. Stored as float only because NaNs force pandas out of int. |
| Delivery_person_Ratings | float64 | 1908 | The rider's cumulative average customer rating going into this delivery, not a rating of this specific order. |
| Restaurant_latitude | float64 | 0 | Latitude of the pickup point, used with longitude to compute trip distance. |
| Restaurant_longitude | float64 | 0 | Longitude of the pickup point, paired with Restaurant_latitude. |
| Delivery_location_latitude | float64 | 0 | Latitude of the customer's drop off point. |
| Delivery_location_longitude | float64 | 0 | Longitude of the drop off point, paired with Delivery_location_latitude. |
| Order_Date | str | 0 | Calendar date the order was placed, useful for day of week or seasonal effects, stored as text rather than a parsed date. |
| Time_Orderd | str | 1731 | Clock time the customer placed the order (typo in the original column name, "Orderd"). Missingness here likely reflects a logging gap rather than the event not occurring, since every order has a placement time in reality. |
| Time_Order_picked | str | 0 | Clock time the rider actually picked up the food from the restaurant, the gap between this and Time_Orderd reflects kitchen or prep delay. |
| Weather_conditions | str | 616 | Weather at the time of the delivery, confirmed categories are Fog, Stormy, Sandstorms, Windy, Cloudy, Sunny, an external condition that could slow the rider down. |
| Road_traffic_density | str | 601 | Categorical traffic level on the route, confirmed categories are Jam, High, Medium, Low, a direct driver of delivery time. |
| Vehicle_condition | int64 | 0 | An encoded score for how good a state the rider's vehicle is in (e.g. 0 to 3 scale). Uncertain whether this reflects mechanical condition, age of vehicle, or upkeep/cleanliness, the exact scale definition isn't self evident from the data alone, flagging this one. |
| Type_of_order | str | 0 | What kind of order it was, confirmed categories are Snack, Meal, Drinks, Buffet, a proxy for how long the kitchen takes to prepare it. |
| Type_of_vehicle | str | 0 | The mode of transport the rider used, confirmed categories are motorcycle, scooter, electric_scooter, bicycle, affects achievable speed. |
| multiple_deliveries | float64 | 993 | How many other orders the rider was juggling in the same trip alongside this one, i.e. whether this was a solo drop off (0) or a batched run where the rider stacked several orders together, adding detours and thus time. Stored as float only because of the NaNs, conceptually it's a small integer count. |
| Festival | str | 228 | Whether the delivery happened on or around a festival day (Yes/No), festivals typically mean more orders and heavier traffic, so this acts as a demand/congestion flag. |
| City | str | 1200 | Not a literal city name but a delivery zone category, confirmed values are Metropolitian (note the typo in the source data), Urban, Semi-Urban, a proxy for infrastructure quality and typical traffic patterns. |
| Time_taken (min) | int64 | 0 | The target variable, total minutes from order to delivery completion. |
