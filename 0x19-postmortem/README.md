Duration: The outage occurred from March 5, 2024, 10:00 PM to March 6, 2024, 1:30 AM (UTC).
Impact: The service experienced intermittent disruptions, resulting in slow response times and partial unavailability. Approximately 30% of users were affected, reporting difficulty accessing account information and performing transactions.
Root Cause: The root cause was identified as a misconfiguration in the load balancer settings, leading to uneven distribution of traffic and overload on certain servers.
Timeline:

Detection: March 5, 2024, 10:15 PM (UTC): Monitoring alert triggered due to increased latency.
Investigation: Engineers initiated investigation into server health metrics and network traffic patterns.
Misleading Paths: Initially, the focus was on database performance and network congestion, leading to temporary adjustments in caching configurations.
Escalation: Incident was escalated to the infrastructure team and system administrators for further analysis.
Resolution: Load balancer settings were reconfigured to evenly distribute traffic, and server capacity was scaled up to accommodate increased demand.
Root Cause and Resolution:

Root Cause: The misconfiguration in the load balancer settings caused uneven distribution of traffic, resulting in overload on certain servers while leaving others underutilized. This imbalance led to degraded performance and partial service unavailability.
Resolution: Load balancer configurations were corrected to evenly distribute traffic across servers. Additionally, server capacity was increased to handle peak loads more efficiently.
Corrective and Preventative Measures:

Improvements/Fixes:
Implement automated load testing procedures to identify potential configuration issues before they impact users.
Enhance monitoring systems to provide real-time visibility into traffic distribution and server performance.
Tasks:
Conduct a thorough review of load balancer configurations and ensure proper distribution logic.
Develop and implement automated load testing scripts to simulate various traffic patterns and assess system response.
Enhance monitoring dashboard to include traffic distribution metrics and server health indicators.
Schedule regular load balancing audits to proactively identify and address any configuration drift.
Establish a protocol for rapid scaling of server capacity during peak demand periods.
By addressing the root cause and implementing preventative measures, we aim to improve system resilience and minimize the risk of similar outages in the future.

