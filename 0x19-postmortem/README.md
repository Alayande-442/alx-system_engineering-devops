Postmortem project

POSTMORTEM REPORT
Issue Summary
Duration: The outage occurred on Aug 08, 2024, from 2:30 PM to 3:45 PM WAT.
Impact: The primary web service was down, affecting the login and payment processing functionalities. Users experienced 502 Bad Gateway errors when trying to access the site. Approximately 75% of our user base was affected.
Root Cause: The root cause was a misconfigured Nginx server that failed to properly communicate with the backend application servers due to a recent update that introduced compatibility issues.
Timeline
2:30 PM: Issue detected via monitoring alert indicating increased error rates and response times.
2:32 PM: Engineers began investigating the alerts and checking logs for anomalies.
2:40 PM: Initial assumption was a database overload, and database performance was checked.
2:50 PM: Investigation showed no signs of database issues; focus shifted to application servers.
3:00 PM: Noticed misleading logs suggesting network connectivity issues.
3:10 PM: Escalated to the network operations team for further investigation.
3:20 PM: Network team found no issues; escalated to the application infrastructure team.
3:30 PM: Application infrastructure team identified a recent Nginx update as the potential cause.
3:40 PM: Rolled back the Nginx update to the previous stable version.
3:45 PM: Issue resolved, and services fully restored.
Root Cause and Resolution
Root Cause: The incident was caused by a misconfigured Nginx server due to a recent update. The update introduced compatibility issues with the backend application servers, leading to failed communications and resulting in 502 Bad Gateway errors for users.
Resolution: The resolution involved rolling back the Nginx server to the previous stable version. This rollback restored proper communication between Nginx and the backend servers, resolving the outage and restoring service functionality.
Corrective and Preventative Measures
Improvements/Fixes:
Improve the update and deployment process to include comprehensive compatibility testing.
Enhance monitoring to detect communication issues between Nginx and backend servers more quickly.
Update incident response playbooks to include faster identification and rollback procedures for configuration issues.
Action Items:
Task: Patch Nginx server to the latest stable version that has been verified for compatibility.
Owner: DevOps Team
Due Date: Aug 20, 2024
Task: Implement automated compatibility tests for all Nginx updates.
Owner: QA Team
Due Date: Aug 25, 2024
Task: Add detailed monitoring and alerting on Nginx to backend server communication.
Owner: Monitoring Team
Due Date: Aug 18, 2024
Task: Update incident response playbook to include steps for rapid rollback of updates.
Owner: Incident Response Team
Due Date: Aug 22, 2024
Task: Conduct a training session for the engineering team on identifying and resolving configuration issues.
Owner: Engineering Manager
Due Date: Aug 30, 2024

A Dash of Humor 
To lighten the mood, here's a little tech joke for you:
Why do programmers prefer dark mode? Because light attracts bugs!😂


