# Troubleshooting

## Start with context

Confirm the tenant, subscription, account, region, run ID, and current lab state before changing anything. Many Azure failures are valid authorization, quota, policy, or regional-availability outcomes rather than command defects.

## Safe diagnosis order

1. Read the full error and correlation/request ID.
2. Run the lab preflight again.
3. Inspect provider registration, feature state, quota, SKU availability, and policy assignments.
4. Query the resource using the lab's canonical command surface.
5. Compare `.state/<run-id>/` with the live resource IDs.
6. Use the Portal only to recognize and corroborate state, not to bypass the documented command path.

Never paste secrets, tokens, or unredacted account output into an issue.
